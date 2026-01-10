#!/bin/bash
#------------------------------------------------------------------------------
# Script to generate and refine the mesh with cell splitting
#------------------------------------------------------------------------------

echo "Starting mesh generation and refinement process..."

# Clean previous mesh if exists
echo "Cleaning previous mesh..."
rm -rf constant/polyMesh

# Step 1: Generate base mesh using blockMesh
echo "Step 1: Generating base mesh with blockMesh..."
blockMesh
checkMesh

# Step 2: Create cell sets for refinement regions
echo "Step 2: Creating cell sets for refinement regions..."
topoSet

# Step 3: First level of refinement (4 mm regions)
echo "Step 3: Applying first level refinement to 4mm boundary regions..."
cp system/refineMeshDict system/refineMeshDict.c0
refineMesh -dict system/refineMeshDict.c0 -overwrite
checkMesh

# Step 4: Update cell sets for second level refinement
echo "Step 4: Updating cell sets for second level refinement..."
# Rename the refined mesh cellSet
mv constant/polyMesh/sets/c0 constant/polyMesh/sets/c0_refined1

# Re-run topoSet to create c4 set for second level refinement
topoSet -dict system/topoSetDict

# Step 5: Second level of refinement (2 mm regions) 
echo "Step 5: Applying second level refinement to 2mm boundary regions..."
cp system/refineMeshDict system/refineMeshDict.c4
sed -i 's/set c0/set c4/g' system/refineMeshDict.c4
refineMesh -dict system/refineMeshDict.c4 -overwrite
checkMesh

# Step 6: Final mesh check
echo "Step 6: Final mesh quality check..."
checkMesh -allTopology -allGeometry

# Display mesh statistics
echo ""
echo "========================================="
echo "Mesh generation completed successfully!"
echo "========================================="
echo ""
echo "Mesh statistics:"
checkMesh | grep -E "cells:|faces:|points:|boundary patches:" 

echo ""
echo "You can visualize the mesh using:"
echo "  paraFoam"
echo "or"
echo "  foamToVTK && paraview"
