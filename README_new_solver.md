# OpenFOAM Plasma Reactor Case: 241125_saas_3_1 (New Solver)

## Overview
This is an advanced OpenFOAM case simulating electrohydrodynamic (EHD) flow in a Surface Dielectric Barrier Discharge (SDBD) plasma reactor with comprehensive tracking capabilities. The custom solver includes time-delayed force activation, passive scalar transport with region-specific tracking, and residence time analysis across 16 individual plasma regions.

## Case Description
- **Solver**: Advanced `icoFoam_basti` (custom incompressible solver with passive scalars)
- **Physics**: Laminar flow with EHD forces, passive scalar transport, and residence time tracking
- **Geometry**: 2D rectangular reactor (50mm × 15mm)
- **Force Configuration**: 8 electrode pairs (4 top + 4 bottom) = 16 force regions total
- **OpenFOAM Version**: v10
- **Key Innovation**: Time-delayed activation (forces and scalars start at t=2.0s)

## Advanced Features

### 1. Time-Delayed Activation
- **Flow development phase**: t = 0 to 2.0s (pure fluid dynamics, no forces)
- **Force activation**: t = 2.0s (EHD forces turn on)
- **Scalar injection**: t = 2.0s (passive scalar tracking begins)
- This allows flow to reach quasi-steady state before plasma effects activate

### 2. Region-Specific Tracking (16 Regions)
Each of the 16 force regions has independent tracking:
- **Bottom pairs**: Bot_P1_L, Bot_P1_R, Bot_P2_L, Bot_P2_R, ... Bot_P4_R (8 regions)
- **Top pairs**: Top_P1_L, Top_P1_R, Top_P2_L, Top_P2_R, ... Top_P4_R (8 regions)

For each region, the solver tracks:
- `c_[region]`: Passive scalar concentration (treatment indicator)
- `tau_[region]`: Local residence time in that specific region
- `Sc_[region]`: Scalar source term for that region

### 3. Global Tracking Fields
- **c**: Global passive scalar field (cumulative treatment)
- **tau**: Global residence time field
- **tauAvg**: Time-averaged residence time
- **plasmaIndicator**: Binary field marking active plasma regions
- **Sc**: Global scalar source term

### 4. Adaptive Mesh Refinement
The mesh generation script (`generateMesh.sh`) implements:
- Base mesh generation with blockMesh
- Two-level refinement near boundaries:
  - First level: 4mm boundary regions
  - Second level: 2mm boundary regions (finest)
- Cell splitting for high resolution in plasma zones

## Solver Physics

### Momentum Equation
```
∂U/∂t + ∇·(UU) = -∇p/ρ + ν∇²U + F(t)
```
where F(t) = 0 for t < 2.0s, F(t) = F_plasma for t ≥ 2.0s

### Passive Scalar Transport
```
∂c/∂t + ∇·(Uc) = Dc∇²c + Sc(t)
```
where:
- `Dc`: Scalar diffusion coefficient [m²/s]
- `Sc(t)`: Source term (active only in plasma regions for t ≥ 2.0s)

### Residence Time Evolution
```
∂τ/∂t + U·∇τ = 1 + Dτ∇²τ
```
Tracks how long fluid parcels have been in plasma regions

## Force Field Configuration

### Key Parameters (in createFields.H)
```cpp
FxMag = 2e3;              // X-direction force magnitude [N/m³]
FyMag = 2e3;              // Y-direction force magnitude [N/m³]
Ly = 15e-3;               // Reactor height [m]
nPairsTop = 4;            // Number of electrode pairs on top
nPairsBottom = 4;         // Number of electrode pairs on bottom
pairWidth = 10e-3;        // Total width of one electrode pair [m]
pairGap = 0.2e-3;         // Gap within each pair [m]
areaHeight = 0.4e-3;      // Band thickness from boundary [m]
pairPitchTop = 10e-3;     // Spacing between pairs (top) [m]
pairPitchBottom = 10e-3;  // Spacing between pairs (bottom) [m]
```

