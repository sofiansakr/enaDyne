# trace generated using paraview version 6.0.1
#import paraview
#paraview.compatibility.major = 6
#paraview.compatibility.minor = 0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
afoam = GetActiveSource()

# Properties modified on afoam
afoam.MeshRegions = ['patch/Out']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
afoamDisplay = Show(afoam, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')
pTF2D.Set(
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    Boxes=[],
    ScalarRangeInitialized=0,
    Range=[0.0, 1.0, 0.0, 1.0],
    OutputDimensions=[10, 10],
)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')
pLUT.Set(
    InterpretValuesAsCategories=0,
    AnnotationsInitialized=0,
    ShowCategoricalColorsinDataRangeOnly=0,
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    RescaleOnVisibilityChange=0,
    TransferFunction2D=pTF2D,
    RGBPoints=GenerateRGBPoints(
        range_min=617300.0,
        range_max=617428.0,
    ),
    UseLogScale=0,
    UseOpacityControlPointsFreehandDrawing=0,
    ShowDataHistogram=0,
    AutomaticDataHistogramComputation=0,
    DataHistogramNumberOfBins=10,
    ColorSpace='Lab',
    UseBelowRangeColor=0,
    BelowRangeColor=[0.0, 0.0, 0.0],
    UseAboveRangeColor=0,
    AboveRangeColor=[0.5, 0.5, 0.5],
    NanColor=[0.0, 1.0, 0.0],
    NanOpacity=1.0,
    Discretize=1,
    NumberOfTableValues=256,
    ScalarRangeInitialized=1.0,
    HSVWrap=0,
    VectorComponent=0,
    VectorMode='Magnitude',
    AllowDuplicateScalars=1,
    Annotations=[],
    ActiveAnnotatedValues=[],
    IndexedColors=[],
    IndexedOpacities=[],
    EnableOpacityMapping=0,
)

# trace defaults for the display properties.
afoamDisplay.Set(
    Selection=None,
    Representation='Surface',
    ColorArrayName=['CELLS', 'p'],
    LookupTable=pLUT,
    MapScalars=1,
    MultiComponentsMapping=0,
    InterpolateScalarsBeforeMapping=1,
    UseNanColorForMissingArrays=0,
    Opacity=1.0,
    PointSize=2.0,
    LineWidth=1.0,
    RenderLinesAsTubes=0,
    RenderPointsAsSpheres=0,
    DisableLighting=0,
    Diffuse=1.0,
    Interpolation='Gouraud',
    Specular=0.0,
    SpecularColor=[1.0, 1.0, 1.0],
    SpecularPower=100.0,
    Luminosity=0.0,
    Ambient=0.0,
    Roughness=0.3,
    Metallic=0.0,
    EdgeTint=[1.0, 1.0, 1.0],
    Anisotropy=0.0,
    AnisotropyRotation=0.0,
    BaseIOR=1.5,
    CoatStrength=0.0,
    CoatIOR=2.0,
    CoatRoughness=0.0,
    CoatColor=[1.0, 1.0, 1.0],
    SelectNormalArray='None',
    SelectTangentArray='None',
    ComputePointNormals=0,
    Splitting=1,
    FeatureAngle=30.0,
    SelectTCoordArray='None',
    Texture=None,
    RepeatTextures=1,
    InterpolateTextures=0,
    SeamlessU=0,
    SeamlessV=0,
    UseMipmapTextures=0,
    ShowTexturesOnBackface=1,
    BaseColorTexture=None,
    NormalTexture=None,
    NormalScale=1.0,
    CoatNormalTexture=None,
    CoatNormalScale=1.0,
    MaterialTexture=None,
    OcclusionStrength=1.0,
    AnisotropyTexture=None,
    EmissiveTexture=None,
    EmissiveFactor=[1.0, 1.0, 1.0],
    TextureTransform='Transform2',
    EdgeOpacity=1.0,
    BackfaceRepresentation='Follow Frontface',
    BackfaceAmbientColor=[1.0, 1.0, 1.0],
    BackfaceOpacity=1.0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    Origin=[0.0, 0.0, 0.0],
    CoordinateShiftScaleMethod='Always Auto Shift Scale',
    CoordinateSystem='Navigable',
    Pickable=1,
    Triangulate=0,
    UseShaderReplacements=0,
    ShaderReplacements='',
    NonlinearSubdivisionLevel=1,
    MatchBoundariesIgnoringCellOrder=0,
    UseDataPartitions=0,
    OSPRayUseScaleArray='All Approximate',
    OSPRayScaleArray='',
    OSPRayScaleFunction='Piecewise Function',
    OSPRayMaterial='None',
    Assembly='Hierarchy',
    SelectedBlockSelectors=[''],
    BlockSelectors=['/'],
    BlockColors=[],
    BlockColorArrayNames=[],
    BlockLookupTables=[],
    BlockUseSeparateColorMaps=[],
    BlockMapScalars=[],
    BlockInterpolateScalarsBeforeMappings=[],
    BlockOpacities=[],
    BlockMapScalarsGUI=1,
    BlockInterpolateScalarsBeforeMappingsGUI=1,
    BlockOpacitiesGUI=1.0,
    Orient=0,
    OrientationMode='Direction',
    SelectOrientationVectors='U',
    Scaling=0,
    ScaleMode='No Data Scaling Off',
    ScaleFactor=0.0014999999664723875,
    SelectScaleArray='p',
    GlyphType='Arrow',
    UseGlyphTable=0,
    GlyphTableIndexArray='p',
    UseCompositeGlyphTable=0,
    UseGlyphCullingAndLOD=0,
    LODValues=[],
    ColorByLODIndex=0,
    GaussianRadius=7.499999832361936e-05,
    ShaderPreset='Sphere',
    CustomTriangleScale=3,
    Emissive=0,
    ScaleByArray=0,
    SetScaleArray=[None, ''],
    ScaleArrayComponent=0,
    UseScaleFunction=1,
    ScaleTransferFunction='Piecewise Function',
    OpacityByArray=0,
    OpacityArray=[None, ''],
    OpacityArrayComponent=0,
    OpacityTransferFunction='Piecewise Function',
    DataAxesGrid='Grid Axes Representation',
    SelectionCellLabelBold=0,
    SelectionCellLabelColor=[0.0, 1.0, 0.0],
    SelectionCellLabelFontFamily='Arial',
    SelectionCellLabelFontFile='',
    SelectionCellLabelFontSize=18,
    SelectionCellLabelItalic=0,
    SelectionCellLabelJustification='Left',
    SelectionCellLabelOpacity=1.0,
    SelectionCellLabelShadow=0,
    SelectionPointLabelBold=0,
    SelectionPointLabelColor=[1.0, 1.0, 0.0],
    SelectionPointLabelFontFamily='Arial',
    SelectionPointLabelFontFile='',
    SelectionPointLabelFontSize=18,
    SelectionPointLabelItalic=0,
    SelectionPointLabelJustification='Left',
    SelectionPointLabelOpacity=1.0,
    SelectionPointLabelShadow=0,
    PolarAxes='Polar Axes Representation',
    SelectInputVectors=[None, ''],
    NumberOfSteps=40,
    StepSize=0.25,
    NormalizeVectors=1,
    EnhancedLIC=1,
    ColorMode='Blend',
    LICIntensity=0.8,
    MapModeBias=0.0,
    EnhanceContrast='Off',
    LowLICContrastEnhancementFactor=0.0,
    HighLICContrastEnhancementFactor=0.0,
    LowColorContrastEnhancementFactor=0.0,
    HighColorContrastEnhancementFactor=0.0,
    AntiAlias=0,
    MaskOnSurface=1,
    MaskThreshold=0.0,
    MaskIntensity=0.0,
    MaskColor=[0.5, 0.5, 0.5],
    GenerateNoiseTexture=0,
    NoiseType='Gaussian',
    NoiseTextureSize=128,
    NoiseGrainSize=2,
    MinNoiseValue=0.0,
    MaxNoiseValue=0.8,
    NumberOfNoiseLevels=1024,
    ImpulseNoiseProbability=1.0,
    ImpulseNoiseBackgroundValue=0.0,
    NoiseGeneratorSeed=1,
    CompositeStrategy='AUTO',
    UseLICForLOD=0,
    WriteLog='',
    CustomShader=""" // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
""",
)

# init the 'Transform2' selected for 'TextureTransform'
afoamDisplay.TextureTransform.Set(
    Translate=[0.0, 0.0, 0.0],
    Rotate=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
afoamDisplay.OSPRayScaleFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Arrow' selected for 'GlyphType'
afoamDisplay.GlyphType.Set(
    TipResolution=6,
    TipRadius=0.1,
    TipLength=0.35,
    ShaftResolution=6,
    ShaftRadius=0.03,
    Invert=0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
afoamDisplay.ScaleTransferFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
afoamDisplay.OpacityTransferFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
afoamDisplay.DataAxesGrid.Set(
    XTitle='X Axis',
    YTitle='Y Axis',
    ZTitle='Z Axis',
    XTitleFontFamily='Arial',
    XTitleFontFile='',
    XTitleBold=0,
    XTitleItalic=0,
    XTitleFontSize=12,
    XTitleShadow=0,
    XTitleOpacity=1.0,
    YTitleFontFamily='Arial',
    YTitleFontFile='',
    YTitleBold=0,
    YTitleItalic=0,
    YTitleFontSize=12,
    YTitleShadow=0,
    YTitleOpacity=1.0,
    ZTitleFontFamily='Arial',
    ZTitleFontFile='',
    ZTitleBold=0,
    ZTitleItalic=0,
    ZTitleFontSize=12,
    ZTitleShadow=0,
    ZTitleOpacity=1.0,
    FacesToRender=63,
    CullBackface=0,
    CullFrontface=1,
    ShowGrid=0,
    ShowEdges=1,
    ShowTicks=1,
    LabelUniqueEdgesOnly=1,
    AxesToLabel=63,
    XLabelFontFamily='Arial',
    XLabelFontFile='',
    XLabelBold=0,
    XLabelItalic=0,
    XLabelFontSize=12,
    XLabelShadow=0,
    XLabelOpacity=1.0,
    YLabelFontFamily='Arial',
    YLabelFontFile='',
    YLabelBold=0,
    YLabelItalic=0,
    YLabelFontSize=12,
    YLabelShadow=0,
    YLabelOpacity=1.0,
    ZLabelFontFamily='Arial',
    ZLabelFontFile='',
    ZLabelBold=0,
    ZLabelItalic=0,
    ZLabelFontSize=12,
    ZLabelShadow=0,
    ZLabelOpacity=1.0,
    XAxisNotation='Mixed',
    XAxisPrecision=2,
    XAxisUseCustomLabels=0,
    XAxisLabels=[],
    YAxisNotation='Mixed',
    YAxisPrecision=2,
    YAxisUseCustomLabels=0,
    YAxisLabels=[],
    ZAxisNotation='Mixed',
    ZAxisPrecision=2,
    ZAxisUseCustomLabels=0,
    ZAxisLabels=[],
    UseCustomBounds=0,
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
)

# init the 'Polar Axes Representation' selected for 'PolarAxes'
afoamDisplay.PolarAxes.Set(
    Visibility=0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    EnableCustomBounds=[0, 0, 0],
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
    EnableCustomRange=0,
    CustomRange=[0.0, 1.0],
    AutoPole=1,
    PolarAxisVisibility=1,
    RadialAxesVisibility=1,
    DrawRadialGridlines=1,
    PolarArcsVisibility=1,
    DrawPolarArcsGridlines=1,
    NumberOfRadialAxes=0,
    DeltaAngleRadialAxes=45.0,
    NumberOfArcs=5,
    DeltaRangeArcs=0.0,
    CustomMinRadius=1,
    MinimumRadius=0.0,
    CustomMaxRadius=0,
    MaximumRadius=1.0,
    CustomAngles=1,
    MinimumAngle=0.0,
    MaximumAngle=90.0,
    RadialAxesOriginToPolarAxis=1,
    PolarArcResolutionPerDegree=0.2,
    Ratio=1.0,
    EnableOverallColor=1,
    OverallColor=[1.0, 1.0, 1.0],
    PolarAxisColor=[1.0, 1.0, 1.0],
    PolarArcsColor=[1.0, 1.0, 1.0],
    LastRadialAxisColor=[1.0, 1.0, 1.0],
    SecondaryPolarArcsColor=[1.0, 1.0, 1.0],
    SecondaryRadialAxesColor=[1.0, 1.0, 1.0],
    PolarAxisTitleVisibility=1,
    PolarAxisTitle='Radial Distance',
    PolarAxisTitleLocation='Bottom',
    PolarTitleOffset=[20.0, 20.0],
    PolarLabelVisibility=1,
    PolarLabelFormat='%-#6.3g',
    PolarLabelExponentLocation='Labels',
    PolarLabelOffset=10.0,
    PolarExponentOffset=5.0,
    RadialLabelVisibility=1,
    RadialLabelFormat='%-#3.1f',
    RadialLabelLocation='Bottom',
    RadialLabelOffset=[20.0, 0.0],
    RadialUnitsVisibility=1,
    ScreenSize=10.0,
    PolarAxisTitleOpacity=1.0,
    PolarAxisTitleFontFamily='Arial',
    PolarAxisTitleFontFile='',
    PolarAxisTitleBold=0,
    PolarAxisTitleItalic=0,
    PolarAxisTitleShadow=0,
    PolarAxisTitleFontSize=12,
    PolarAxisLabelOpacity=1.0,
    PolarAxisLabelFontFamily='Arial',
    PolarAxisLabelFontFile='',
    PolarAxisLabelBold=0,
    PolarAxisLabelItalic=0,
    PolarAxisLabelShadow=0,
    PolarAxisLabelFontSize=12,
    LastRadialAxisTextOpacity=1.0,
    LastRadialAxisTextFontFamily='Arial',
    LastRadialAxisTextFontFile='',
    LastRadialAxisTextBold=0,
    LastRadialAxisTextItalic=0,
    LastRadialAxisTextShadow=0,
    LastRadialAxisTextFontSize=12,
    SecondaryRadialAxesTextOpacity=1.0,
    SecondaryRadialAxesTextFontFamily='Arial',
    SecondaryRadialAxesTextFontFile='',
    SecondaryRadialAxesTextBold=0,
    SecondaryRadialAxesTextItalic=0,
    SecondaryRadialAxesTextShadow=0,
    SecondaryRadialAxesTextFontSize=12,
    EnableDistanceLOD=1,
    DistanceLODThreshold=0.7,
    EnableViewAngleLOD=1,
    ViewAngleLODThreshold=0.7,
    SmallestVisiblePolarAngle=0.5,
    AllTicksVisibility=1,
    ArcTicksOriginToPolarAxis=1,
    TickLocation='Both',
    AxisTickVisibility=1,
    AxisMinorTickVisibility=0,
    AxisTickMatchesPolarAxes=1,
    DeltaRangeMajor=1.0,
    DeltaRangeMinor=0.5,
    ArcTickVisibility=1,
    ArcMinorTickVisibility=0,
    ArcTickMatchesRadialAxes=1,
    DeltaAngleMajor=10.0,
    DeltaAngleMinor=5.0,
    TickRatioRadiusSize=0.02,
    PolarAxisMajorTickSize=0.0,
    PolarAxisTickRatioSize=0.3,
    PolarAxisMajorTickThickness=1.0,
    PolarAxisTickRatioThickness=0.5,
    LastRadialAxisMajorTickSize=0.0,
    LastRadialAxisTickRatioSize=0.3,
    LastRadialAxisMajorTickThickness=1.0,
    LastRadialAxisTickRatioThickness=0.5,
    ArcMajorTickSize=0.0,
    ArcTickRatioSize=0.3,
    ArcMajorTickThickness=1.0,
    ArcTickRatioThickness=0.5,
    Use2DMode=0,
    UseLogAxis=0,
)

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

#changing interaction mode based on data extents
renderView1.Set(
    InteractionMode='2D',
    CameraPosition=[0.10024999962188304, 0.007499999832361937, 0.0005000000237487257],
    CameraFocalPoint=[0.05000000074505806, 0.007499999832361937, 0.0005000000237487257],
    CameraViewUp=[0.0, 0.0, 1.0],
)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
afoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')
pPWF.Set(
    Points=[617300.0, 0.0, 0.5, 0.0, 617428.0, 1.0, 0.5, 0.0],
    AllowDuplicateScalars=1,
    UseLogScale=0,
    ScalarRangeInitialized=1,
)

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=afoam)
cellDatatoPointData1.Set(
    ProcessAllArrays=1,
    CellDataArraytoprocess=['F', 'Sc', 'U', 'c', 'c_Bot_P1_L', 'c_Bot_P1_R', 'c_Bot_P2_L', 'c_Bot_P2_R', 'c_Bot_P3_L', 'c_Bot_P3_R', 'c_Bot_P4_L', 'c_Bot_P4_R', 'c_Top_P1_L', 'c_Top_P1_R', 'c_Top_P2_L', 'c_Top_P2_R', 'c_Top_P3_L', 'c_Top_P3_R', 'c_Top_P4_L', 'c_Top_P4_R', 'p', 'plasmaIndicator', 'tau', 'tauAvg', 'tau_Bot_P1_L', 'tau_Bot_P1_R', 'tau_Bot_P2_L', 'tau_Bot_P2_R', 'tau_Bot_P3_L', 'tau_Bot_P3_R', 'tau_Bot_P4_L', 'tau_Bot_P4_R', 'tau_Top_P1_L', 'tau_Top_P1_R', 'tau_Top_P2_L', 'tau_Top_P2_R', 'tau_Top_P3_L', 'tau_Top_P3_R', 'tau_Top_P4_L', 'tau_Top_P4_R'],
    PassCellData=0,
    PieceInvariant=0,
)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
cellDatatoPointData1Display.Set(
    Selection=None,
    Representation='Surface',
    ColorArrayName=['POINTS', 'p'],
    LookupTable=pLUT,
    MapScalars=1,
    MultiComponentsMapping=0,
    InterpolateScalarsBeforeMapping=1,
    UseNanColorForMissingArrays=0,
    Opacity=1.0,
    PointSize=2.0,
    LineWidth=1.0,
    RenderLinesAsTubes=0,
    RenderPointsAsSpheres=0,
    DisableLighting=0,
    Diffuse=1.0,
    Interpolation='Gouraud',
    Specular=0.0,
    SpecularColor=[1.0, 1.0, 1.0],
    SpecularPower=100.0,
    Luminosity=0.0,
    Ambient=0.0,
    Roughness=0.3,
    Metallic=0.0,
    EdgeTint=[1.0, 1.0, 1.0],
    Anisotropy=0.0,
    AnisotropyRotation=0.0,
    BaseIOR=1.5,
    CoatStrength=0.0,
    CoatIOR=2.0,
    CoatRoughness=0.0,
    CoatColor=[1.0, 1.0, 1.0],
    SelectNormalArray='None',
    SelectTangentArray='None',
    ComputePointNormals=0,
    Splitting=1,
    FeatureAngle=30.0,
    SelectTCoordArray='None',
    Texture=None,
    RepeatTextures=1,
    InterpolateTextures=0,
    SeamlessU=0,
    SeamlessV=0,
    UseMipmapTextures=0,
    ShowTexturesOnBackface=1,
    BaseColorTexture=None,
    NormalTexture=None,
    NormalScale=1.0,
    CoatNormalTexture=None,
    CoatNormalScale=1.0,
    MaterialTexture=None,
    OcclusionStrength=1.0,
    AnisotropyTexture=None,
    EmissiveTexture=None,
    EmissiveFactor=[1.0, 1.0, 1.0],
    TextureTransform='Transform2',
    EdgeOpacity=1.0,
    BackfaceRepresentation='Follow Frontface',
    BackfaceAmbientColor=[1.0, 1.0, 1.0],
    BackfaceOpacity=1.0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    Origin=[0.0, 0.0, 0.0],
    CoordinateShiftScaleMethod='Always Auto Shift Scale',
    CoordinateSystem='Navigable',
    Pickable=1,
    Triangulate=0,
    UseShaderReplacements=0,
    ShaderReplacements='',
    NonlinearSubdivisionLevel=1,
    MatchBoundariesIgnoringCellOrder=0,
    UseDataPartitions=0,
    OSPRayUseScaleArray='All Approximate',
    OSPRayScaleArray='p',
    OSPRayScaleFunction='Piecewise Function',
    OSPRayMaterial='None',
    Assembly='Hierarchy',
    SelectedBlockSelectors=[''],
    BlockSelectors=['/'],
    BlockColors=[],
    BlockColorArrayNames=[],
    BlockLookupTables=[],
    BlockUseSeparateColorMaps=[],
    BlockMapScalars=[],
    BlockInterpolateScalarsBeforeMappings=[],
    BlockOpacities=[],
    BlockMapScalarsGUI=1,
    BlockInterpolateScalarsBeforeMappingsGUI=1,
    BlockOpacitiesGUI=1.0,
    Orient=0,
    OrientationMode='Direction',
    SelectOrientationVectors='U',
    Scaling=0,
    ScaleMode='No Data Scaling Off',
    ScaleFactor=0.0014999999664723875,
    SelectScaleArray='p',
    GlyphType='Arrow',
    UseGlyphTable=0,
    GlyphTableIndexArray='p',
    UseCompositeGlyphTable=0,
    UseGlyphCullingAndLOD=0,
    LODValues=[],
    ColorByLODIndex=0,
    GaussianRadius=7.499999832361936e-05,
    ShaderPreset='Sphere',
    CustomTriangleScale=3,
    Emissive=0,
    ScaleByArray=0,
    SetScaleArray=['POINTS', 'p'],
    ScaleArrayComponent='',
    UseScaleFunction=1,
    ScaleTransferFunction='Piecewise Function',
    OpacityByArray=0,
    OpacityArray=['POINTS', 'p'],
    OpacityArrayComponent='',
    OpacityTransferFunction='Piecewise Function',
    DataAxesGrid='Grid Axes Representation',
    SelectionCellLabelBold=0,
    SelectionCellLabelColor=[0.0, 1.0, 0.0],
    SelectionCellLabelFontFamily='Arial',
    SelectionCellLabelFontFile='',
    SelectionCellLabelFontSize=18,
    SelectionCellLabelItalic=0,
    SelectionCellLabelJustification='Left',
    SelectionCellLabelOpacity=1.0,
    SelectionCellLabelShadow=0,
    SelectionPointLabelBold=0,
    SelectionPointLabelColor=[1.0, 1.0, 0.0],
    SelectionPointLabelFontFamily='Arial',
    SelectionPointLabelFontFile='',
    SelectionPointLabelFontSize=18,
    SelectionPointLabelItalic=0,
    SelectionPointLabelJustification='Left',
    SelectionPointLabelOpacity=1.0,
    SelectionPointLabelShadow=0,
    PolarAxes='Polar Axes Representation',
    SelectInputVectors=['POINTS', 'U'],
    NumberOfSteps=40,
    StepSize=0.25,
    NormalizeVectors=1,
    EnhancedLIC=1,
    ColorMode='Blend',
    LICIntensity=0.8,
    MapModeBias=0.0,
    EnhanceContrast='Off',
    LowLICContrastEnhancementFactor=0.0,
    HighLICContrastEnhancementFactor=0.0,
    LowColorContrastEnhancementFactor=0.0,
    HighColorContrastEnhancementFactor=0.0,
    AntiAlias=0,
    MaskOnSurface=1,
    MaskThreshold=0.0,
    MaskIntensity=0.0,
    MaskColor=[0.5, 0.5, 0.5],
    GenerateNoiseTexture=0,
    NoiseType='Gaussian',
    NoiseTextureSize=128,
    NoiseGrainSize=2,
    MinNoiseValue=0.0,
    MaxNoiseValue=0.8,
    NumberOfNoiseLevels=1024,
    ImpulseNoiseProbability=1.0,
    ImpulseNoiseBackgroundValue=0.0,
    NoiseGeneratorSeed=1,
    CompositeStrategy='AUTO',
    UseLICForLOD=0,
    WriteLog='',
    CustomShader=""" // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
""",
)

# init the 'Transform2' selected for 'TextureTransform'
cellDatatoPointData1Display.TextureTransform.Set(
    Translate=[0.0, 0.0, 0.0],
    Rotate=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
cellDatatoPointData1Display.OSPRayScaleFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Arrow' selected for 'GlyphType'
cellDatatoPointData1Display.GlyphType.Set(
    TipResolution=6,
    TipRadius=0.1,
    TipLength=0.35,
    ShaftResolution=6,
    ShaftRadius=0.03,
    Invert=0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Set(
    Points=[617300.0, 0.0, 0.5, 0.0, 617428.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Set(
    Points=[617300.0, 0.0, 0.5, 0.0, 617428.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
cellDatatoPointData1Display.DataAxesGrid.Set(
    XTitle='X Axis',
    YTitle='Y Axis',
    ZTitle='Z Axis',
    XTitleFontFamily='Arial',
    XTitleFontFile='',
    XTitleBold=0,
    XTitleItalic=0,
    XTitleFontSize=12,
    XTitleShadow=0,
    XTitleOpacity=1.0,
    YTitleFontFamily='Arial',
    YTitleFontFile='',
    YTitleBold=0,
    YTitleItalic=0,
    YTitleFontSize=12,
    YTitleShadow=0,
    YTitleOpacity=1.0,
    ZTitleFontFamily='Arial',
    ZTitleFontFile='',
    ZTitleBold=0,
    ZTitleItalic=0,
    ZTitleFontSize=12,
    ZTitleShadow=0,
    ZTitleOpacity=1.0,
    FacesToRender=63,
    CullBackface=0,
    CullFrontface=1,
    ShowGrid=0,
    ShowEdges=1,
    ShowTicks=1,
    LabelUniqueEdgesOnly=1,
    AxesToLabel=63,
    XLabelFontFamily='Arial',
    XLabelFontFile='',
    XLabelBold=0,
    XLabelItalic=0,
    XLabelFontSize=12,
    XLabelShadow=0,
    XLabelOpacity=1.0,
    YLabelFontFamily='Arial',
    YLabelFontFile='',
    YLabelBold=0,
    YLabelItalic=0,
    YLabelFontSize=12,
    YLabelShadow=0,
    YLabelOpacity=1.0,
    ZLabelFontFamily='Arial',
    ZLabelFontFile='',
    ZLabelBold=0,
    ZLabelItalic=0,
    ZLabelFontSize=12,
    ZLabelShadow=0,
    ZLabelOpacity=1.0,
    XAxisNotation='Mixed',
    XAxisPrecision=2,
    XAxisUseCustomLabels=0,
    XAxisLabels=[],
    YAxisNotation='Mixed',
    YAxisPrecision=2,
    YAxisUseCustomLabels=0,
    YAxisLabels=[],
    ZAxisNotation='Mixed',
    ZAxisPrecision=2,
    ZAxisUseCustomLabels=0,
    ZAxisLabels=[],
    UseCustomBounds=0,
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
)

# init the 'Polar Axes Representation' selected for 'PolarAxes'
cellDatatoPointData1Display.PolarAxes.Set(
    Visibility=0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    EnableCustomBounds=[0, 0, 0],
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
    EnableCustomRange=0,
    CustomRange=[0.0, 1.0],
    AutoPole=1,
    PolarAxisVisibility=1,
    RadialAxesVisibility=1,
    DrawRadialGridlines=1,
    PolarArcsVisibility=1,
    DrawPolarArcsGridlines=1,
    NumberOfRadialAxes=0,
    DeltaAngleRadialAxes=45.0,
    NumberOfArcs=5,
    DeltaRangeArcs=0.0,
    CustomMinRadius=1,
    MinimumRadius=0.0,
    CustomMaxRadius=0,
    MaximumRadius=1.0,
    CustomAngles=1,
    MinimumAngle=0.0,
    MaximumAngle=90.0,
    RadialAxesOriginToPolarAxis=1,
    PolarArcResolutionPerDegree=0.2,
    Ratio=1.0,
    EnableOverallColor=1,
    OverallColor=[1.0, 1.0, 1.0],
    PolarAxisColor=[1.0, 1.0, 1.0],
    PolarArcsColor=[1.0, 1.0, 1.0],
    LastRadialAxisColor=[1.0, 1.0, 1.0],
    SecondaryPolarArcsColor=[1.0, 1.0, 1.0],
    SecondaryRadialAxesColor=[1.0, 1.0, 1.0],
    PolarAxisTitleVisibility=1,
    PolarAxisTitle='Radial Distance',
    PolarAxisTitleLocation='Bottom',
    PolarTitleOffset=[20.0, 20.0],
    PolarLabelVisibility=1,
    PolarLabelFormat='%-#6.3g',
    PolarLabelExponentLocation='Labels',
    PolarLabelOffset=10.0,
    PolarExponentOffset=5.0,
    RadialLabelVisibility=1,
    RadialLabelFormat='%-#3.1f',
    RadialLabelLocation='Bottom',
    RadialLabelOffset=[20.0, 0.0],
    RadialUnitsVisibility=1,
    ScreenSize=10.0,
    PolarAxisTitleOpacity=1.0,
    PolarAxisTitleFontFamily='Arial',
    PolarAxisTitleFontFile='',
    PolarAxisTitleBold=0,
    PolarAxisTitleItalic=0,
    PolarAxisTitleShadow=0,
    PolarAxisTitleFontSize=12,
    PolarAxisLabelOpacity=1.0,
    PolarAxisLabelFontFamily='Arial',
    PolarAxisLabelFontFile='',
    PolarAxisLabelBold=0,
    PolarAxisLabelItalic=0,
    PolarAxisLabelShadow=0,
    PolarAxisLabelFontSize=12,
    LastRadialAxisTextOpacity=1.0,
    LastRadialAxisTextFontFamily='Arial',
    LastRadialAxisTextFontFile='',
    LastRadialAxisTextBold=0,
    LastRadialAxisTextItalic=0,
    LastRadialAxisTextShadow=0,
    LastRadialAxisTextFontSize=12,
    SecondaryRadialAxesTextOpacity=1.0,
    SecondaryRadialAxesTextFontFamily='Arial',
    SecondaryRadialAxesTextFontFile='',
    SecondaryRadialAxesTextBold=0,
    SecondaryRadialAxesTextItalic=0,
    SecondaryRadialAxesTextShadow=0,
    SecondaryRadialAxesTextFontSize=12,
    EnableDistanceLOD=1,
    DistanceLODThreshold=0.7,
    EnableViewAngleLOD=1,
    ViewAngleLODThreshold=0.7,
    SmallestVisiblePolarAngle=0.5,
    AllTicksVisibility=1,
    ArcTicksOriginToPolarAxis=1,
    TickLocation='Both',
    AxisTickVisibility=1,
    AxisMinorTickVisibility=0,
    AxisTickMatchesPolarAxes=1,
    DeltaRangeMajor=1.0,
    DeltaRangeMinor=0.5,
    ArcTickVisibility=1,
    ArcMinorTickVisibility=0,
    ArcTickMatchesRadialAxes=1,
    DeltaAngleMajor=10.0,
    DeltaAngleMinor=5.0,
    TickRatioRadiusSize=0.02,
    PolarAxisMajorTickSize=0.0,
    PolarAxisTickRatioSize=0.3,
    PolarAxisMajorTickThickness=1.0,
    PolarAxisTickRatioThickness=0.5,
    LastRadialAxisMajorTickSize=0.0,
    LastRadialAxisTickRatioSize=0.3,
    LastRadialAxisMajorTickThickness=1.0,
    LastRadialAxisTickRatioThickness=0.5,
    ArcMajorTickSize=0.0,
    ArcTickRatioSize=0.3,
    ArcMajorTickThickness=1.0,
    ArcTickRatioThickness=0.5,
    Use2DMode=0,
    UseLogAxis=0,
)

# hide data in view
Hide(afoam, renderView1)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(cellDatatoPointData1Display, ('POINTS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
cellDatatoPointData1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')
uTF2D.Set(
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    Boxes=[],
    ScalarRangeInitialized=0,
    Range=[0.0, 1.0, 0.0, 1.0],
    OutputDimensions=[10, 10],
)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.Set(
    InterpretValuesAsCategories=0,
    AnnotationsInitialized=0,
    ShowCategoricalColorsinDataRangeOnly=0,
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    RescaleOnVisibilityChange=0,
    TransferFunction2D=uTF2D,
    RGBPoints=GenerateRGBPoints(
        range_min=0.015557776216027863,
        range_max=1.9412411950441164,
    ),
    UseLogScale=0,
    UseOpacityControlPointsFreehandDrawing=0,
    ShowDataHistogram=0,
    AutomaticDataHistogramComputation=0,
    DataHistogramNumberOfBins=10,
    ColorSpace='Lab',
    UseBelowRangeColor=0,
    BelowRangeColor=[0.0, 0.0, 0.0],
    UseAboveRangeColor=0,
    AboveRangeColor=[0.5, 0.5, 0.5],
    NanColor=[0.0, 1.0, 0.0],
    NanOpacity=1.0,
    Discretize=1,
    NumberOfTableValues=256,
    ScalarRangeInitialized=1.0,
    HSVWrap=0,
    VectorComponent=0,
    VectorMode='Magnitude',
    AllowDuplicateScalars=1,
    Annotations=[],
    ActiveAnnotatedValues=[],
    IndexedColors=[],
    IndexedOpacities=[],
    EnableOpacityMapping=0,
)

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Set(
    Points=[0.015557776216027863, 0.0, 0.5, 0.0, 1.9412411950441164, 1.0, 0.5, 0.0],
    AllowDuplicateScalars=1,
    UseLogScale=0,
    ScalarRangeInitialized=1,
)

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.GoToLast()

animationScene1.GoToLast()

animationScene1.GoToLast()

# set scalar coloring
ColorBy(cellDatatoPointData1Display, ('POINTS', 'c'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(uLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
cellDatatoPointData1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'c'
cTF2D = GetTransferFunction2D('c')
cTF2D.Set(
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    Boxes=[],
    ScalarRangeInitialized=0,
    Range=[0.0, 1.0, 0.0, 1.0],
    OutputDimensions=[10, 10],
)

# get color transfer function/color map for 'c'
cLUT = GetColorTransferFunction('c')
cLUT.Set(
    InterpretValuesAsCategories=0,
    AnnotationsInitialized=0,
    ShowCategoricalColorsinDataRangeOnly=0,
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    RescaleOnVisibilityChange=0,
    TransferFunction2D=cTF2D,
    RGBPoints=GenerateRGBPoints(
        range_min=0.42694899439811707,
        range_max=0.4684324860572815,
    ),
    UseLogScale=0,
    UseOpacityControlPointsFreehandDrawing=0,
    ShowDataHistogram=0,
    AutomaticDataHistogramComputation=0,
    DataHistogramNumberOfBins=10,
    ColorSpace='Lab',
    UseBelowRangeColor=0,
    BelowRangeColor=[0.0, 0.0, 0.0],
    UseAboveRangeColor=0,
    AboveRangeColor=[0.5, 0.5, 0.5],
    NanColor=[0.0, 1.0, 0.0],
    NanOpacity=1.0,
    Discretize=1,
    NumberOfTableValues=256,
    ScalarRangeInitialized=1.0,
    HSVWrap=0,
    VectorComponent=0,
    VectorMode='Magnitude',
    AllowDuplicateScalars=1,
    Annotations=[],
    ActiveAnnotatedValues=[],
    IndexedColors=[],
    IndexedOpacities=[],
    EnableOpacityMapping=0,
)

# get opacity transfer function/opacity map for 'c'
cPWF = GetOpacityTransferFunction('c')
cPWF.Set(
    Points=[0.42694899439811707, 0.0, 0.5, 0.0, 0.4684324860572815, 1.0, 0.5, 0.0],
    AllowDuplicateScalars=1,
    UseLogScale=0,
    ScalarRangeInitialized=1,
)

# create a new 'Surface Normals'
surfaceNormals1 = SurfaceNormals(registrationName='SurfaceNormals1', Input=cellDatatoPointData1)
surfaceNormals1.Set(
    Consistency=1,
    NonManifoldTraversal=1,
    Splitting=1,
    FeatureAngle=30.0,
    FlipNormals=0,
    ComputeCellNormals=0,
    PieceInvariant=1,
)

# show data in view
surfaceNormals1Display = Show(surfaceNormals1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
surfaceNormals1Display.Set(
    Selection=None,
    Representation='Surface',
    ColorArrayName=['POINTS', 'p'],
    LookupTable=pLUT,
    MapScalars=1,
    MultiComponentsMapping=0,
    InterpolateScalarsBeforeMapping=1,
    UseNanColorForMissingArrays=0,
    Opacity=1.0,
    PointSize=2.0,
    LineWidth=1.0,
    RenderLinesAsTubes=0,
    RenderPointsAsSpheres=0,
    DisableLighting=0,
    Diffuse=1.0,
    Interpolation='Gouraud',
    Specular=0.0,
    SpecularColor=[1.0, 1.0, 1.0],
    SpecularPower=100.0,
    Luminosity=0.0,
    Ambient=0.0,
    Roughness=0.3,
    Metallic=0.0,
    EdgeTint=[1.0, 1.0, 1.0],
    Anisotropy=0.0,
    AnisotropyRotation=0.0,
    BaseIOR=1.5,
    CoatStrength=0.0,
    CoatIOR=2.0,
    CoatRoughness=0.0,
    CoatColor=[1.0, 1.0, 1.0],
    SelectNormalArray='Normals',
    SelectTangentArray='None',
    ComputePointNormals=0,
    Splitting=1,
    FeatureAngle=30.0,
    SelectTCoordArray='None',
    Texture=None,
    RepeatTextures=1,
    InterpolateTextures=0,
    SeamlessU=0,
    SeamlessV=0,
    UseMipmapTextures=0,
    ShowTexturesOnBackface=1,
    BaseColorTexture=None,
    NormalTexture=None,
    NormalScale=1.0,
    CoatNormalTexture=None,
    CoatNormalScale=1.0,
    MaterialTexture=None,
    OcclusionStrength=1.0,
    AnisotropyTexture=None,
    EmissiveTexture=None,
    EmissiveFactor=[1.0, 1.0, 1.0],
    TextureTransform='Transform2',
    EdgeOpacity=1.0,
    BackfaceRepresentation='Follow Frontface',
    BackfaceAmbientColor=[1.0, 1.0, 1.0],
    BackfaceOpacity=1.0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    Origin=[0.0, 0.0, 0.0],
    CoordinateShiftScaleMethod='Always Auto Shift Scale',
    CoordinateSystem='Navigable',
    Pickable=1,
    Triangulate=0,
    UseShaderReplacements=0,
    ShaderReplacements='',
    NonlinearSubdivisionLevel=1,
    MatchBoundariesIgnoringCellOrder=0,
    UseDataPartitions=0,
    OSPRayUseScaleArray='All Approximate',
    OSPRayScaleArray='p',
    OSPRayScaleFunction='Piecewise Function',
    OSPRayMaterial='None',
    Assembly='Hierarchy',
    SelectedBlockSelectors=[''],
    BlockSelectors=['/'],
    BlockColors=[],
    BlockColorArrayNames=[],
    BlockLookupTables=[],
    BlockUseSeparateColorMaps=[],
    BlockMapScalars=[],
    BlockInterpolateScalarsBeforeMappings=[],
    BlockOpacities=[],
    BlockMapScalarsGUI=1,
    BlockInterpolateScalarsBeforeMappingsGUI=1,
    BlockOpacitiesGUI=1.0,
    Orient=0,
    OrientationMode='Direction',
    SelectOrientationVectors='U',
    Scaling=0,
    ScaleMode='No Data Scaling Off',
    ScaleFactor=0.0014999999664723875,
    SelectScaleArray='p',
    GlyphType='Arrow',
    UseGlyphTable=0,
    GlyphTableIndexArray='p',
    UseCompositeGlyphTable=0,
    UseGlyphCullingAndLOD=0,
    LODValues=[],
    ColorByLODIndex=0,
    GaussianRadius=7.499999832361936e-05,
    ShaderPreset='Sphere',
    CustomTriangleScale=3,
    Emissive=0,
    ScaleByArray=0,
    SetScaleArray=['POINTS', 'p'],
    ScaleArrayComponent='',
    UseScaleFunction=1,
    ScaleTransferFunction='Piecewise Function',
    OpacityByArray=0,
    OpacityArray=['POINTS', 'p'],
    OpacityArrayComponent='',
    OpacityTransferFunction='Piecewise Function',
    DataAxesGrid='Grid Axes Representation',
    SelectionCellLabelBold=0,
    SelectionCellLabelColor=[0.0, 1.0, 0.0],
    SelectionCellLabelFontFamily='Arial',
    SelectionCellLabelFontFile='',
    SelectionCellLabelFontSize=18,
    SelectionCellLabelItalic=0,
    SelectionCellLabelJustification='Left',
    SelectionCellLabelOpacity=1.0,
    SelectionCellLabelShadow=0,
    SelectionPointLabelBold=0,
    SelectionPointLabelColor=[1.0, 1.0, 0.0],
    SelectionPointLabelFontFamily='Arial',
    SelectionPointLabelFontFile='',
    SelectionPointLabelFontSize=18,
    SelectionPointLabelItalic=0,
    SelectionPointLabelJustification='Left',
    SelectionPointLabelOpacity=1.0,
    SelectionPointLabelShadow=0,
    PolarAxes='Polar Axes Representation',
    SelectInputVectors=['POINTS', 'U'],
    NumberOfSteps=40,
    StepSize=0.25,
    NormalizeVectors=1,
    EnhancedLIC=1,
    ColorMode='Blend',
    LICIntensity=0.8,
    MapModeBias=0.0,
    EnhanceContrast='Off',
    LowLICContrastEnhancementFactor=0.0,
    HighLICContrastEnhancementFactor=0.0,
    LowColorContrastEnhancementFactor=0.0,
    HighColorContrastEnhancementFactor=0.0,
    AntiAlias=0,
    MaskOnSurface=1,
    MaskThreshold=0.0,
    MaskIntensity=0.0,
    MaskColor=[0.5, 0.5, 0.5],
    GenerateNoiseTexture=0,
    NoiseType='Gaussian',
    NoiseTextureSize=128,
    NoiseGrainSize=2,
    MinNoiseValue=0.0,
    MaxNoiseValue=0.8,
    NumberOfNoiseLevels=1024,
    ImpulseNoiseProbability=1.0,
    ImpulseNoiseBackgroundValue=0.0,
    NoiseGeneratorSeed=1,
    CompositeStrategy='AUTO',
    UseLICForLOD=0,
    WriteLog='',
    CustomShader=""" // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
""",
)

# init the 'Transform2' selected for 'TextureTransform'
surfaceNormals1Display.TextureTransform.Set(
    Translate=[0.0, 0.0, 0.0],
    Rotate=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
surfaceNormals1Display.OSPRayScaleFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Arrow' selected for 'GlyphType'
surfaceNormals1Display.GlyphType.Set(
    TipResolution=6,
    TipRadius=0.1,
    TipLength=0.35,
    ShaftResolution=6,
    ShaftRadius=0.03,
    Invert=0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
surfaceNormals1Display.ScaleTransferFunction.Set(
    Points=[617300.0, 0.0, 0.5, 0.0, 617428.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
surfaceNormals1Display.OpacityTransferFunction.Set(
    Points=[617300.0, 0.0, 0.5, 0.0, 617428.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
surfaceNormals1Display.DataAxesGrid.Set(
    XTitle='X Axis',
    YTitle='Y Axis',
    ZTitle='Z Axis',
    XTitleFontFamily='Arial',
    XTitleFontFile='',
    XTitleBold=0,
    XTitleItalic=0,
    XTitleFontSize=12,
    XTitleShadow=0,
    XTitleOpacity=1.0,
    YTitleFontFamily='Arial',
    YTitleFontFile='',
    YTitleBold=0,
    YTitleItalic=0,
    YTitleFontSize=12,
    YTitleShadow=0,
    YTitleOpacity=1.0,
    ZTitleFontFamily='Arial',
    ZTitleFontFile='',
    ZTitleBold=0,
    ZTitleItalic=0,
    ZTitleFontSize=12,
    ZTitleShadow=0,
    ZTitleOpacity=1.0,
    FacesToRender=63,
    CullBackface=0,
    CullFrontface=1,
    ShowGrid=0,
    ShowEdges=1,
    ShowTicks=1,
    LabelUniqueEdgesOnly=1,
    AxesToLabel=63,
    XLabelFontFamily='Arial',
    XLabelFontFile='',
    XLabelBold=0,
    XLabelItalic=0,
    XLabelFontSize=12,
    XLabelShadow=0,
    XLabelOpacity=1.0,
    YLabelFontFamily='Arial',
    YLabelFontFile='',
    YLabelBold=0,
    YLabelItalic=0,
    YLabelFontSize=12,
    YLabelShadow=0,
    YLabelOpacity=1.0,
    ZLabelFontFamily='Arial',
    ZLabelFontFile='',
    ZLabelBold=0,
    ZLabelItalic=0,
    ZLabelFontSize=12,
    ZLabelShadow=0,
    ZLabelOpacity=1.0,
    XAxisNotation='Mixed',
    XAxisPrecision=2,
    XAxisUseCustomLabels=0,
    XAxisLabels=[],
    YAxisNotation='Mixed',
    YAxisPrecision=2,
    YAxisUseCustomLabels=0,
    YAxisLabels=[],
    ZAxisNotation='Mixed',
    ZAxisPrecision=2,
    ZAxisUseCustomLabels=0,
    ZAxisLabels=[],
    UseCustomBounds=0,
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
)

# init the 'Polar Axes Representation' selected for 'PolarAxes'
surfaceNormals1Display.PolarAxes.Set(
    Visibility=0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    EnableCustomBounds=[0, 0, 0],
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
    EnableCustomRange=0,
    CustomRange=[0.0, 1.0],
    AutoPole=1,
    PolarAxisVisibility=1,
    RadialAxesVisibility=1,
    DrawRadialGridlines=1,
    PolarArcsVisibility=1,
    DrawPolarArcsGridlines=1,
    NumberOfRadialAxes=0,
    DeltaAngleRadialAxes=45.0,
    NumberOfArcs=5,
    DeltaRangeArcs=0.0,
    CustomMinRadius=1,
    MinimumRadius=0.0,
    CustomMaxRadius=0,
    MaximumRadius=1.0,
    CustomAngles=1,
    MinimumAngle=0.0,
    MaximumAngle=90.0,
    RadialAxesOriginToPolarAxis=1,
    PolarArcResolutionPerDegree=0.2,
    Ratio=1.0,
    EnableOverallColor=1,
    OverallColor=[1.0, 1.0, 1.0],
    PolarAxisColor=[1.0, 1.0, 1.0],
    PolarArcsColor=[1.0, 1.0, 1.0],
    LastRadialAxisColor=[1.0, 1.0, 1.0],
    SecondaryPolarArcsColor=[1.0, 1.0, 1.0],
    SecondaryRadialAxesColor=[1.0, 1.0, 1.0],
    PolarAxisTitleVisibility=1,
    PolarAxisTitle='Radial Distance',
    PolarAxisTitleLocation='Bottom',
    PolarTitleOffset=[20.0, 20.0],
    PolarLabelVisibility=1,
    PolarLabelFormat='%-#6.3g',
    PolarLabelExponentLocation='Labels',
    PolarLabelOffset=10.0,
    PolarExponentOffset=5.0,
    RadialLabelVisibility=1,
    RadialLabelFormat='%-#3.1f',
    RadialLabelLocation='Bottom',
    RadialLabelOffset=[20.0, 0.0],
    RadialUnitsVisibility=1,
    ScreenSize=10.0,
    PolarAxisTitleOpacity=1.0,
    PolarAxisTitleFontFamily='Arial',
    PolarAxisTitleFontFile='',
    PolarAxisTitleBold=0,
    PolarAxisTitleItalic=0,
    PolarAxisTitleShadow=0,
    PolarAxisTitleFontSize=12,
    PolarAxisLabelOpacity=1.0,
    PolarAxisLabelFontFamily='Arial',
    PolarAxisLabelFontFile='',
    PolarAxisLabelBold=0,
    PolarAxisLabelItalic=0,
    PolarAxisLabelShadow=0,
    PolarAxisLabelFontSize=12,
    LastRadialAxisTextOpacity=1.0,
    LastRadialAxisTextFontFamily='Arial',
    LastRadialAxisTextFontFile='',
    LastRadialAxisTextBold=0,
    LastRadialAxisTextItalic=0,
    LastRadialAxisTextShadow=0,
    LastRadialAxisTextFontSize=12,
    SecondaryRadialAxesTextOpacity=1.0,
    SecondaryRadialAxesTextFontFamily='Arial',
    SecondaryRadialAxesTextFontFile='',
    SecondaryRadialAxesTextBold=0,
    SecondaryRadialAxesTextItalic=0,
    SecondaryRadialAxesTextShadow=0,
    SecondaryRadialAxesTextFontSize=12,
    EnableDistanceLOD=1,
    DistanceLODThreshold=0.7,
    EnableViewAngleLOD=1,
    ViewAngleLODThreshold=0.7,
    SmallestVisiblePolarAngle=0.5,
    AllTicksVisibility=1,
    ArcTicksOriginToPolarAxis=1,
    TickLocation='Both',
    AxisTickVisibility=1,
    AxisMinorTickVisibility=0,
    AxisTickMatchesPolarAxes=1,
    DeltaRangeMajor=1.0,
    DeltaRangeMinor=0.5,
    ArcTickVisibility=1,
    ArcMinorTickVisibility=0,
    ArcTickMatchesRadialAxes=1,
    DeltaAngleMajor=10.0,
    DeltaAngleMinor=5.0,
    TickRatioRadiusSize=0.02,
    PolarAxisMajorTickSize=0.0,
    PolarAxisTickRatioSize=0.3,
    PolarAxisMajorTickThickness=1.0,
    PolarAxisTickRatioThickness=0.5,
    LastRadialAxisMajorTickSize=0.0,
    LastRadialAxisTickRatioSize=0.3,
    LastRadialAxisMajorTickThickness=1.0,
    LastRadialAxisTickRatioThickness=0.5,
    ArcMajorTickSize=0.0,
    ArcTickRatioSize=0.3,
    ArcMajorTickThickness=1.0,
    ArcTickRatioThickness=0.5,
    Use2DMode=0,
    UseLogAxis=0,
)

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# show color bar/color legend
surfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(surfaceNormals1Display, ('POINTS', 'Normals', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
surfaceNormals1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
surfaceNormals1Display.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'Normals'
normalsTF2D = GetTransferFunction2D('Normals')
normalsTF2D.Set(
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    Boxes=[],
    ScalarRangeInitialized=0,
    Range=[0.0, 1.0, 0.0, 1.0],
    OutputDimensions=[10, 10],
)

# get color transfer function/color map for 'Normals'
normalsLUT = GetColorTransferFunction('Normals')
normalsLUT.Set(
    InterpretValuesAsCategories=0,
    AnnotationsInitialized=0,
    ShowCategoricalColorsinDataRangeOnly=0,
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    RescaleOnVisibilityChange=0,
    TransferFunction2D=normalsTF2D,
    RGBPoints=GenerateRGBPoints(
        range_min=1.0,
        range_max=1.000244140625,
    ),
    UseLogScale=0,
    UseOpacityControlPointsFreehandDrawing=0,
    ShowDataHistogram=0,
    AutomaticDataHistogramComputation=0,
    DataHistogramNumberOfBins=10,
    ColorSpace='Lab',
    UseBelowRangeColor=0,
    BelowRangeColor=[0.0, 0.0, 0.0],
    UseAboveRangeColor=0,
    AboveRangeColor=[0.5, 0.5, 0.5],
    NanColor=[0.0, 1.0, 0.0],
    NanOpacity=1.0,
    Discretize=1,
    NumberOfTableValues=256,
    ScalarRangeInitialized=1.0,
    HSVWrap=0,
    VectorComponent=0,
    VectorMode='Magnitude',
    AllowDuplicateScalars=1,
    Annotations=[],
    ActiveAnnotatedValues=[],
    IndexedColors=[],
    IndexedOpacities=[],
    EnableOpacityMapping=0,
)

# get opacity transfer function/opacity map for 'Normals'
normalsPWF = GetOpacityTransferFunction('Normals')
normalsPWF.Set(
    Points=[1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0],
    AllowDuplicateScalars=1,
    UseLogScale=0,
    ScalarRangeInitialized=1,
)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=surfaceNormals1)
calculator1.Set(
    AttributeType='Point Data',
    CoordinateResults=0,
    ResultNormals=0,
    ResultTCoords=0,
    ResultArrayName='Result',
    Function='',
    ReplaceInvalidResults=1,
    ReplacementValue=0.0,
    ResultArrayType='Double',
)

# Properties modified on calculator1
calculator1.Set(
    ResultArrayName='U_n',
    Function='U_0*Normals_0',
)

# show data in view
calculator1Display = Show(calculator1, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'U_n'
u_nTF2D = GetTransferFunction2D('U_n')
u_nTF2D.Set(
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    Boxes=[],
    ScalarRangeInitialized=0,
    Range=[0.0, 1.0, 0.0, 1.0],
    OutputDimensions=[10, 10],
)

# get color transfer function/color map for 'U_n'
u_nLUT = GetColorTransferFunction('U_n')
u_nLUT.Set(
    InterpretValuesAsCategories=0,
    AnnotationsInitialized=0,
    ShowCategoricalColorsinDataRangeOnly=0,
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    RescaleOnVisibilityChange=0,
    TransferFunction2D=u_nTF2D,
    RGBPoints=GenerateRGBPoints(
        range_min=-0.07564295083284378,
        range_max=0.1788800060749054,
    ),
    UseLogScale=0,
    UseOpacityControlPointsFreehandDrawing=0,
    ShowDataHistogram=0,
    AutomaticDataHistogramComputation=0,
    DataHistogramNumberOfBins=10,
    ColorSpace='Lab',
    UseBelowRangeColor=0,
    BelowRangeColor=[0.0, 0.0, 0.0],
    UseAboveRangeColor=0,
    AboveRangeColor=[0.5, 0.5, 0.5],
    NanColor=[0.0, 1.0, 0.0],
    NanOpacity=1.0,
    Discretize=1,
    NumberOfTableValues=256,
    ScalarRangeInitialized=1.0,
    HSVWrap=0,
    VectorComponent=0,
    VectorMode='Magnitude',
    AllowDuplicateScalars=1,
    Annotations=[],
    ActiveAnnotatedValues=[],
    IndexedColors=[],
    IndexedOpacities=[],
    EnableOpacityMapping=0,
)

# trace defaults for the display properties.
calculator1Display.Set(
    Selection=None,
    Representation='Surface',
    ColorArrayName=['POINTS', 'U_n'],
    LookupTable=u_nLUT,
    MapScalars=1,
    MultiComponentsMapping=0,
    InterpolateScalarsBeforeMapping=1,
    UseNanColorForMissingArrays=0,
    Opacity=1.0,
    PointSize=2.0,
    LineWidth=1.0,
    RenderLinesAsTubes=0,
    RenderPointsAsSpheres=0,
    DisableLighting=0,
    Diffuse=1.0,
    Interpolation='Gouraud',
    Specular=0.0,
    SpecularColor=[1.0, 1.0, 1.0],
    SpecularPower=100.0,
    Luminosity=0.0,
    Ambient=0.0,
    Roughness=0.3,
    Metallic=0.0,
    EdgeTint=[1.0, 1.0, 1.0],
    Anisotropy=0.0,
    AnisotropyRotation=0.0,
    BaseIOR=1.5,
    CoatStrength=0.0,
    CoatIOR=2.0,
    CoatRoughness=0.0,
    CoatColor=[1.0, 1.0, 1.0],
    SelectNormalArray='Normals',
    SelectTangentArray='None',
    ComputePointNormals=0,
    Splitting=1,
    FeatureAngle=30.0,
    SelectTCoordArray='None',
    Texture=None,
    RepeatTextures=1,
    InterpolateTextures=0,
    SeamlessU=0,
    SeamlessV=0,
    UseMipmapTextures=0,
    ShowTexturesOnBackface=1,
    BaseColorTexture=None,
    NormalTexture=None,
    NormalScale=1.0,
    CoatNormalTexture=None,
    CoatNormalScale=1.0,
    MaterialTexture=None,
    OcclusionStrength=1.0,
    AnisotropyTexture=None,
    EmissiveTexture=None,
    EmissiveFactor=[1.0, 1.0, 1.0],
    TextureTransform='Transform2',
    EdgeOpacity=1.0,
    BackfaceRepresentation='Follow Frontface',
    BackfaceAmbientColor=[1.0, 1.0, 1.0],
    BackfaceOpacity=1.0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    Origin=[0.0, 0.0, 0.0],
    CoordinateShiftScaleMethod='Always Auto Shift Scale',
    CoordinateSystem='Navigable',
    Pickable=1,
    Triangulate=0,
    UseShaderReplacements=0,
    ShaderReplacements='',
    NonlinearSubdivisionLevel=1,
    MatchBoundariesIgnoringCellOrder=0,
    UseDataPartitions=0,
    OSPRayUseScaleArray='All Approximate',
    OSPRayScaleArray='U_n',
    OSPRayScaleFunction='Piecewise Function',
    OSPRayMaterial='None',
    Assembly='Hierarchy',
    SelectedBlockSelectors=[''],
    BlockSelectors=['/'],
    BlockColors=[],
    BlockColorArrayNames=[],
    BlockLookupTables=[],
    BlockUseSeparateColorMaps=[],
    BlockMapScalars=[],
    BlockInterpolateScalarsBeforeMappings=[],
    BlockOpacities=[],
    BlockMapScalarsGUI=1,
    BlockInterpolateScalarsBeforeMappingsGUI=1,
    BlockOpacitiesGUI=1.0,
    Orient=0,
    OrientationMode='Direction',
    SelectOrientationVectors='U',
    Scaling=0,
    ScaleMode='No Data Scaling Off',
    ScaleFactor=0.0014999999664723875,
    SelectScaleArray='U_n',
    GlyphType='Arrow',
    UseGlyphTable=0,
    GlyphTableIndexArray='U_n',
    UseCompositeGlyphTable=0,
    UseGlyphCullingAndLOD=0,
    LODValues=[],
    ColorByLODIndex=0,
    GaussianRadius=7.499999832361936e-05,
    ShaderPreset='Sphere',
    CustomTriangleScale=3,
    Emissive=0,
    ScaleByArray=0,
    SetScaleArray=['POINTS', 'U_n'],
    ScaleArrayComponent='',
    UseScaleFunction=1,
    ScaleTransferFunction='Piecewise Function',
    OpacityByArray=0,
    OpacityArray=['POINTS', 'U_n'],
    OpacityArrayComponent='',
    OpacityTransferFunction='Piecewise Function',
    DataAxesGrid='Grid Axes Representation',
    SelectionCellLabelBold=0,
    SelectionCellLabelColor=[0.0, 1.0, 0.0],
    SelectionCellLabelFontFamily='Arial',
    SelectionCellLabelFontFile='',
    SelectionCellLabelFontSize=18,
    SelectionCellLabelItalic=0,
    SelectionCellLabelJustification='Left',
    SelectionCellLabelOpacity=1.0,
    SelectionCellLabelShadow=0,
    SelectionPointLabelBold=0,
    SelectionPointLabelColor=[1.0, 1.0, 0.0],
    SelectionPointLabelFontFamily='Arial',
    SelectionPointLabelFontFile='',
    SelectionPointLabelFontSize=18,
    SelectionPointLabelItalic=0,
    SelectionPointLabelJustification='Left',
    SelectionPointLabelOpacity=1.0,
    SelectionPointLabelShadow=0,
    PolarAxes='Polar Axes Representation',
    SelectInputVectors=['POINTS', 'U'],
    NumberOfSteps=40,
    StepSize=0.25,
    NormalizeVectors=1,
    EnhancedLIC=1,
    ColorMode='Blend',
    LICIntensity=0.8,
    MapModeBias=0.0,
    EnhanceContrast='Off',
    LowLICContrastEnhancementFactor=0.0,
    HighLICContrastEnhancementFactor=0.0,
    LowColorContrastEnhancementFactor=0.0,
    HighColorContrastEnhancementFactor=0.0,
    AntiAlias=0,
    MaskOnSurface=1,
    MaskThreshold=0.0,
    MaskIntensity=0.0,
    MaskColor=[0.5, 0.5, 0.5],
    GenerateNoiseTexture=0,
    NoiseType='Gaussian',
    NoiseTextureSize=128,
    NoiseGrainSize=2,
    MinNoiseValue=0.0,
    MaxNoiseValue=0.8,
    NumberOfNoiseLevels=1024,
    ImpulseNoiseProbability=1.0,
    ImpulseNoiseBackgroundValue=0.0,
    NoiseGeneratorSeed=1,
    CompositeStrategy='AUTO',
    UseLICForLOD=0,
    WriteLog='',
    CustomShader=""" // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
""",
)

# init the 'Transform2' selected for 'TextureTransform'
calculator1Display.TextureTransform.Set(
    Translate=[0.0, 0.0, 0.0],
    Rotate=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Arrow' selected for 'GlyphType'
calculator1Display.GlyphType.Set(
    TipResolution=6,
    TipRadius=0.1,
    TipLength=0.35,
    ShaftResolution=6,
    ShaftRadius=0.03,
    Invert=0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Set(
    Points=[-0.07564295083284378, 0.0, 0.5, 0.0, 0.1788800060749054, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Set(
    Points=[-0.07564295083284378, 0.0, 0.5, 0.0, 0.1788800060749054, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.Set(
    XTitle='X Axis',
    YTitle='Y Axis',
    ZTitle='Z Axis',
    XTitleFontFamily='Arial',
    XTitleFontFile='',
    XTitleBold=0,
    XTitleItalic=0,
    XTitleFontSize=12,
    XTitleShadow=0,
    XTitleOpacity=1.0,
    YTitleFontFamily='Arial',
    YTitleFontFile='',
    YTitleBold=0,
    YTitleItalic=0,
    YTitleFontSize=12,
    YTitleShadow=0,
    YTitleOpacity=1.0,
    ZTitleFontFamily='Arial',
    ZTitleFontFile='',
    ZTitleBold=0,
    ZTitleItalic=0,
    ZTitleFontSize=12,
    ZTitleShadow=0,
    ZTitleOpacity=1.0,
    FacesToRender=63,
    CullBackface=0,
    CullFrontface=1,
    ShowGrid=0,
    ShowEdges=1,
    ShowTicks=1,
    LabelUniqueEdgesOnly=1,
    AxesToLabel=63,
    XLabelFontFamily='Arial',
    XLabelFontFile='',
    XLabelBold=0,
    XLabelItalic=0,
    XLabelFontSize=12,
    XLabelShadow=0,
    XLabelOpacity=1.0,
    YLabelFontFamily='Arial',
    YLabelFontFile='',
    YLabelBold=0,
    YLabelItalic=0,
    YLabelFontSize=12,
    YLabelShadow=0,
    YLabelOpacity=1.0,
    ZLabelFontFamily='Arial',
    ZLabelFontFile='',
    ZLabelBold=0,
    ZLabelItalic=0,
    ZLabelFontSize=12,
    ZLabelShadow=0,
    ZLabelOpacity=1.0,
    XAxisNotation='Mixed',
    XAxisPrecision=2,
    XAxisUseCustomLabels=0,
    XAxisLabels=[],
    YAxisNotation='Mixed',
    YAxisPrecision=2,
    YAxisUseCustomLabels=0,
    YAxisLabels=[],
    ZAxisNotation='Mixed',
    ZAxisPrecision=2,
    ZAxisUseCustomLabels=0,
    ZAxisLabels=[],
    UseCustomBounds=0,
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
)

# init the 'Polar Axes Representation' selected for 'PolarAxes'
calculator1Display.PolarAxes.Set(
    Visibility=0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    EnableCustomBounds=[0, 0, 0],
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
    EnableCustomRange=0,
    CustomRange=[0.0, 1.0],
    AutoPole=1,
    PolarAxisVisibility=1,
    RadialAxesVisibility=1,
    DrawRadialGridlines=1,
    PolarArcsVisibility=1,
    DrawPolarArcsGridlines=1,
    NumberOfRadialAxes=0,
    DeltaAngleRadialAxes=45.0,
    NumberOfArcs=5,
    DeltaRangeArcs=0.0,
    CustomMinRadius=1,
    MinimumRadius=0.0,
    CustomMaxRadius=0,
    MaximumRadius=1.0,
    CustomAngles=1,
    MinimumAngle=0.0,
    MaximumAngle=90.0,
    RadialAxesOriginToPolarAxis=1,
    PolarArcResolutionPerDegree=0.2,
    Ratio=1.0,
    EnableOverallColor=1,
    OverallColor=[1.0, 1.0, 1.0],
    PolarAxisColor=[1.0, 1.0, 1.0],
    PolarArcsColor=[1.0, 1.0, 1.0],
    LastRadialAxisColor=[1.0, 1.0, 1.0],
    SecondaryPolarArcsColor=[1.0, 1.0, 1.0],
    SecondaryRadialAxesColor=[1.0, 1.0, 1.0],
    PolarAxisTitleVisibility=1,
    PolarAxisTitle='Radial Distance',
    PolarAxisTitleLocation='Bottom',
    PolarTitleOffset=[20.0, 20.0],
    PolarLabelVisibility=1,
    PolarLabelFormat='%-#6.3g',
    PolarLabelExponentLocation='Labels',
    PolarLabelOffset=10.0,
    PolarExponentOffset=5.0,
    RadialLabelVisibility=1,
    RadialLabelFormat='%-#3.1f',
    RadialLabelLocation='Bottom',
    RadialLabelOffset=[20.0, 0.0],
    RadialUnitsVisibility=1,
    ScreenSize=10.0,
    PolarAxisTitleOpacity=1.0,
    PolarAxisTitleFontFamily='Arial',
    PolarAxisTitleFontFile='',
    PolarAxisTitleBold=0,
    PolarAxisTitleItalic=0,
    PolarAxisTitleShadow=0,
    PolarAxisTitleFontSize=12,
    PolarAxisLabelOpacity=1.0,
    PolarAxisLabelFontFamily='Arial',
    PolarAxisLabelFontFile='',
    PolarAxisLabelBold=0,
    PolarAxisLabelItalic=0,
    PolarAxisLabelShadow=0,
    PolarAxisLabelFontSize=12,
    LastRadialAxisTextOpacity=1.0,
    LastRadialAxisTextFontFamily='Arial',
    LastRadialAxisTextFontFile='',
    LastRadialAxisTextBold=0,
    LastRadialAxisTextItalic=0,
    LastRadialAxisTextShadow=0,
    LastRadialAxisTextFontSize=12,
    SecondaryRadialAxesTextOpacity=1.0,
    SecondaryRadialAxesTextFontFamily='Arial',
    SecondaryRadialAxesTextFontFile='',
    SecondaryRadialAxesTextBold=0,
    SecondaryRadialAxesTextItalic=0,
    SecondaryRadialAxesTextShadow=0,
    SecondaryRadialAxesTextFontSize=12,
    EnableDistanceLOD=1,
    DistanceLODThreshold=0.7,
    EnableViewAngleLOD=1,
    ViewAngleLODThreshold=0.7,
    SmallestVisiblePolarAngle=0.5,
    AllTicksVisibility=1,
    ArcTicksOriginToPolarAxis=1,
    TickLocation='Both',
    AxisTickVisibility=1,
    AxisMinorTickVisibility=0,
    AxisTickMatchesPolarAxes=1,
    DeltaRangeMajor=1.0,
    DeltaRangeMinor=0.5,
    ArcTickVisibility=1,
    ArcMinorTickVisibility=0,
    ArcTickMatchesRadialAxes=1,
    DeltaAngleMajor=10.0,
    DeltaAngleMinor=5.0,
    TickRatioRadiusSize=0.02,
    PolarAxisMajorTickSize=0.0,
    PolarAxisTickRatioSize=0.3,
    PolarAxisMajorTickThickness=1.0,
    PolarAxisTickRatioThickness=0.5,
    LastRadialAxisMajorTickSize=0.0,
    LastRadialAxisTickRatioSize=0.3,
    LastRadialAxisMajorTickThickness=1.0,
    LastRadialAxisTickRatioThickness=0.5,
    ArcMajorTickSize=0.0,
    ArcTickRatioSize=0.3,
    ArcMajorTickThickness=1.0,
    ArcTickRatioThickness=0.5,
    Use2DMode=0,
    UseLogAxis=0,
)

# hide data in view
Hide(surfaceNormals1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'U_n'
u_nPWF = GetOpacityTransferFunction('U_n')
u_nPWF.Set(
    Points=[-0.07564295083284378, 0.0, 0.5, 0.0, 0.1788800060749054, 1.0, 0.5, 0.0],
    AllowDuplicateScalars=1,
    UseLogScale=0,
    ScalarRangeInitialized=1,
)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.Set(
    AttributeType='Point Data',
    CoordinateResults=0,
    ResultNormals=0,
    ResultTCoords=0,
    ResultArrayName='Result',
    Function='',
    ReplaceInvalidResults=1,
    ReplacementValue=0.0,
    ResultArrayType='Double',
)

# Properties modified on calculator2
calculator2.Set(
    ResultArrayName='U_n_pos',
    Function='0.5*(U_n+abs(U_n))',
)

# show data in view
calculator2Display = Show(calculator2, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'U_n_pos'
u_n_posTF2D = GetTransferFunction2D('U_n_pos')
u_n_posTF2D.Set(
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    Boxes=[],
    ScalarRangeInitialized=0,
    Range=[0.0, 1.0, 0.0, 1.0],
    OutputDimensions=[10, 10],
)

# get color transfer function/color map for 'U_n_pos'
u_n_posLUT = GetColorTransferFunction('U_n_pos')
u_n_posLUT.Set(
    InterpretValuesAsCategories=0,
    AnnotationsInitialized=0,
    ShowCategoricalColorsinDataRangeOnly=0,
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    RescaleOnVisibilityChange=0,
    TransferFunction2D=u_n_posTF2D,
    RGBPoints=GenerateRGBPoints(
        range_min=0.0,
        range_max=0.1788800060749054,
    ),
    UseLogScale=0,
    UseOpacityControlPointsFreehandDrawing=0,
    ShowDataHistogram=0,
    AutomaticDataHistogramComputation=0,
    DataHistogramNumberOfBins=10,
    ColorSpace='Lab',
    UseBelowRangeColor=0,
    BelowRangeColor=[0.0, 0.0, 0.0],
    UseAboveRangeColor=0,
    AboveRangeColor=[0.5, 0.5, 0.5],
    NanColor=[0.0, 1.0, 0.0],
    NanOpacity=1.0,
    Discretize=1,
    NumberOfTableValues=256,
    ScalarRangeInitialized=1.0,
    HSVWrap=0,
    VectorComponent=0,
    VectorMode='Magnitude',
    AllowDuplicateScalars=1,
    Annotations=[],
    ActiveAnnotatedValues=[],
    IndexedColors=[],
    IndexedOpacities=[],
    EnableOpacityMapping=0,
)

# trace defaults for the display properties.
calculator2Display.Set(
    Selection=None,
    Representation='Surface',
    ColorArrayName=['POINTS', 'U_n_pos'],
    LookupTable=u_n_posLUT,
    MapScalars=1,
    MultiComponentsMapping=0,
    InterpolateScalarsBeforeMapping=1,
    UseNanColorForMissingArrays=0,
    Opacity=1.0,
    PointSize=2.0,
    LineWidth=1.0,
    RenderLinesAsTubes=0,
    RenderPointsAsSpheres=0,
    DisableLighting=0,
    Diffuse=1.0,
    Interpolation='Gouraud',
    Specular=0.0,
    SpecularColor=[1.0, 1.0, 1.0],
    SpecularPower=100.0,
    Luminosity=0.0,
    Ambient=0.0,
    Roughness=0.3,
    Metallic=0.0,
    EdgeTint=[1.0, 1.0, 1.0],
    Anisotropy=0.0,
    AnisotropyRotation=0.0,
    BaseIOR=1.5,
    CoatStrength=0.0,
    CoatIOR=2.0,
    CoatRoughness=0.0,
    CoatColor=[1.0, 1.0, 1.0],
    SelectNormalArray='Normals',
    SelectTangentArray='None',
    ComputePointNormals=0,
    Splitting=1,
    FeatureAngle=30.0,
    SelectTCoordArray='None',
    Texture=None,
    RepeatTextures=1,
    InterpolateTextures=0,
    SeamlessU=0,
    SeamlessV=0,
    UseMipmapTextures=0,
    ShowTexturesOnBackface=1,
    BaseColorTexture=None,
    NormalTexture=None,
    NormalScale=1.0,
    CoatNormalTexture=None,
    CoatNormalScale=1.0,
    MaterialTexture=None,
    OcclusionStrength=1.0,
    AnisotropyTexture=None,
    EmissiveTexture=None,
    EmissiveFactor=[1.0, 1.0, 1.0],
    TextureTransform='Transform2',
    EdgeOpacity=1.0,
    BackfaceRepresentation='Follow Frontface',
    BackfaceAmbientColor=[1.0, 1.0, 1.0],
    BackfaceOpacity=1.0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    Origin=[0.0, 0.0, 0.0],
    CoordinateShiftScaleMethod='Always Auto Shift Scale',
    CoordinateSystem='Navigable',
    Pickable=1,
    Triangulate=0,
    UseShaderReplacements=0,
    ShaderReplacements='',
    NonlinearSubdivisionLevel=1,
    MatchBoundariesIgnoringCellOrder=0,
    UseDataPartitions=0,
    OSPRayUseScaleArray='All Approximate',
    OSPRayScaleArray='U_n_pos',
    OSPRayScaleFunction='Piecewise Function',
    OSPRayMaterial='None',
    Assembly='Hierarchy',
    SelectedBlockSelectors=[''],
    BlockSelectors=['/'],
    BlockColors=[],
    BlockColorArrayNames=[],
    BlockLookupTables=[],
    BlockUseSeparateColorMaps=[],
    BlockMapScalars=[],
    BlockInterpolateScalarsBeforeMappings=[],
    BlockOpacities=[],
    BlockMapScalarsGUI=1,
    BlockInterpolateScalarsBeforeMappingsGUI=1,
    BlockOpacitiesGUI=1.0,
    Orient=0,
    OrientationMode='Direction',
    SelectOrientationVectors='U',
    Scaling=0,
    ScaleMode='No Data Scaling Off',
    ScaleFactor=0.0014999999664723875,
    SelectScaleArray='U_n_pos',
    GlyphType='Arrow',
    UseGlyphTable=0,
    GlyphTableIndexArray='U_n_pos',
    UseCompositeGlyphTable=0,
    UseGlyphCullingAndLOD=0,
    LODValues=[],
    ColorByLODIndex=0,
    GaussianRadius=7.499999832361936e-05,
    ShaderPreset='Sphere',
    CustomTriangleScale=3,
    Emissive=0,
    ScaleByArray=0,
    SetScaleArray=['POINTS', 'U_n_pos'],
    ScaleArrayComponent='',
    UseScaleFunction=1,
    ScaleTransferFunction='Piecewise Function',
    OpacityByArray=0,
    OpacityArray=['POINTS', 'U_n_pos'],
    OpacityArrayComponent='',
    OpacityTransferFunction='Piecewise Function',
    DataAxesGrid='Grid Axes Representation',
    SelectionCellLabelBold=0,
    SelectionCellLabelColor=[0.0, 1.0, 0.0],
    SelectionCellLabelFontFamily='Arial',
    SelectionCellLabelFontFile='',
    SelectionCellLabelFontSize=18,
    SelectionCellLabelItalic=0,
    SelectionCellLabelJustification='Left',
    SelectionCellLabelOpacity=1.0,
    SelectionCellLabelShadow=0,
    SelectionPointLabelBold=0,
    SelectionPointLabelColor=[1.0, 1.0, 0.0],
    SelectionPointLabelFontFamily='Arial',
    SelectionPointLabelFontFile='',
    SelectionPointLabelFontSize=18,
    SelectionPointLabelItalic=0,
    SelectionPointLabelJustification='Left',
    SelectionPointLabelOpacity=1.0,
    SelectionPointLabelShadow=0,
    PolarAxes='Polar Axes Representation',
    SelectInputVectors=['POINTS', 'U'],
    NumberOfSteps=40,
    StepSize=0.25,
    NormalizeVectors=1,
    EnhancedLIC=1,
    ColorMode='Blend',
    LICIntensity=0.8,
    MapModeBias=0.0,
    EnhanceContrast='Off',
    LowLICContrastEnhancementFactor=0.0,
    HighLICContrastEnhancementFactor=0.0,
    LowColorContrastEnhancementFactor=0.0,
    HighColorContrastEnhancementFactor=0.0,
    AntiAlias=0,
    MaskOnSurface=1,
    MaskThreshold=0.0,
    MaskIntensity=0.0,
    MaskColor=[0.5, 0.5, 0.5],
    GenerateNoiseTexture=0,
    NoiseType='Gaussian',
    NoiseTextureSize=128,
    NoiseGrainSize=2,
    MinNoiseValue=0.0,
    MaxNoiseValue=0.8,
    NumberOfNoiseLevels=1024,
    ImpulseNoiseProbability=1.0,
    ImpulseNoiseBackgroundValue=0.0,
    NoiseGeneratorSeed=1,
    CompositeStrategy='AUTO',
    UseLICForLOD=0,
    WriteLog='',
    CustomShader=""" // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
""",
)

# init the 'Transform2' selected for 'TextureTransform'
calculator2Display.TextureTransform.Set(
    Translate=[0.0, 0.0, 0.0],
    Rotate=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
calculator2Display.OSPRayScaleFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Arrow' selected for 'GlyphType'
calculator2Display.GlyphType.Set(
    TipResolution=6,
    TipRadius=0.1,
    TipLength=0.35,
    ShaftResolution=6,
    ShaftRadius=0.03,
    Invert=0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator2Display.ScaleTransferFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 0.1788800060749054, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator2Display.OpacityTransferFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 0.1788800060749054, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
calculator2Display.DataAxesGrid.Set(
    XTitle='X Axis',
    YTitle='Y Axis',
    ZTitle='Z Axis',
    XTitleFontFamily='Arial',
    XTitleFontFile='',
    XTitleBold=0,
    XTitleItalic=0,
    XTitleFontSize=12,
    XTitleShadow=0,
    XTitleOpacity=1.0,
    YTitleFontFamily='Arial',
    YTitleFontFile='',
    YTitleBold=0,
    YTitleItalic=0,
    YTitleFontSize=12,
    YTitleShadow=0,
    YTitleOpacity=1.0,
    ZTitleFontFamily='Arial',
    ZTitleFontFile='',
    ZTitleBold=0,
    ZTitleItalic=0,
    ZTitleFontSize=12,
    ZTitleShadow=0,
    ZTitleOpacity=1.0,
    FacesToRender=63,
    CullBackface=0,
    CullFrontface=1,
    ShowGrid=0,
    ShowEdges=1,
    ShowTicks=1,
    LabelUniqueEdgesOnly=1,
    AxesToLabel=63,
    XLabelFontFamily='Arial',
    XLabelFontFile='',
    XLabelBold=0,
    XLabelItalic=0,
    XLabelFontSize=12,
    XLabelShadow=0,
    XLabelOpacity=1.0,
    YLabelFontFamily='Arial',
    YLabelFontFile='',
    YLabelBold=0,
    YLabelItalic=0,
    YLabelFontSize=12,
    YLabelShadow=0,
    YLabelOpacity=1.0,
    ZLabelFontFamily='Arial',
    ZLabelFontFile='',
    ZLabelBold=0,
    ZLabelItalic=0,
    ZLabelFontSize=12,
    ZLabelShadow=0,
    ZLabelOpacity=1.0,
    XAxisNotation='Mixed',
    XAxisPrecision=2,
    XAxisUseCustomLabels=0,
    XAxisLabels=[],
    YAxisNotation='Mixed',
    YAxisPrecision=2,
    YAxisUseCustomLabels=0,
    YAxisLabels=[],
    ZAxisNotation='Mixed',
    ZAxisPrecision=2,
    ZAxisUseCustomLabels=0,
    ZAxisLabels=[],
    UseCustomBounds=0,
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
)

# init the 'Polar Axes Representation' selected for 'PolarAxes'
calculator2Display.PolarAxes.Set(
    Visibility=0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    EnableCustomBounds=[0, 0, 0],
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
    EnableCustomRange=0,
    CustomRange=[0.0, 1.0],
    AutoPole=1,
    PolarAxisVisibility=1,
    RadialAxesVisibility=1,
    DrawRadialGridlines=1,
    PolarArcsVisibility=1,
    DrawPolarArcsGridlines=1,
    NumberOfRadialAxes=0,
    DeltaAngleRadialAxes=45.0,
    NumberOfArcs=5,
    DeltaRangeArcs=0.0,
    CustomMinRadius=1,
    MinimumRadius=0.0,
    CustomMaxRadius=0,
    MaximumRadius=1.0,
    CustomAngles=1,
    MinimumAngle=0.0,
    MaximumAngle=90.0,
    RadialAxesOriginToPolarAxis=1,
    PolarArcResolutionPerDegree=0.2,
    Ratio=1.0,
    EnableOverallColor=1,
    OverallColor=[1.0, 1.0, 1.0],
    PolarAxisColor=[1.0, 1.0, 1.0],
    PolarArcsColor=[1.0, 1.0, 1.0],
    LastRadialAxisColor=[1.0, 1.0, 1.0],
    SecondaryPolarArcsColor=[1.0, 1.0, 1.0],
    SecondaryRadialAxesColor=[1.0, 1.0, 1.0],
    PolarAxisTitleVisibility=1,
    PolarAxisTitle='Radial Distance',
    PolarAxisTitleLocation='Bottom',
    PolarTitleOffset=[20.0, 20.0],
    PolarLabelVisibility=1,
    PolarLabelFormat='%-#6.3g',
    PolarLabelExponentLocation='Labels',
    PolarLabelOffset=10.0,
    PolarExponentOffset=5.0,
    RadialLabelVisibility=1,
    RadialLabelFormat='%-#3.1f',
    RadialLabelLocation='Bottom',
    RadialLabelOffset=[20.0, 0.0],
    RadialUnitsVisibility=1,
    ScreenSize=10.0,
    PolarAxisTitleOpacity=1.0,
    PolarAxisTitleFontFamily='Arial',
    PolarAxisTitleFontFile='',
    PolarAxisTitleBold=0,
    PolarAxisTitleItalic=0,
    PolarAxisTitleShadow=0,
    PolarAxisTitleFontSize=12,
    PolarAxisLabelOpacity=1.0,
    PolarAxisLabelFontFamily='Arial',
    PolarAxisLabelFontFile='',
    PolarAxisLabelBold=0,
    PolarAxisLabelItalic=0,
    PolarAxisLabelShadow=0,
    PolarAxisLabelFontSize=12,
    LastRadialAxisTextOpacity=1.0,
    LastRadialAxisTextFontFamily='Arial',
    LastRadialAxisTextFontFile='',
    LastRadialAxisTextBold=0,
    LastRadialAxisTextItalic=0,
    LastRadialAxisTextShadow=0,
    LastRadialAxisTextFontSize=12,
    SecondaryRadialAxesTextOpacity=1.0,
    SecondaryRadialAxesTextFontFamily='Arial',
    SecondaryRadialAxesTextFontFile='',
    SecondaryRadialAxesTextBold=0,
    SecondaryRadialAxesTextItalic=0,
    SecondaryRadialAxesTextShadow=0,
    SecondaryRadialAxesTextFontSize=12,
    EnableDistanceLOD=1,
    DistanceLODThreshold=0.7,
    EnableViewAngleLOD=1,
    ViewAngleLODThreshold=0.7,
    SmallestVisiblePolarAngle=0.5,
    AllTicksVisibility=1,
    ArcTicksOriginToPolarAxis=1,
    TickLocation='Both',
    AxisTickVisibility=1,
    AxisMinorTickVisibility=0,
    AxisTickMatchesPolarAxes=1,
    DeltaRangeMajor=1.0,
    DeltaRangeMinor=0.5,
    ArcTickVisibility=1,
    ArcMinorTickVisibility=0,
    ArcTickMatchesRadialAxes=1,
    DeltaAngleMajor=10.0,
    DeltaAngleMinor=5.0,
    TickRatioRadiusSize=0.02,
    PolarAxisMajorTickSize=0.0,
    PolarAxisTickRatioSize=0.3,
    PolarAxisMajorTickThickness=1.0,
    PolarAxisTickRatioThickness=0.5,
    LastRadialAxisMajorTickSize=0.0,
    LastRadialAxisTickRatioSize=0.3,
    LastRadialAxisMajorTickThickness=1.0,
    LastRadialAxisTickRatioThickness=0.5,
    ArcMajorTickSize=0.0,
    ArcTickRatioSize=0.3,
    ArcMajorTickThickness=1.0,
    ArcTickRatioThickness=0.5,
    Use2DMode=0,
    UseLogAxis=0,
)

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'U_n_pos'
u_n_posPWF = GetOpacityTransferFunction('U_n_pos')
u_n_posPWF.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 0.1788800060749054, 1.0, 0.5, 0.0],
    AllowDuplicateScalars=1,
    UseLogScale=0,
    ScalarRangeInitialized=1,
)

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.Set(
    AttributeType='Point Data',
    CoordinateResults=0,
    ResultNormals=0,
    ResultTCoords=0,
    ResultArrayName='Result',
    Function='',
    ReplaceInvalidResults=1,
    ReplacementValue=0.0,
    ResultArrayType='Double',
)

# Properties modified on calculator3
calculator3.Set(
    ResultArrayName='c_flux',
    Function='c*U_n_pos',
)

# show data in view
calculator3Display = Show(calculator3, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'c_flux'
c_fluxTF2D = GetTransferFunction2D('c_flux')
c_fluxTF2D.Set(
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    Boxes=[],
    ScalarRangeInitialized=0,
    Range=[0.0, 1.0, 0.0, 1.0],
    OutputDimensions=[10, 10],
)

# get color transfer function/color map for 'c_flux'
c_fluxLUT = GetColorTransferFunction('c_flux')
c_fluxLUT.Set(
    InterpretValuesAsCategories=0,
    AnnotationsInitialized=0,
    ShowCategoricalColorsinDataRangeOnly=0,
    AutomaticRescaleRangeMode="Grow and update on 'Apply'",
    RescaleOnVisibilityChange=0,
    TransferFunction2D=c_fluxTF2D,
    RGBPoints=GenerateRGBPoints(
        range_min=0.0,
        range_max=0.07936682243946969,
    ),
    UseLogScale=0,
    UseOpacityControlPointsFreehandDrawing=0,
    ShowDataHistogram=0,
    AutomaticDataHistogramComputation=0,
    DataHistogramNumberOfBins=10,
    ColorSpace='Lab',
    UseBelowRangeColor=0,
    BelowRangeColor=[0.0, 0.0, 0.0],
    UseAboveRangeColor=0,
    AboveRangeColor=[0.5, 0.5, 0.5],
    NanColor=[0.0, 1.0, 0.0],
    NanOpacity=1.0,
    Discretize=1,
    NumberOfTableValues=256,
    ScalarRangeInitialized=1.0,
    HSVWrap=0,
    VectorComponent=0,
    VectorMode='Magnitude',
    AllowDuplicateScalars=1,
    Annotations=[],
    ActiveAnnotatedValues=[],
    IndexedColors=[],
    IndexedOpacities=[],
    EnableOpacityMapping=0,
)

# trace defaults for the display properties.
calculator3Display.Set(
    Selection=None,
    Representation='Surface',
    ColorArrayName=['POINTS', 'c_flux'],
    LookupTable=c_fluxLUT,
    MapScalars=1,
    MultiComponentsMapping=0,
    InterpolateScalarsBeforeMapping=1,
    UseNanColorForMissingArrays=0,
    Opacity=1.0,
    PointSize=2.0,
    LineWidth=1.0,
    RenderLinesAsTubes=0,
    RenderPointsAsSpheres=0,
    DisableLighting=0,
    Diffuse=1.0,
    Interpolation='Gouraud',
    Specular=0.0,
    SpecularColor=[1.0, 1.0, 1.0],
    SpecularPower=100.0,
    Luminosity=0.0,
    Ambient=0.0,
    Roughness=0.3,
    Metallic=0.0,
    EdgeTint=[1.0, 1.0, 1.0],
    Anisotropy=0.0,
    AnisotropyRotation=0.0,
    BaseIOR=1.5,
    CoatStrength=0.0,
    CoatIOR=2.0,
    CoatRoughness=0.0,
    CoatColor=[1.0, 1.0, 1.0],
    SelectNormalArray='Normals',
    SelectTangentArray='None',
    ComputePointNormals=0,
    Splitting=1,
    FeatureAngle=30.0,
    SelectTCoordArray='None',
    Texture=None,
    RepeatTextures=1,
    InterpolateTextures=0,
    SeamlessU=0,
    SeamlessV=0,
    UseMipmapTextures=0,
    ShowTexturesOnBackface=1,
    BaseColorTexture=None,
    NormalTexture=None,
    NormalScale=1.0,
    CoatNormalTexture=None,
    CoatNormalScale=1.0,
    MaterialTexture=None,
    OcclusionStrength=1.0,
    AnisotropyTexture=None,
    EmissiveTexture=None,
    EmissiveFactor=[1.0, 1.0, 1.0],
    TextureTransform='Transform2',
    EdgeOpacity=1.0,
    BackfaceRepresentation='Follow Frontface',
    BackfaceAmbientColor=[1.0, 1.0, 1.0],
    BackfaceOpacity=1.0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    Origin=[0.0, 0.0, 0.0],
    CoordinateShiftScaleMethod='Always Auto Shift Scale',
    CoordinateSystem='Navigable',
    Pickable=1,
    Triangulate=0,
    UseShaderReplacements=0,
    ShaderReplacements='',
    NonlinearSubdivisionLevel=1,
    MatchBoundariesIgnoringCellOrder=0,
    UseDataPartitions=0,
    OSPRayUseScaleArray='All Approximate',
    OSPRayScaleArray='c_flux',
    OSPRayScaleFunction='Piecewise Function',
    OSPRayMaterial='None',
    Assembly='Hierarchy',
    SelectedBlockSelectors=[''],
    BlockSelectors=['/'],
    BlockColors=[],
    BlockColorArrayNames=[],
    BlockLookupTables=[],
    BlockUseSeparateColorMaps=[],
    BlockMapScalars=[],
    BlockInterpolateScalarsBeforeMappings=[],
    BlockOpacities=[],
    BlockMapScalarsGUI=1,
    BlockInterpolateScalarsBeforeMappingsGUI=1,
    BlockOpacitiesGUI=1.0,
    Orient=0,
    OrientationMode='Direction',
    SelectOrientationVectors='U',
    Scaling=0,
    ScaleMode='No Data Scaling Off',
    ScaleFactor=0.0014999999664723875,
    SelectScaleArray='c_flux',
    GlyphType='Arrow',
    UseGlyphTable=0,
    GlyphTableIndexArray='c_flux',
    UseCompositeGlyphTable=0,
    UseGlyphCullingAndLOD=0,
    LODValues=[],
    ColorByLODIndex=0,
    GaussianRadius=7.499999832361936e-05,
    ShaderPreset='Sphere',
    CustomTriangleScale=3,
    Emissive=0,
    ScaleByArray=0,
    SetScaleArray=['POINTS', 'c_flux'],
    ScaleArrayComponent='',
    UseScaleFunction=1,
    ScaleTransferFunction='Piecewise Function',
    OpacityByArray=0,
    OpacityArray=['POINTS', 'c_flux'],
    OpacityArrayComponent='',
    OpacityTransferFunction='Piecewise Function',
    DataAxesGrid='Grid Axes Representation',
    SelectionCellLabelBold=0,
    SelectionCellLabelColor=[0.0, 1.0, 0.0],
    SelectionCellLabelFontFamily='Arial',
    SelectionCellLabelFontFile='',
    SelectionCellLabelFontSize=18,
    SelectionCellLabelItalic=0,
    SelectionCellLabelJustification='Left',
    SelectionCellLabelOpacity=1.0,
    SelectionCellLabelShadow=0,
    SelectionPointLabelBold=0,
    SelectionPointLabelColor=[1.0, 1.0, 0.0],
    SelectionPointLabelFontFamily='Arial',
    SelectionPointLabelFontFile='',
    SelectionPointLabelFontSize=18,
    SelectionPointLabelItalic=0,
    SelectionPointLabelJustification='Left',
    SelectionPointLabelOpacity=1.0,
    SelectionPointLabelShadow=0,
    PolarAxes='Polar Axes Representation',
    SelectInputVectors=['POINTS', 'U'],
    NumberOfSteps=40,
    StepSize=0.25,
    NormalizeVectors=1,
    EnhancedLIC=1,
    ColorMode='Blend',
    LICIntensity=0.8,
    MapModeBias=0.0,
    EnhanceContrast='Off',
    LowLICContrastEnhancementFactor=0.0,
    HighLICContrastEnhancementFactor=0.0,
    LowColorContrastEnhancementFactor=0.0,
    HighColorContrastEnhancementFactor=0.0,
    AntiAlias=0,
    MaskOnSurface=1,
    MaskThreshold=0.0,
    MaskIntensity=0.0,
    MaskColor=[0.5, 0.5, 0.5],
    GenerateNoiseTexture=0,
    NoiseType='Gaussian',
    NoiseTextureSize=128,
    NoiseGrainSize=2,
    MinNoiseValue=0.0,
    MaxNoiseValue=0.8,
    NumberOfNoiseLevels=1024,
    ImpulseNoiseProbability=1.0,
    ImpulseNoiseBackgroundValue=0.0,
    NoiseGeneratorSeed=1,
    CompositeStrategy='AUTO',
    UseLICForLOD=0,
    WriteLog='',
    CustomShader=""" // This custom shader code define a gaussian blur
 // Please take a look into vtkSMPointGaussianRepresentation.cxx
 // for other custom shader examples
 //VTK::Color::Impl
   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);
   float gaussian = exp(-0.5*dist2);
   opacity = opacity*gaussian;
""",
)

# init the 'Transform2' selected for 'TextureTransform'
calculator3Display.TextureTransform.Set(
    Translate=[0.0, 0.0, 0.0],
    Rotate=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
)

# init the 'Piecewise Function' selected for 'OSPRayScaleFunction'
calculator3Display.OSPRayScaleFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Arrow' selected for 'GlyphType'
calculator3Display.GlyphType.Set(
    TipResolution=6,
    TipRadius=0.1,
    TipLength=0.35,
    ShaftResolution=6,
    ShaftRadius=0.03,
    Invert=0,
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
calculator3Display.ScaleTransferFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 0.07936682243946969, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
calculator3Display.OpacityTransferFunction.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 0.07936682243946969, 1.0, 0.5, 0.0],
    UseLogScale=0,
)

# init the 'Grid Axes Representation' selected for 'DataAxesGrid'
calculator3Display.DataAxesGrid.Set(
    XTitle='X Axis',
    YTitle='Y Axis',
    ZTitle='Z Axis',
    XTitleFontFamily='Arial',
    XTitleFontFile='',
    XTitleBold=0,
    XTitleItalic=0,
    XTitleFontSize=12,
    XTitleShadow=0,
    XTitleOpacity=1.0,
    YTitleFontFamily='Arial',
    YTitleFontFile='',
    YTitleBold=0,
    YTitleItalic=0,
    YTitleFontSize=12,
    YTitleShadow=0,
    YTitleOpacity=1.0,
    ZTitleFontFamily='Arial',
    ZTitleFontFile='',
    ZTitleBold=0,
    ZTitleItalic=0,
    ZTitleFontSize=12,
    ZTitleShadow=0,
    ZTitleOpacity=1.0,
    FacesToRender=63,
    CullBackface=0,
    CullFrontface=1,
    ShowGrid=0,
    ShowEdges=1,
    ShowTicks=1,
    LabelUniqueEdgesOnly=1,
    AxesToLabel=63,
    XLabelFontFamily='Arial',
    XLabelFontFile='',
    XLabelBold=0,
    XLabelItalic=0,
    XLabelFontSize=12,
    XLabelShadow=0,
    XLabelOpacity=1.0,
    YLabelFontFamily='Arial',
    YLabelFontFile='',
    YLabelBold=0,
    YLabelItalic=0,
    YLabelFontSize=12,
    YLabelShadow=0,
    YLabelOpacity=1.0,
    ZLabelFontFamily='Arial',
    ZLabelFontFile='',
    ZLabelBold=0,
    ZLabelItalic=0,
    ZLabelFontSize=12,
    ZLabelShadow=0,
    ZLabelOpacity=1.0,
    XAxisNotation='Mixed',
    XAxisPrecision=2,
    XAxisUseCustomLabels=0,
    XAxisLabels=[],
    YAxisNotation='Mixed',
    YAxisPrecision=2,
    YAxisUseCustomLabels=0,
    YAxisLabels=[],
    ZAxisNotation='Mixed',
    ZAxisPrecision=2,
    ZAxisUseCustomLabels=0,
    ZAxisLabels=[],
    UseCustomBounds=0,
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
)

# init the 'Polar Axes Representation' selected for 'PolarAxes'
calculator3Display.PolarAxes.Set(
    Visibility=0,
    Translation=[0.0, 0.0, 0.0],
    Scale=[1.0, 1.0, 1.0],
    Orientation=[0.0, 0.0, 0.0],
    EnableCustomBounds=[0, 0, 0],
    CustomBounds=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
    EnableCustomRange=0,
    CustomRange=[0.0, 1.0],
    AutoPole=1,
    PolarAxisVisibility=1,
    RadialAxesVisibility=1,
    DrawRadialGridlines=1,
    PolarArcsVisibility=1,
    DrawPolarArcsGridlines=1,
    NumberOfRadialAxes=0,
    DeltaAngleRadialAxes=45.0,
    NumberOfArcs=5,
    DeltaRangeArcs=0.0,
    CustomMinRadius=1,
    MinimumRadius=0.0,
    CustomMaxRadius=0,
    MaximumRadius=1.0,
    CustomAngles=1,
    MinimumAngle=0.0,
    MaximumAngle=90.0,
    RadialAxesOriginToPolarAxis=1,
    PolarArcResolutionPerDegree=0.2,
    Ratio=1.0,
    EnableOverallColor=1,
    OverallColor=[1.0, 1.0, 1.0],
    PolarAxisColor=[1.0, 1.0, 1.0],
    PolarArcsColor=[1.0, 1.0, 1.0],
    LastRadialAxisColor=[1.0, 1.0, 1.0],
    SecondaryPolarArcsColor=[1.0, 1.0, 1.0],
    SecondaryRadialAxesColor=[1.0, 1.0, 1.0],
    PolarAxisTitleVisibility=1,
    PolarAxisTitle='Radial Distance',
    PolarAxisTitleLocation='Bottom',
    PolarTitleOffset=[20.0, 20.0],
    PolarLabelVisibility=1,
    PolarLabelFormat='%-#6.3g',
    PolarLabelExponentLocation='Labels',
    PolarLabelOffset=10.0,
    PolarExponentOffset=5.0,
    RadialLabelVisibility=1,
    RadialLabelFormat='%-#3.1f',
    RadialLabelLocation='Bottom',
    RadialLabelOffset=[20.0, 0.0],
    RadialUnitsVisibility=1,
    ScreenSize=10.0,
    PolarAxisTitleOpacity=1.0,
    PolarAxisTitleFontFamily='Arial',
    PolarAxisTitleFontFile='',
    PolarAxisTitleBold=0,
    PolarAxisTitleItalic=0,
    PolarAxisTitleShadow=0,
    PolarAxisTitleFontSize=12,
    PolarAxisLabelOpacity=1.0,
    PolarAxisLabelFontFamily='Arial',
    PolarAxisLabelFontFile='',
    PolarAxisLabelBold=0,
    PolarAxisLabelItalic=0,
    PolarAxisLabelShadow=0,
    PolarAxisLabelFontSize=12,
    LastRadialAxisTextOpacity=1.0,
    LastRadialAxisTextFontFamily='Arial',
    LastRadialAxisTextFontFile='',
    LastRadialAxisTextBold=0,
    LastRadialAxisTextItalic=0,
    LastRadialAxisTextShadow=0,
    LastRadialAxisTextFontSize=12,
    SecondaryRadialAxesTextOpacity=1.0,
    SecondaryRadialAxesTextFontFamily='Arial',
    SecondaryRadialAxesTextFontFile='',
    SecondaryRadialAxesTextBold=0,
    SecondaryRadialAxesTextItalic=0,
    SecondaryRadialAxesTextShadow=0,
    SecondaryRadialAxesTextFontSize=12,
    EnableDistanceLOD=1,
    DistanceLODThreshold=0.7,
    EnableViewAngleLOD=1,
    ViewAngleLODThreshold=0.7,
    SmallestVisiblePolarAngle=0.5,
    AllTicksVisibility=1,
    ArcTicksOriginToPolarAxis=1,
    TickLocation='Both',
    AxisTickVisibility=1,
    AxisMinorTickVisibility=0,
    AxisTickMatchesPolarAxes=1,
    DeltaRangeMajor=1.0,
    DeltaRangeMinor=0.5,
    ArcTickVisibility=1,
    ArcMinorTickVisibility=0,
    ArcTickMatchesRadialAxes=1,
    DeltaAngleMajor=10.0,
    DeltaAngleMinor=5.0,
    TickRatioRadiusSize=0.02,
    PolarAxisMajorTickSize=0.0,
    PolarAxisTickRatioSize=0.3,
    PolarAxisMajorTickThickness=1.0,
    PolarAxisTickRatioThickness=0.5,
    LastRadialAxisMajorTickSize=0.0,
    LastRadialAxisTickRatioSize=0.3,
    LastRadialAxisMajorTickThickness=1.0,
    LastRadialAxisTickRatioThickness=0.5,
    ArcMajorTickSize=0.0,
    ArcTickRatioSize=0.3,
    ArcMajorTickThickness=1.0,
    ArcTickRatioThickness=0.5,
    Use2DMode=0,
    UseLogAxis=0,
)

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'c_flux'
c_fluxPWF = GetOpacityTransferFunction('c_flux')
c_fluxPWF.Set(
    Points=[0.0, 0.0, 0.5, 0.0, 0.07936682243946969, 1.0, 0.5, 0.0],
    AllowDuplicateScalars=1,
    UseLogScale=0,
    ScalarRangeInitialized=1,
)

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.Set(
    AttributeType='Point Data',
    CoordinateResults=0,
    ResultNormals=0,
    ResultTCoords=0,
    ResultArrayName='Result',
    Function='',
    ReplaceInvalidResults=1,
    ReplacementValue=0.0,
    ResultArrayType='Double',
)

# set active source
SetActiveSource(calculator3)

# destroy calculator4
Delete(calculator4)
del calculator4

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=calculator3)
integrateVariables1.Set(
    IntegrationStrategy='Linear Strategy',
    DivideCellDataByVolume=0,
)

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.Set(
    UseCache=0,
    ViewSize=[400, 400],
    CellFontSize=9,
    HeaderFontSize=9,
    SelectionOnly=0,
    GenerateCellConnectivity=0,
    ShowFieldData=0,
    ColumnToSort='',
    InvertOrder=0,
    BlockSize=1024,
    HiddenColumnLabels=['Block Number'],
    FieldAssociation='Point Data',
)

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
integrateVariables1Display.Set(
    Assembly='',
    BlockVisibilities=[],
)

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=integrateVariables1)
calculator4.Set(
    AttributeType='Point Data',
    CoordinateResults=0,
    ResultNormals=0,
    ResultTCoords=0,
    ResultArrayName='Result',
    Function='',
    ReplaceInvalidResults=1,
    ReplacementValue=0.0,
    ResultArrayType='Double',
)

# Properties modified on calculator4
calculator4.Set(
    ResultArrayName='Active Flow Percentage%',
    Function='(c_flux/U_n_pos)*100',
)

# show data in view
calculator4Display = Show(calculator4, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
calculator4Display.Set(
    Assembly='',
    BlockVisibilities=[],
)

# hide data in view
Hide(integrateVariables1, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

SelectIDs(IDs=[-1, 0], FieldType=1, ContainingCells=0)

# set active source
SetActiveSource(calculator4)

SelectIDs(IDs=[-1, 0], FieldType=1, ContainingCells=0)

SelectIDs(IDs=[-1, 0], FieldType=1, ContainingCells=0)

SelectIDs(IDs=[-1, 0], FieldType=1, ContainingCells=0)

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = []

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'Active Flow Percentage%', 'c', 'c_Bot_P1_L', 'c_Bot_P1_R', 'c_Bot_P2_L', 'c_Bot_P2_R', 'c_Bot_P3_L', 'c_Bot_P3_R', 'c_Bot_P4_L', 'c_Bot_P4_R', 'c_flux', 'c_Top_P1_L', 'c_Top_P1_R', 'c_Top_P2_L', 'c_Top_P2_R', 'c_Top_P3_L', 'c_Top_P3_R', 'c_Top_P4_L', 'c_Top_P4_R', 'F', 'F_Magnitude', 'Normals', 'Normals_Magnitude', 'p', 'plasmaIndicator', 'Points', 'Points_Magnitude', 'Sc', 'tau', 'tau_Bot_P1_L', 'tau_Bot_P1_R', 'tau_Bot_P2_L', 'tau_Bot_P2_R', 'tau_Bot_P3_L', 'tau_Bot_P3_R', 'tau_Bot_P4_L', 'tau_Bot_P4_R', 'tau_Top_P1_L', 'tau_Top_P1_R', 'tau_Top_P2_L', 'tau_Top_P2_R', 'tau_Top_P3_L', 'tau_Top_P3_R', 'tau_Top_P4_L', 'tau_Top_P4_R', 'tauAvg', 'U', 'U_Magnitude', 'U_n', 'U_n_pos', 'Block Number']

# Properties modified on spreadSheetView1
spreadSheetView1.HiddenColumnLabels = ['Point ID', 'c', 'c_Bot_P1_L', 'c_Bot_P1_R', 'c_Bot_P2_L', 'c_Bot_P2_R', 'c_Bot_P3_L', 'c_Bot_P3_R', 'c_Bot_P4_L', 'c_Bot_P4_R', 'c_flux', 'c_Top_P1_L', 'c_Top_P1_R', 'c_Top_P2_L', 'c_Top_P2_R', 'c_Top_P3_L', 'c_Top_P3_R', 'c_Top_P4_L', 'c_Top_P4_R', 'F', 'F_Magnitude', 'Normals', 'Normals_Magnitude', 'p', 'plasmaIndicator', 'Points', 'Points_Magnitude', 'Sc', 'tau', 'tau_Bot_P1_L', 'tau_Bot_P1_R', 'tau_Bot_P2_L', 'tau_Bot_P2_R', 'tau_Bot_P3_L', 'tau_Bot_P3_R', 'tau_Bot_P4_L', 'tau_Bot_P4_R', 'tau_Top_P1_L', 'tau_Top_P1_R', 'tau_Top_P2_L', 'tau_Top_P2_R', 'tau_Top_P3_L', 'tau_Top_P3_R', 'tau_Top_P4_L', 'tau_Top_P4_R', 'tauAvg', 'U', 'U_Magnitude', 'U_n', 'U_n_pos', 'Block Number']

# set active source
SetActiveSource(calculator4)

# set active source
SetActiveSource(calculator4)

# export view
ExportView('/home/saas/SAAS_Ubun/071125_saas_3/071125_saas_3_3/Active Flow Percentage.csv', view=spreadSheetView1, RealNumberNotation='Mixed',
    RealNumberPrecision=6)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1951, 1622)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.Set(
    InteractionMode='2D',
    CameraPosition=[0.10024999962188304, 0.007499999832361937, 0.0005000000237487257],
    CameraFocalPoint=[0.05000000074505806, 0.007499999832361937, 0.0005000000237487257],
    CameraViewUp=[0.0, 0.0, 1.0],
    CameraParallelScale=0.011005124371205509,
)


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/nightly/python/
##--------------------------------------------