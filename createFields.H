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
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedVector("zero", dimensionSet(0,1,-2,0,0,0,0), vector(0,0,0))
);

Info<<"Force field created (will be activated at t = 2.0s in solver)\n"<<endl;

// ================== Parametric force layout (pairs on top & bottom) ==================
// X-force:  left area  -> -FxMag
//           right area -> +FxMag
// Y-force:  bottom band -> -FyMag
//           top band    -> +FyMag

// -------- Parameters you can tweak --------
scalar FxMag       = 2e3;      // x-force magnitude (sign from left/right)
scalar FyMag       = 2e3;      // y-force magnitude (sign from top/bottom)

//scalar Lx          = 50e-3;    // total reactor length in x (meters)
scalar Ly          = 15e-3;    // total reactor height in y (meters)

// Separate number of pairs on each face
label  nPairsTop      = 4;
label  nPairsBottom   = 4;

// Pair geometry (shared)
scalar pairWidth   = 10e-3;     // total width of one pair (left + internal gap + right)
scalar pairGap     = 0.2e-3;   // internal gap inside a pair (edge-to-edge)
scalar areaHeight  = 0.4e-3;   // band thickness from boundary inward (y)

// Center-to-center spacing (zero gap allowed when == pairWidth)
scalar pairPitchTop    = 10e-3;
scalar pairPitchBottom = 10e-3;

// >>> Shifts (meters) applied FROM the base positions below <
scalar firstCenterShiftTop    = 0.0e-3;  // + shifts top first center to +x
scalar firstCenterShiftBottom = 0.0e-3;  // + shifts bottom first center to +x

// -------- Derived (do not edit) --------
if (pairWidth <= pairGap)
{
    FatalErrorInFunction
        << "pairWidth (" << pairWidth << ") must be > pairGap (" << pairGap << ")"
        << abort(FatalError);
}

scalar areaLen       = 0.5*(pairWidth - pairGap);   // length of ONE rectangle
scalar halfLen       = 0.5*areaLen;
scalar halfLRcenter  = 0.5*(areaLen + pairGap);     // |center(L/R) - center(pair)|

// allow zero gap; only forbid true overlap
if (nPairsTop    > 0 && pairPitchTop    < pairWidth)
    FatalErrorInFunction << "pairPitchTop must be >= pairWidth" << abort(FatalError);
if (nPairsBottom > 0 && pairPitchBottom < pairWidth)
    FatalErrorInFunction << "pairPitchBottom must be >= pairWidth" << abort(FatalError);

// ===== Base first-center positions (as you specified) =====
scalar xBaseTop =       pairPitchTop;
scalar xBaseBot =       pairPitchBottom;

// Apply your shifts FROM the base values
scalar xCenter0Top = (nPairsTop    > 0) ? (xBaseTop + firstCenterShiftTop)    : 0.0;
scalar xCenter0Bot = (nPairsBottom > 0) ? (xBaseBot + firstCenterShiftBottom) : 0.0;

// y-bands
scalar yTopMin = Ly - areaHeight, yTopMax = Ly;
scalar yBottomMin = 0.0, yBottomMax = areaHeight;

// ================== Initialize force field as zero ==================
// Forces will be applied in the main solver at t = 2.0 seconds
F = dimensionedVector("zeroF", F.dimensions(), vector::zero);

// half-open bounds help when gap == 0
scalar eps = SMALL;

Info<< "Force field initialized to zero (will be activated at t=2.0s in solver)\n" << endl;

// ================== GLOBAL SCALAR FIELDS ==================
Info<< "\nCreating global passive scalar field c\n" << endl;

