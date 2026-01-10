#!/bin/bash
# Script: createRegionFields.sh
# Run this in your case directory

cd 0

# Define regions
regions=(
    "Bot_P1_L" "Bot_P1_R" "Bot_P2_L" "Bot_P2_R"
    "Bot_P3_L" "Bot_P3_R" "Bot_P4_L" "Bot_P4_R"
    "Top_P1_L" "Top_P1_R" "Top_P2_L" "Top_P2_R"
    "Top_P3_L" "Top_P3_R" "Top_P4_L" "Top_P4_R"
)

# Create concentration fields for each region
for region in "${regions[@]}"; do
    cat > "c_${region}" << EOF
/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\\\    /   O peration     | Website:  https://openfoam.org
    \\\\  /    A nd           | Version:  10
     \\\\/     M anipulation  |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    format      ascii;
    class       volScalarField;
    location    "0";
    object      c_${region};
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    In
    {
        type            fixedValue;
        value           uniform 0;
    }
    
    Out
    {
        type            zeroGradient;
    }
    
    Top
    {
        type            zeroGradient;
    }
    
    Bottom
    {
        type            zeroGradient;
    }
    
    DefaultFaces
    {
        type            empty;
    }
}

// ************************************************************************* //
EOF

    # Create tau fields for each region
    cat > "tau_${region}" << EOF
/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\\\    /   O peration     | Website:  https://openfoam.org
    \\\\  /    A nd           | Version:  10
     \\\\/     M anipulation  |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    format      ascii;
    class       volScalarField;
    location    "0";
    object      tau_${region};
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 1 0 0 0 0];  // Time

internalField   uniform 0;

boundaryField
{
    In
    {
        type            fixedValue;
        value           uniform 0;
    }
    
    Out
    {
        type            zeroGradient;
    }
    
    Top
    {
        type            zeroGradient;
    }
    
    Bottom
    {
        type            zeroGradient;
    }
    
    DefaultFaces
    {
        type            empty;
    }
}

// ************************************************************************* //
EOF

done

echo "Created 32 region-specific field files"
ls -la *_Bot_* *_Top_* | wc -l
