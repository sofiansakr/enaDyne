# Quick Start Guide - Advanced OpenFOAM Plasma Reactor Solver

## What's New in This Solver?

### Compared to Previous Version (040825_1_1)
| Feature | Old Solver | New Solver (This) |
|---------|-----------|-------------------|
| Force activation | Immediate (t=0) | Delayed (t=2.0s) |
| Region tracking | None | 16 regions |
| Passive scalars | No | Yes (global + per region) |
| Residence time | No | Yes (global + per region) |
| Force magnitude | 1e5 N/m³ | 2e3 N/m³ |
| Complexity | Basic | Advanced |
| Fields per timestep | 4-5 | 40+ |
| Memory usage | Low | High |
| Analysis depth | Basic | Comprehensive |

## 5-Minute Setup

### 1. Navigate to Case Directory
```bash
cd ~/SAAS_Ubun/071125_saas_3/241125_saas_3_1
```

### 2. Copy Documentation Files
```bash
# Copy the documentation files you created to the case directory:
cp README_new_solver.md README.md
cp PACKAGES_new_solver.txt PACKAGES.txt
cp requirements_new_solver.txt requirements.txt
cp .gitignore_new_solver .gitignore
```

### 3. Generate Mesh (First Time Only)
```bash
# This takes 5-10 minutes
./generateMesh.sh
```

### 4. Create Region Fields (First Time Only)
```bash
# Creates initial condition files for 16 regions
./createRegionFields.sh
```

### 5. Compile Solver (First Time or After Changes)
```bash
cd Make/
wmake
cd ..
```

### 6. Run Simulation

**Option A: Serial (for testing)**
```bash
./icoFoam_basti | tee log.run
```

**Option B: Parallel (recommended)**
```bash
# Decompose
decomposePar

# Run on 16 cores
mpirun -np 16 ./icoFoam_basti -parallel | tee log.run

# Reconstruct
reconstructPar
```

### 7. Visualize Results
```bash
# Option 1: ParaView
paraFoam

# Option 2: Create .foam file and open in ParaView
touch case.foam
# Then open case.foam in ParaView GUI
```

## Understanding the Simulation Timeline

```
t = 0.0s ──────────────► t = 2.0s ──────────────► t = 5.0s (end)
│                        │                        │
│ Flow Development       │ Plasma Treatment       │
│ - No forces            │ - Forces ON            │
│ - No scalars           │ - Scalars injected     │
│ - Pure fluid dynamics  │ - Full tracking        │
│                        │                        │
└────────────────────────┴────────────────────────┘
```

## Key Files to Check

### Before Running
- [ ] `system/controlDict` - Check endTime (default: 5.0s)
- [ ] `constant/physicalProperties` - Verify viscosity
- [ ] `constant/transportProperties` - Check Dc and Sc_mag
- [ ] `createFields.H` - Verify force parameters

### After Running
- [ ] `log.run` - Check for errors and convergence
- [ ] `postProcessing/` - Automated analysis results
- [ ] Time directories (1, 2, 3, 4, 5) - Flow fields
- [ ] `constant/polyMesh/` - Mesh statistics

## Important Fields to Visualize

### Essential Fields
1. **U** - Velocity field (check flow patterns)
2. **p** - Pressure field
3. **F** - Force field (should be zero before t=2.0s)
4. **c** - Global scalar concentration (treatment indicator)

### Advanced Analysis Fields
5. **tau** - Global residence time
6. **plasmaIndicator** - Shows active plasma regions
7. **c_Bot_P1_L** (example) - Region-specific concentration
8. **tau_Bot_P1_L** (example) - Region-specific residence time

### ParaView Tips
- Use "Glyph" filter for velocity vectors
- Use "Stream Tracer" for streamlines
- Use "Contour" filter for iso-surfaces of c field
- Color by magnitude for scalar fields

## Common Workflows

### Workflow 1: Quick Test Run
```bash
# 1. Generate mesh
./generateMesh.sh

# 2. Create fields
./createRegionFields.sh

# 3. Test compile
cd Make && wmake && cd ..

# 4. Short test run (0.1s)
# Edit system/controlDict: endTime 0.1;
./icoFoam_basti

# 5. Check results
paraFoam
```