### Transport Properties (in constant/transportProperties)
```cpp
Dc       1e-9;           // Scalar diffusion coefficient [m²/s]
Sc_mag   1.0;            // Scalar source magnitude [1/s]
```

## Directory Structure
```
241125_saas_3_1/
├── 0/                              # Initial conditions
│   ├── U, p, F                    # Flow fields
│   ├── c, tau, tauAvg             # Global tracking fields
│   ├── c_Bot_P1_L, tau_Bot_P1_L   # Region-specific fields (×16)
│   └── ...
├── constant/                       # Physical properties and mesh
│   ├── polyMesh/                  # Refined mesh
│   ├── physicalProperties         # Kinematic viscosity
│   └── transportProperties        # Scalar diffusion parameters
├── system/                         # Solver configuration
│   ├── controlDict                # Time control (adaptive stepping)
│   ├── fvSchemes                  # Discretization schemes
│   ├── fvSolution                 # Linear solvers
│   ├── topoSetDict               # Cell set definitions for refinement
│   ├── refineMeshDict            # Mesh refinement parameters
│   └── decomposeParDict          # Parallel decomposition
├── dynamicCode/                    # Runtime-compiled code
├── Make/                          # Compilation files
├── icoFoam_basti.C               # Advanced solver source
├── createFields.H                # Field initialization with regions
├── createRegionFields.sh         # Script to generate region field files
├── generateMesh.sh               # Automated mesh generation & refinement
└── log.241125_saas_3_1           # Simulation log
```

## Usage

### 1. Mesh Generation
Run the automated mesh generation script:
```bash
./generateMesh.sh
```
This will:
- Generate base mesh with blockMesh
- Create cell sets for refinement zones
- Apply two levels of refinement
- Run mesh quality checks

### 2. Create Region Field Files
Generate initial condition files for all 16 regions:
```bash
./createRegionFields.sh
```
This creates 32 files in the `0/` directory (c_* and tau_* for each region).

### 3. Compile the Solver
```bash
cd Make/
wmake
cd ..
```

### 4. Run the Simulation

**Serial execution:**
```bash
./icoFoam_basti > log.simulation 2>&1
```

**Parallel execution:**
```bash
# Decompose the case
decomposePar

# Run in parallel (adjust -np based on cores)
mpirun -np 16 ./icoFoam_basti -parallel > log.simulation 2>&1

# Reconstruct the fields
reconstructPar
```

### 5. Post-Processing

**ParaView visualization:**
```bash
paraFoam
# or
touch a.foam
# Open a.foam in ParaView
```

**Important fields to visualize:**
- `U`: Velocity field (magnitude and vectors)
- `F`: Force field (active after t=2.0s)
- `c`: Global scalar concentration
- `tau`: Global residence time
- `c_Bot_P1_L`, `c_Top_P1_R`, etc.: Region-specific concentrations
- `plasmaIndicator`: Shows active plasma regions

## Simulation Timeline

### Phase 1: Flow Development (t = 0 → 2.0s)
- Forces F = 0 (inactive)
- Scalars not injected
- Pure hydrodynamic flow development
- Allows flow field to stabilize

### Phase 2: Plasma Treatment (t ≥ 2.0s)
- Forces activate (F ≠ 0)
- Scalar injection begins in plasma regions
- Residence time tracking starts
- Region-specific analysis enabled

## Key Output Fields and Their Meaning

### Global Fields
| Field | Description | Units | Physical Meaning |
|-------|-------------|-------|------------------|
| `U` | Velocity | m/s | Flow field |
| `p` | Pressure | Pa | Pressure field |
| `F` | Body force | N/m³ | EHD force (active t≥2.0s) |
| `c` | Global scalar | - | Cumulative treatment indicator |
| `tau` | Residence time | s | Time spent in any plasma region |
| `tauAvg` | Avg residence time | s | Time-averaged tau |
| `plasmaIndicator` | Plasma marker | - | 1 in plasma, 0 elsewhere |

### Region-Specific Fields (×16)
| Field Pattern | Description | Purpose |
|---------------|-------------|---------|
| `c_Bot_P1_L` | Scalar from bottom-left pair 1 | Track treatment from specific region |
| `tau_Bot_P1_L` | Residence time in that region | Local dwell time analysis |

