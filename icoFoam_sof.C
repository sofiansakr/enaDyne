/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM v10: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           |
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/

/*------------*\
  09.05.2025
  =========     
  \\sofian/  
   \\Sakr/ 
    \\  /    
     \\/     
\*-----------*/


#include "fvCFD.H"
#include "pisoControl.H"

int main(int argc, char *argv[])
{
    #include "setRootCaseLists.H"
    #include "createTime.H"
    #include "createMesh.H"

    pisoControl piso(mesh);

    #include "createFields.H"
    #include "initContinuityErrs.H"

    // Read time-stepping parameters from controlDict
    bool adjustTimeStep = runTime.controlDict().lookupOrDefault<Switch>("adjustTimeStep", false);
    scalar maxCo        = runTime.controlDict().lookupOrDefault<scalar>("maxCo", 0.08);
    scalar maxDeltaT    = runTime.controlDict().lookupOrDefault<scalar>("maxDeltaT", GREAT);

    Info<< "\nStarting time loop\n" << endl;

    while (runTime.loop())
    {
        #include "CourantNo.H"

        if (adjustTimeStep)
        {
            scalar newDeltaT = maxCo * runTime.deltaTValue() / (CoNum + SMALL);
            newDeltaT = min(newDeltaT, maxDeltaT);
            runTime.setDeltaT(newDeltaT);

            Info<< "Adaptive deltaT adjusted to: " << runTime.deltaTValue()
                << " s (CoNum: " << CoNum << ")\n";
        }

        Info<< "Time = " << runTime.userTimeName() << nl << endl;

        // Momentum predictor
        fvVectorMatrix UEqn
        (
            fvm::ddt(U)
          + fvm::div(phi, U)
          - fvm::laplacian(nu, U)
        );

        if (piso.momentumPredictor())
        {
            solve(UEqn == -fvc::grad(p) + F);
        }

        // --- PISO loop
        while (piso.correct())
        {
            volScalarField rAU(1.0/UEqn.A());
            volVectorField HbyA(constrainHbyA(rAU*UEqn.H(), U, p));
            surfaceScalarField phiHbyA
            (
                "phiHbyA",
                fvc::flux(HbyA)
              + fvc::interpolate(rAU)*fvc::ddtCorr(U, phi)
            );

            adjustPhi(phiHbyA, U, p);
            constrainPressure(p, U, phiHbyA, rAU);

            while (piso.correctNonOrthogonal())
            {
                fvScalarMatrix pEqn
                (
                    fvm::laplacian(rAU, p) == fvc::div(phiHbyA)
                );

                pEqn.setReference(pRefCell, pRefValue);
                pEqn.solve();

                if (piso.finalNonOrthogonalIter())
                {
                    phi = phiHbyA - pEqn.flux();
                }
            }

            #include "continuityErrs.H"

            U = HbyA - rAU*fvc::grad(p);
            U.correctBoundaryConditions();
        }

        runTime.write();

        // === Estimated Completion Time ===
	{
	    scalar simTimeCompleted = runTime.time().value() - runTime.startTime().value();
	    scalar simTimeTotal = runTime.endTime().value() - runTime.startTime().value();
	    scalar percentComplete = simTimeCompleted / (simTimeTotal + SMALL);

	    scalar elapsedCPU = runTime.elapsedCpuTime();
	    scalar estTotalTime = elapsedCPU / (percentComplete + SMALL);
	    scalar estRemaining = estTotalTime - elapsedCPU;

	    Info<< "Estimated time to completion: "
		<< estRemaining << " s ("
		<< estRemaining / 60 << " minutes) "
		<< "Progress: " << 100 * percentComplete << " %\n" << endl;
	}

    }


    Info<< "End\n" << endl;
    return 0;
}