### Workflow 2: Production Run
```bash
# 1. Setup (if not done)
./generateMesh.sh
./createRegionFields.sh
cd Make && wmake && cd ..

# 2. Run full simulation
decomposePar
mpirun -np 16 ./icoFoam_basti -parallel > log.full 2>&1 &

# 3. Monitor progress
tail -f log.full

# 4. After completion
reconstructPar
paraFoam
```

### Workflow 3: Parametric Study
```bash
# 1. Edit parameters in createFields.H
nano createFields.H
# Change FxMag, FyMag, nPairs, etc.

# 2. Recompile
cd Make && wmake && cd ..

# 3. Clean old results
rm -rf [1-9]* processor* log.*

# 4. Run new case
mpirun -np 16 ./icoFoam_basti -parallel > log.param_study 2>&1

# 5. Analyze and compare
paraFoam
```

## Troubleshooting Quick Fixes

### Problem: "Command not found: ./icoFoam_basti"
```bash
# Solution: Compile the solver
cd Make
wmake
cd ..
```

### Problem: "Cannot find file 0/c_Bot_P1_L"
```bash
# Solution: Create region fields
./createRegionFields.sh
```

### Problem: Mesh errors
```bash
# Solution: Regenerate mesh
rm -rf constant/polyMesh
./generateMesh.sh
```

### Problem: Out of memory during run
```bash
# Solution 1: Reduce output frequency
# Edit system/controlDict: increase writeInterval

# Solution 2: Run on machine with more RAM
# or reduce number of processors

# Solution 3: Use swap space
sudo fallocate -l 32G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Problem: Simulation too slow
```bash
# Solution 1: Increase time step (if stable)
# Edit system/controlDict: maxDeltaT 1e-3;

# Solution 2: Use more processors
mpirun -np 32 ./icoFoam_basti -parallel

# Solution 3: Coarsen mesh in non-critical regions
```

## Git Repository Setup

```bash
# Initialize git
git init

# Add remote
git remote add origin http://10.12.5.20:4000/SAAS/new_solver

# Cache credentials (8 hours)
git config --global credential.helper 'cache --timeout=28800'

# Configure user
git config user.name "Sofian Sakr"
git config user.email "your.email@example.com"

# Add files (respects .gitignore)
git add .

# Check what will be committed
git status

# Commit
git commit -m "Initial commit: Advanced solver with 16-region tracking"

# Push (create repository on server first!)
git push -u origin master
```

## Analysis Checklist

After simulation completes:

- [ ] Verify flow development (0-2s) looks reasonable
- [ ] Check force activation at t=2.0s (F field should change)
- [ ] Examine scalar injection (c field should start growing)
- [ ] Compare region contributions (which regions treat most?)
- [ ] Analyze residence time distribution
- [ ] Check for dead zones or recirculation
- [ ] Export KPIs for reporting
- [ ] Create visualization animations

## Next Steps

1. **Learn the physics**: Read README.md sections on equations
2. **Explore parameters**: Try different FxMag, FyMag values
3. **Post-process**: Use Python notebooks for detailed analysis
4. **Optimize**: Use insights to improve reactor design
5. **Document**: Record parameter studies and results

## Getting Help

- Check README.md for detailed documentation
- Review PACKAGES.txt for installation issues
- Examine log files for error messages
- Use `checkMesh` for mesh problems
- Monitor memory usage with `htop` or `top`

## Pro Tips

1. **Save disk space**: Increase `writeInterval` to 0.05 or 0.1
2. **Speed up I/O**: Write to local SSD, not network drive
3. **Parallel efficiency**: Use 16 cores to match region count
4. **Memory management**: Monitor with `free -h` during runs
5. **Backup**: Archive completed cases to external storage

---

**Ready to run?** Follow the 5-Minute Setup above!

**Need more details?** Check the full README.md

**Having issues?** See the Troubleshooting section