volScalarField c
(
    IOobject
    (
        "c",
        runTime.timeName(),
        mesh,
        IOobject::READ_IF_PRESENT,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar("zero", dimless, 0.0)
);

IOdictionary transportProperties
(
    IOobject
    (
        "transportProperties",
        runTime.constant(),
        mesh,
        IOobject::MUST_READ_IF_MODIFIED,
        IOobject::NO_WRITE
    )
);

dimensionedScalar Dc
(
    "Dc",
    dimensionSet(0, 2, -1, 0, 0, 0, 0),
    transportProperties.lookup("Dc")
);

dimensionedScalar Sc_mag
(
    "Sc_mag", 
    dimensionSet(0, 0, -1, 0, 0, 0, 0),
    transportProperties.lookup("Sc_mag")
);

Info<< "Scalar diffusion coefficient Dc = " << Dc.value() << " m^2/s\n";
Info<< "Scalar source magnitude Sc_mag = " << Sc_mag.value() << " 1/s\n";

volScalarField Sc
(
    IOobject
    (
        "Sc",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar("zero", Sc_mag.dimensions(), 0.0)
);

Info<< "Scalar injection will start at t = 2.0s in plasma regions\n" << endl;

// === GLOBAL RESIDENCE TIME AND TRACKING FIELDS ===
Info<< "\nCreating global residence time field tau\n" << endl;

volScalarField tau
(
    IOobject
    (
        "tau",
        runTime.timeName(),
        mesh,
        IOobject::READ_IF_PRESENT,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar("zero", dimTime, 0.0)
);

// Create plasma indicator field for global tracking
volScalarField plasmaIndicator
(
    IOobject
    (
        "plasmaIndicator",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar("zero", dimless, 0.0)
);

// Initially zero - will be set when scalars activate at t=3.0s in the main solver
forAll(F, cellI)
{
    plasmaIndicator[cellI] = 0.0;
}

Info<< "Plasma indicator initialized to zero (will be activated at t=2.0s in solver)\n" << endl;

// Create average residence time field
volScalarField tauAvg
(
    IOobject
    (
        "tauAvg",
        runTime.timeName(),
        mesh,
        IOobject::NO_READ,
        IOobject::AUTO_WRITE
    ),
    mesh,
    dimensionedScalar("zero", dimTime, 0.0)
);

Info<< "Global tracking fields created\n" << endl;

// ================== REGION-SPECIFIC TRACKING ==================
Info<< "Creating region-specific tracking fields for 16 force regions\n" << endl;

const label nRegions = 16;
List<word> regionNames(nRegions);
List<scalar> regionXmin(nRegions);
List<scalar> regionXmax(nRegions);
List<scalar> regionYmin(nRegions);
List<scalar> regionYmax(nRegions);

label regionID = 0;

// Bottom pairs
for (label i = 0; i < nPairsBottom; i++)
{
    scalar xc = xCenter0Bot + i*pairPitchBottom;
    
    // Left region
    regionNames[regionID] = "Bot_P" + Foam::name(i+1) + "_L";
    regionXmin[regionID] = xc - halfLRcenter - halfLen;
    regionXmax[regionID] = xc - halfLRcenter + halfLen;
    regionYmin[regionID] = 0.0;
    regionYmax[regionID] = areaHeight;
    regionID++;
    
    // Right region
    regionNames[regionID] = "Bot_P" + Foam::name(i+1) + "_R";
    regionXmin[regionID] = xc + halfLRcenter - halfLen;
    regionXmax[regionID] = xc + halfLRcenter + halfLen;
    regionYmin[regionID] = 0.0;
    regionYmax[regionID] = areaHeight;
    regionID++;
}

// Top pairs
for (label i = 0; i < nPairsTop; i++)
{
    scalar xc = xCenter0Top + i*pairPitchTop;
    
    // Left region
    regionNames[regionID] = "Top_P" + Foam::name(i+1) + "_L";
    regionXmin[regionID] = xc - halfLRcenter - halfLen;
    regionXmax[regionID] = xc - halfLRcenter + halfLen;
    regionYmin[regionID] = Ly - areaHeight;
    regionYmax[regionID] = Ly;
    regionID++;
    
    // Right region
    regionNames[regionID] = "Top_P" + Foam::name(i+1) + "_R";
    regionXmin[regionID] = xc + halfLRcenter - halfLen;
    regionXmax[regionID] = xc + halfLRcenter + halfLen;
    regionYmin[regionID] = Ly - areaHeight;
    regionYmax[regionID] = Ly;
    regionID++;
}

// Create fields for each region
PtrList<volScalarField> c_regions(nRegions);
PtrList<volScalarField> tau_regions(nRegions);
PtrList<volScalarField> Sc_regions(nRegions);

for (label r = 0; r < nRegions; r++)
{
    Info<< "Creating fields for region: " << regionNames[r] << endl;
    
    c_regions.set
    (
        r,
        new volScalarField
        (
            IOobject
            (
                "c_" + regionNames[r],
                runTime.timeName(),
                mesh,
                IOobject::READ_IF_PRESENT,
                IOobject::AUTO_WRITE
            ),
            mesh,
            dimensionedScalar("zero", dimless, 0.0)
        )
    );
    
    tau_regions.set
    (
        r,
        new volScalarField
        (
            IOobject
            (
                "tau_" + regionNames[r],
                runTime.timeName(),
                mesh,
                IOobject::READ_IF_PRESENT,
                IOobject::AUTO_WRITE
            ),
            mesh,
            dimensionedScalar("zero", dimTime, 0.0)
        )
    );
    
    Sc_regions.set
    (
        r,
        new volScalarField
        (
            IOobject
            (
                "Sc_" + regionNames[r],
                runTime.timeName(),
                mesh,
                IOobject::NO_READ,
                IOobject::NO_WRITE
            ),
            mesh,
            dimensionedScalar("zero", Sc_mag.dimensions(), 0.0)
        )
    );
}

#include "createPhi.H"

label pRefCell = 0;
scalar pRefValue = 0.0;
setRefCell(p, mesh.solution().dict().subDict("PISO"), pRefCell, pRefValue);
mesh.schemes().setFluxRequired(p.name());
