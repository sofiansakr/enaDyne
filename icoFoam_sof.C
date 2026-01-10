/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM v10: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           |
     \\/     M anipulation  |
\*---------------------------------------------------------------------------*/
/*------------*\
  27.10.2025
  =========     
  \\sofian/  
   \\Sakr/ 
    \\  /    
     \\/     
\*---------------------------------------------------------------------------*/
#include "fvCFD.H"
#include "pisoControl.H"
#include <cstdlib>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

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
    
    // Activation times for forces and scalars
    scalar forceStartTime = 2.0;      // Start forces at 2.0 seconds
    scalar scalarStartTime = 2.0;     // Start scalars at 2.0 seconds
    bool forcesActivated = false;
    bool scalarsActivated = false;
    
    // Variables for transit time tracking
    List<scalar> transitTimes(nRegions, 0.0);
    
    // Clear plasma indicator initially (will be set when scalars activate)
    plasmaIndicator = dimensionedScalar("zero", dimless, 0.0);
    
    if (Pstream::master())
    {
        Info<< "\n=== SIMULATION SETUP ===\n";
        Info<< "Forces will activate at t = " << forceStartTime << " s\n";
        Info<< "Passive scalars injection will start at t = " << scalarStartTime << " s\n";
        Info<< "========================\n" << endl;
    }
    
    Info<< "\nStarting time loop\n" << endl;
    
    while (runTime.loop())
    {
        #include "CourantNo.H"
        
        if (adjustTimeStep)
        {
            scalar newDeltaT = maxCo * runTime.deltaTValue() / (CoNum + SMALL);
            newDeltaT = min(newDeltaT, maxDeltaT);
            runTime.setDeltaT(newDeltaT);
            if (Pstream::master())
            {
                Info<< "Adaptive deltaT adjusted to: " << runTime.deltaTValue()
                    << " s (CoNum: " << CoNum << ")\n";
            }
        }
        
        Info<< "Time = " << runTime.userTimeName() << nl << endl;
        
        scalar currentTime = runTime.time().value();
        
        // === CONTROL FORCES BASED ON TIME ===
        if (currentTime >= forceStartTime && !forcesActivated)
        {
            // First timestep with forces - regenerate force field
            if (Pstream::master())
            {
                Info<< "\n*** ACTIVATING FORCES at t = " << currentTime << " s ***\n" << endl;
            }
            
            F = dimensionedVector("zeroF", F.dimensions(), vector::zero);
            
            forAll(mesh.C(), cellI)
            {
                const vector& cc = mesh.C()[cellI];
                scalar x = cc.x(), y = cc.y();

                bool inTop    = (y >= yTopMin - eps    && y <= yTopMax + eps);
                bool inBottom = (y >= yBottomMin - eps && y <= yBottomMax + eps);
                if (!(inTop || inBottom)) continue;

                const bool useTop = inTop;
                scalar Fy = useTop ? +FyMag : -FyMag;

                label  nPairsBand    = useTop ? nPairsTop      : nPairsBottom;
                scalar pairPitchBand = useTop ? pairPitchTop   : pairPitchBottom;
                scalar xCenter0Band  = useTop ? xCenter0Top    : xCenter0Bot;

                if (nPairsBand <= 0) continue;

                for (label i = 0; i < nPairsBand; ++i)
                {
                    scalar xc = xCenter0Band + i*pairPitchBand;

                    scalar xLcenter = xc - halfLRcenter;
                    scalar xRcenter = xc + halfLRcenter;

                    scalar leftMin  = xLcenter - halfLen;
                    scalar leftMax  = xLcenter + halfLen;
                    scalar rightMin = xRcenter - halfLen;
                    scalar rightMax = xRcenter + halfLen;

                    if (x >= leftMin - eps && x < leftMax + eps)
                    {
                        F.primitiveFieldRef()[cellI] = vector(-FxMag, Fy, 0);
                        break;
                    }

                    if (x >= rightMin - eps && x < rightMax + eps)
                    {
                        F.primitiveFieldRef()[cellI] = vector(+FxMag, Fy, 0);
                        break;
                    }
                }
            }
            
            forcesActivated = true;
        }
        else if (currentTime < forceStartTime)
        {
            // Keep forces at zero
            F = dimensionedVector("zeroF", F.dimensions(), vector::zero);
        }
        
        // === CONTROL SCALARS BASED ON TIME ===
        if (currentTime >= scalarStartTime && !scalarsActivated)
        {
            // First timestep with scalars - set up plasma indicator
            if (Pstream::master())
            {
                Info<< "\n*** ACTIVATING SCALAR INJECTION at t = 2" << currentTime << " s ***\n" << endl;
            }
            
            // Initialize plasma indicator field based on geometry
            forAll(mesh.C(), cellI)
            {
                const vector& cc = mesh.C()[cellI];
                scalar x = cc.x(), y = cc.y();
                
                bool inTop    = (y >= yTopMin - eps && y <= yTopMax + eps);
                bool inBottom = (y >= yBottomMin - eps && y <= yBottomMax + eps);
                
                if (inTop || inBottom)
                {
                    const bool useTop = inTop;
                    label  nPairsBand = useTop ? nPairsTop : nPairsBottom;
                    scalar pairPitchBand = useTop ? pairPitchTop : pairPitchBottom;
                    scalar xCenter0Band = useTop ? xCenter0Top : xCenter0Bot;
                    
                    for (label i = 0; i < nPairsBand; ++i)
                    {
                        scalar xc = xCenter0Band + i*pairPitchBand;
                        scalar xLcenter = xc - halfLRcenter;
                        scalar xRcenter = xc + halfLRcenter;
                        
                        scalar leftMin = xLcenter - halfLen;
                        scalar leftMax = xLcenter + halfLen;
                        scalar rightMin = xRcenter - halfLen;
                        scalar rightMax = xRcenter + halfLen;
                        
                        if ((x >= leftMin - eps && x < leftMax + eps) ||
                            (x >= rightMin - eps && x < rightMax + eps))
                        {
                            plasmaIndicator[cellI] = 1.0;
                            break;
                        }
                    }
                }
            }
            
            scalarsActivated = true;
        }
        
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
        
        // === GLOBAL PASSIVE SCALAR TRANSPORT (ONLY ACTIVE AFTER scalarStartTime) ===
        if (currentTime >= scalarStartTime)
        {
            // Update source term based on plasma indicator
            forAll(mesh.C(), cellI)
            {
                if (plasmaIndicator[cellI] > 0.5)
                {
                    Sc[cellI] = Sc_mag.value() * (1.0 - c[cellI]);
                }
                else
                {
                    Sc[cellI] = 0.0;
                }
            }
        }
        else
        {
            // Before scalar activation, ensure no source term
            Sc = dimensionedScalar("zero", Sc.dimensions(), 0.0);
        }
        
        // Solve scalar transport equation
        fvScalarMatrix cEqn
        (
            fvm::ddt(c)
          + fvm::div(phi, c)
          - fvm::laplacian(Dc, c)
          ==
            Sc
        );
        
        cEqn.relax();
        cEqn.solve();
        c.max(0.0);
        c.min(1.0);
        
        // === GLOBAL RESIDENCE TIME TRACKING ===
        fvScalarMatrix tauEqn
        (
            fvm::ddt(tau)
          + fvm::div(phi, tau)
          - fvm::laplacian(Dc, tau)
          ==
            plasmaIndicator  // Will be zero until scalars activate
        );
        
        tauEqn.relax();
        tauEqn.solve();
        tau.max(0.0);
        
        // === CALCULATE AVERAGE RESIDENCE TIME ===
        forAll(c, cellI)
        {
            if (c[cellI] > 0.01)
            {
                tauAvg[cellI] = tau[cellI] / c[cellI];
            }
            else
            {
                tauAvg[cellI] = 0.0;
            }
        }
        
        // === REGION-SPECIFIC SCALAR TRANSPORT (ONLY ACTIVE AFTER scalarStartTime) ===
        if (currentTime >= scalarStartTime)
        {
            for (label r = 0; r < nRegions; r++)
            {
                volScalarField& c_r = c_regions[r];
                volScalarField& tau_r = tau_regions[r];
                volScalarField& Sc_r = Sc_regions[r];
                
                // Update source term for this region
                forAll(mesh.C(), cellI)
                {
                    const vector& cc = mesh.C()[cellI];
                    scalar x = cc.x();
                    scalar y = cc.y();
                    
                    // Check if cell is in this region
                    if (x >= regionXmin[r] - eps && x <= regionXmax[r] + eps &&
                        y >= regionYmin[r] - eps && y <= regionYmax[r] + eps)
                    {
                        Sc_r[cellI] = Sc_mag.value() * (1.0 - c_r[cellI]);
                    }
                    else
                    {
                        Sc_r[cellI] = 0.0;
                    }
                }
                
                // Solve concentration for this region
                fvScalarMatrix cRegionEqn
                (
                    fvm::ddt(c_r)
                  + fvm::div(phi, c_r)
                  - fvm::laplacian(Dc, c_r)
                  ==
                    Sc_r
                );
                
                cRegionEqn.relax();
                cRegionEqn.solve();
                c_r.max(0.0);
                c_r.min(1.0);
                
                // Create plasma indicator for this region
                volScalarField plasmaIndicator_r
                (
                    IOobject
                    (
                        "plasmaInd_temp",
                        runTime.timeName(),
                        mesh,
                        IOobject::NO_READ,
                        IOobject::NO_WRITE
                    ),
                    mesh,
                    dimensionedScalar("zero", dimless, 0.0)
                );
                
                forAll(mesh.C(), cellI)
                {
                    const vector& cc = mesh.C()[cellI];
                    scalar x = cc.x();
                    scalar y = cc.y();
                    
                    if (x >= regionXmin[r] - eps && x <= regionXmax[r] + eps &&
                        y >= regionYmin[r] - eps && y <= regionYmax[r] + eps)
                    {
                        plasmaIndicator_r[cellI] = 1.0;
                    }
                }
                
                // Solve residence time for this region
                fvScalarMatrix tauRegionEqn
                (
                    fvm::ddt(tau_r)
                  + fvm::div(phi, tau_r)
                  - fvm::laplacian(Dc, tau_r)
                  ==
                    plasmaIndicator_r
                );
                
                tauRegionEqn.relax();
                tauRegionEqn.solve();
                tau_r.max(0.0);
            }
        }
        
        // === TRANSIT TIME ANALYSIS (only when forces are active) ===
        if (currentTime >= forceStartTime && runTime.outputTime())
        {
            Info<< "\n=== STREAMER TRANSIT TIME ANALYSIS ===\n";
            
            scalar totalTransitTime = 0.0;
            label activeRegions = 0;
            
            for (label r = 0; r < nRegions; r++)
            {
                scalar sumVx = 0.0;
                scalar sumVy = 0.0;
                scalar sumVmag = 0.0;
                scalar cellCount = 0.0;
                
                forAll(mesh.C(), cellI)
                {
                    const vector& cc = mesh.C()[cellI];
                    scalar x = cc.x();
                    scalar y = cc.y();
                    
                    if (x >= regionXmin[r] - eps && x <= regionXmax[r] + eps &&
                        y >= regionYmin[r] - eps && y <= regionYmax[r] + eps)
                    {
                        sumVx += U[cellI].x();
                        sumVy += U[cellI].y();
                        sumVmag += mag(U[cellI]);
                        cellCount += 1.0;
                    }
                }
                
                reduce(sumVx, sumOp<scalar>());
                reduce(sumVy, sumOp<scalar>());
                reduce(sumVmag, sumOp<scalar>());
                reduce(cellCount, sumOp<scalar>());
                
                if (cellCount > SMALL)
                {
                    scalar avgVx = sumVx / cellCount;
                    scalar avgVy = sumVy / cellCount;
                    scalar avgVmag = sumVmag / cellCount;
                    
                    scalar lengthX = regionXmax[r] - regionXmin[r];
                    scalar lengthY = regionYmax[r] - regionYmin[r];
                    
                    scalar transitTimeX = lengthX / (mag(avgVx) + SMALL);
                    scalar transitTimeY = lengthY / (mag(avgVy) + SMALL);
                    
                    scalar effectiveTransit = Foam::sqrt(transitTimeX*transitTimeX + 
                                                        transitTimeY*transitTimeY);
                    
                    scalar simpleTransit = Foam::sqrt(lengthX*lengthX + lengthY*lengthY) / 
                                         (avgVmag + SMALL);
                    
                    transitTimes[r] = effectiveTransit;
                    totalTransitTime += effectiveTransit;
                    activeRegions++;
                    
                    if (Pstream::master())
                    {
                        Info<< regionNames[r] << ":\n"
                            << "  Avg velocity: (" << avgVx << ", " << avgVy 
                            << ") m/s, |V| = " << avgVmag << " m/s\n"
                            << "  Transit time (X): " << transitTimeX << " s\n"
                            << "  Transit time (Y): " << transitTimeY << " s\n"
                            << "  Effective transit: " << effectiveTransit << " s\n"
                            << "  Simple transit: " << simpleTransit << " s\n";
                    }
                }
                else if (Pstream::master())
                {
                    Info<< regionNames[r] << ": No flow in region\n";
                }
            }
            
            if (Pstream::master() && activeRegions > 0)
            {
                scalar avgTransitTime = totalTransitTime / activeRegions;
                Info<< "\nAverage transit time across all active streamers: " 
                    << avgTransitTime << " s\n";
                Info<< "Total active streamers: " << activeRegions << "/" 
                    << nRegions << "\n";
                Info<< "=======================================\n" << endl;
            }
        }
        
        runTime.write();
        
        // === Estimated Completion Time ===
        if (Pstream::master())
        {
            scalar simTimeCompleted = runTime.time().value() - runTime.startTime().value();
            scalar simTimeTotal = runTime.endTime().value() - runTime.startTime().value();
            scalar percentComplete = simTimeCompleted / (simTimeTotal + SMALL);
            scalar elapsedCPU = runTime.elapsedCpuTime();
            scalar estTotalTime = elapsedCPU / (percentComplete + SMALL);
            scalar estRemaining = estTotalTime - elapsedCPU;
            
            Info<< "\nEstimated time to completion: "
                << estRemaining << " s ("
                << estRemaining / 60 << " minutes) "
                << "Progress: " << 100 * percentComplete << " %\n" << endl;
        }
    }
    
    Info<< "End\n" << endl;
    
    return 0;
}