## Adaptive Time Stepping
Controlled in `system/controlDict`:
```cpp
adjustTimeStep  yes;
maxCo          0.08;     // Maximum Courant number
maxDeltaT      1e-3;     // Maximum time step [s]
```

## Analysis Capabilities

### Flow Analysis
- Velocity profiles and streamlines
- Vorticity and circulation patterns
- Flow rate through reactor
- Pressure drop analysis

### Scalar Transport Analysis
- Global treatment efficiency (c field)
- Region-specific contribution analysis
- Diffusion vs. convection balance
- Downstream mixing patterns

### Residence Time Analysis
- Global residence time distribution
- Per-region dwell time statistics
- Average residence time evolution
- Identification of dead zones vs. high-residence regions

### Multi-Region KPI Extraction
- Treatment efficiency per region
- Flow distribution across 16 regions
- Optimization: which regions contribute most
- Parametric studies: varying individual region properties

## Modifying the Configuration

### Changing Force Parameters
Edit `createFields.H`:
```cpp
scalar FxMag = 2e3;        // Adjust force magnitude
scalar FyMag = 2e3;
scalar nPairsTop = 4;      // Change number of pairs
scalar pairWidth = 10e-3;  // Adjust geometry
```
Recompile after changes: `wmake`

### Changing Activation Time
Edit `icoFoam_basti.C`, find the condition:
```cpp
if (runTime.time().value() >= 2.0)  // Change 2.0 to desired time
```

### Changing Scalar Properties
Edit `constant/transportProperties`:
```cpp
Dc       1e-9;    // Diffusion coefficient
Sc_mag   1.0;     // Source strength
```

## Mesh Refinement Zones
Defined in `system/topoSetDict`:
- **c0**: 4mm boundary regions (first refinement level)
- **c4**: 2mm boundary regions (second refinement level, finest)

Adjust these zones for different refinement strategies.

## Important Simulation Notes

1. **Memory Requirements**: With region tracking, expect ~2-4GB RAM per core for parallel runs

2. **Storage**: Each time directory stores 40+ fields (global + 32 region fields), plan accordingly

3. **Activation Delay**: Always verify forces and scalars activate at t=2.0s by checking field values

4. **Region Boundaries**: Use `plasmaIndicator` field to visualize exact region locations

5. **Convergence**: Monitor both flow residuals and scalar field evolution

## Performance Optimization

### Parallel Scaling
- Recommended: 16 cores (matches region count)
- Good load balancing with hierarchical decomposition
- Each core can "own" one region conceptually

### Time Step Selection
- Initial: Δt ~ 1e-5 s (flow development)
- After stabilization: Δt ~ 1e-4 s
- Adaptive timestepping handles transitions automatically

### Output Frequency
- Save every 0.01-0.02s for steady regions
- Save more frequently (0.001s) during transients
- Balance storage vs. temporal resolution

## Troubleshooting

### Problem: Forces not activating
- Check `icoFoam_basti.C` for activation condition
- Verify t ≥ 2.0s in simulation
- Check `plasmaIndicator` field

### Problem: Region fields all zero
- Ensure `createRegionFields.sh` was run
- Check boundary conditions in `0/` directory
- Verify source terms Sc_regions are computed

### Problem: Large memory usage
- Reduce output fields in controlDict
- Increase writeInterval
- Consider reducing number of regions tracked

## References
- OpenFOAM v10: https://openfoam.org
- Passive scalar transport: OpenFOAM User Guide Ch. 7
- Residence time tracking: Custom implementation

## Version History
- **v2.0** (241125): Advanced solver with 16-region tracking, time-delayed activation
- **v1.5** (071125): Added passive scalar transport
- **v1.0** (040825): Original solver with basic force field

## Author
Sofian Sakr  
November 2024

## Citation
If you use this solver in your research, please cite:
```
Sakr, S. (2024). Advanced EHD Plasma Reactor Simulation with 
Region-Specific Tracking. OpenFOAM v10 Custom Solver.
```
