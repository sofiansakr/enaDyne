Info<< "Reading physicalProperties\n" << endl;

IOdictionary physicalProperties
(
    IOobject
    (
        "physicalProperties",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);

dimensionedScalar nu
(
    "nu",
    dimViscosity,
    physicalProperties.lookup("nu")
);

Info<< "Reading field p\n" << endl;
volScalarField p
(
    IOobject
    (
        "p",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);


Info<< "Reading field U\n" << endl;
volVectorField U
(
    IOobject
    (
        "U",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh
);

Info<< "Creating force field F\n"<<endl;
volVectorField F
(
    IOobject
    (
        "F",
        runTime.timeName(),
        mesh,
        IOobject::MUST_READ,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedVector("zero", dimensionSet(0,1,-2,0,0,0,0), vector(0,0,0))
);

    Info<<"Generating force field\n"<<endl;
	
	// Kraftwerte für Oberseite
	scalar Force_X = 1e3;
	scalar ymax = 18e-3;
	
    forAll(mesh.C(), cellI)
{

		  /***************TOP*********************/
			
  		  /* 1 Electrode up left*/
          if(
          mesh.C()[cellI].x() > 6.9e-3 &&
          mesh.C()[cellI].x() < 9.9e-3 &&
          mesh.C()[cellI].y() > ymax - 0.4e-3 &&
          mesh.C()[cellI].y() < ymax
          )
          {
              F[cellI] = vector(-Force_X, Force_X, 0);
          }
        
          /* 1 Electrode up right*/
          if(
          mesh.C()[cellI].x() > 10.1e-3 &&
          mesh.C()[cellI].x() < 13.1e-3 &&
          mesh.C()[cellI].y() > ymax - 0.4e-3 &&
          mesh.C()[cellI].y() < ymax
          )
          {
              F[cellI] = vector(+Force_X, Force_X, 0);
          }
        
        
  		  /* 2 Electrode up left*/
          if(
          mesh.C()[cellI].x() > 16.9e-3 &&
          mesh.C()[cellI].x() < 19.9e-3 &&
          mesh.C()[cellI].y() > ymax - 0.4e-3 &&
          mesh.C()[cellI].y() < ymax
          )
          {
              F[cellI] = vector(-Force_X, Force_X, 0);
          }
        
          /* 2 Electrode up right*/
          if(
          mesh.C()[cellI].x() > 20.1e-3 &&
          mesh.C()[cellI].x() < 23.1e-3 &&
          mesh.C()[cellI].y() > ymax - 0.4e-3 &&
          mesh.C()[cellI].y() < ymax
          )
          {
              F[cellI] = vector(+Force_X, Force_X, 0);
          }
		  
  		  /* 3 Electrode up left*/
          if(
          mesh.C()[cellI].x() > 26.9e-3 &&
          mesh.C()[cellI].x() < 29.9e-3 &&
          mesh.C()[cellI].y() > ymax - 0.4e-3 &&
          mesh.C()[cellI].y() < ymax
          )
          {
              F[cellI] = vector(-Force_X, Force_X, 0);
          }
        
          /* 3 Electrode up right*/
          if(
          mesh.C()[cellI].x() > 30.1e-3 &&
          mesh.C()[cellI].x() < 33.1e-3 &&
          mesh.C()[cellI].y() > ymax - 0.4e-3 &&
          mesh.C()[cellI].y() < ymax
          )
          {
              F[cellI] = vector(+Force_X, Force_X, 0);
          }
		  
		  
		  /* Center Electrode up left*/
          if(
          mesh.C()[cellI].x() > 31.9e-3  &&
          mesh.C()[cellI].x() < 34.9e-3 &&
          mesh.C()[cellI].y() > ymax / 2 + 0.05e-3 &&
          mesh.C()[cellI].y() < ymax / 2 + 0.6e-3
          )
          {
              F[cellI] = vector(-Force_X, -Force_X, 0);
          }
		  
		  /* Center Electrode up right*/
          if(
          mesh.C()[cellI].x() > 11.9e-3 &&
          mesh.C()[cellI].x() < 14.9e-3 &&
          mesh.C()[cellI].y() > ymax / 2 + 0.05e-3 &&
          mesh.C()[cellI].y() < ymax / 2 + 0.6e-3
          )
          {
              F[cellI] = vector(-Force_X, -Force_X, 0);
          }
		  
		  
		  /***************BOTTOM*********************/
		  
  		  /* 1 Electrode up left*/
          if(
          mesh.C()[cellI].x() > 6.9e-3 &&
          mesh.C()[cellI].x() < 9.9e-3 &&
          mesh.C()[cellI].y() > 0e-3 &&
          mesh.C()[cellI].y() < 0.4e-3
          )
          {
              F[cellI] = vector(-Force_X, -Force_X, 0);
          }
        
          /* 1 Electrode up right*/
          if(
          mesh.C()[cellI].x() > 10.1e-3 &&
          mesh.C()[cellI].x() < 13.1e-3 &&
          mesh.C()[cellI].y() > 0e-3 &&
          mesh.C()[cellI].y() < 0.4e-3
          )
          {
              F[cellI] = vector(+Force_X, -Force_X, 0);
          }
        
        
  		  /* 2 Electrode up left*/
          if(
          mesh.C()[cellI].x() > 16.9e-3 &&
          mesh.C()[cellI].x() < 19.9e-3 &&
          mesh.C()[cellI].y() > 0e-3 &&
          mesh.C()[cellI].y() < 0.4e-3
          )
          {
              F[cellI] = vector(-Force_X, -Force_X, 0);
          }
        
          /* 2 Electrode up right*/
          if(
          mesh.C()[cellI].x() > 20.1e-3 &&
          mesh.C()[cellI].x() < 23.1e-3 &&
          mesh.C()[cellI].y() > 0e-3 &&
          mesh.C()[cellI].y() < 0.4e-3
          )
          {
              F[cellI] = vector(+Force_X, -Force_X, 0);
          }
		  
  		  /* 3 Electrode up left*/
          if(
          mesh.C()[cellI].x() > 26.9e-3 &&
          mesh.C()[cellI].x() < 29.9e-3 &&
          mesh.C()[cellI].y() > 0e-3 &&
          mesh.C()[cellI].y() < 0.4e-3
          )
          {
              F[cellI] = vector(-Force_X, -Force_X, 0);
          }
        
          /* 3 Electrode up right*/
          if(
          mesh.C()[cellI].x() > 30.1e-3 &&
          mesh.C()[cellI].x() < 33.1e-3 &&
          mesh.C()[cellI].y() > 0e-3 &&
          mesh.C()[cellI].y() < 0.4e-3
          )
          {
              F[cellI] = vector(+Force_X, -Force_X, 0);
          }
		  
		  
		  
		  
		  /* Center Electrode bottom left*/
          if(
          mesh.C()[cellI].x() > 25.1e-3 &&
          mesh.C()[cellI].x() < 28.1e-3 &&
          mesh.C()[cellI].y() > ymax / 2 - 0.6e-3 &&
          mesh.C()[cellI].y() < ymax / 2 - 0.05e-3
          )
          {
              F[cellI] = vector(+Force_X, +Force_X, 0);
          }
		  
		  /* Center Electrode bottom right*/
          if(
          mesh.C()[cellI].x() > 5.1e-3 &&
          mesh.C()[cellI].x() < 8.1e-3 &&
          mesh.C()[cellI].y() > ymax / 2 - 0.6e-3 &&
          mesh.C()[cellI].y() < ymax / 2 - 0.05e-3
          )
          {
              F[cellI] = vector(+Force_X, +Force_X, 0);
          }
		  
  		  
}
F.write();


#include "createPhi.H"


label pRefCell = 0;
scalar pRefValue = 0.0;
setRefCell(p, mesh.solution().dict().subDict("PISO"), pRefCell, pRefValue);
mesh.schemes().setFluxRequired(p.name());
