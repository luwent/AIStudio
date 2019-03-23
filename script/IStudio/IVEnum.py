class NPDType():
    BYTE = 1
    SHORT = 3
    INT = 5
    FLOAT = 11
    DOUBLE = 12

#Vertical text aligment
class VerticalAlignment():
    VerticalAlign_Top = 0  #Align objects on top
    VerticalAlign_Center = 1 #Align objects at center
    VerticalAlign_Bottom = 2 #Align objects at bottom

#Horizontal text aligment
class HorizontalAlignment():
    HorizontalAlign_Left = 0 #Align objects on left side
    HorizontalAlign_Center = 1 #Align objects at center
    HorizontalAlign_Right = 2 #Align objects on right
    HorizontalAlign_Justify = 2 #justifying a line of text

class LocationSide():
    Location_Left = 0
    Location_Right = 1
    Location_Top = 2
    Location_Bottom = 3
    Location_TopLeft = 4
    Location_TopRight = 5
    Location_BottomLeft = 6
    Location_BottomRight = 7
    Location_Center = 8
    Location_TopCenter = 9
    Location_BottomCenter = 10

    LocationSide_Left = 0x1
    LocationSide_Right = 0x2
    LocationSide_Top = 0x4
    LocationSide_Bottom = 0x8
    LocationSide_All = 0xF

class FillType():
    FillType_None = 0
    FillType_Solid = 1
    FillType_Texture = 2
    FillType_Hatch = 3
    FillType_HoriGradient = 4
    FillType_VertGradient = 5
    FillType_FDiagonalGradient = 6
    FillType_BDiagonalGradient = 7
    FillType_RadialGradient = 8
    FillType_PathGradient = 9

class LineType():
    LineType_None = 0
    LineType_Solid = 1
    LineType_Dash = 2
    LineType_Dot = 3
    LineType_DashDot = 4
    LineType_DashDotDot = 5
    LineType_Custom = 6

    LineType_3DBeam = 10
    LineType_3DCylinder = 11

class LineCapType():
    LineCapType_Butt = 0
    LineCapType_Square = 1
    LineCapType_Round = 2
    LineCapType_Triangle = 3
    LineCapType_Arrow = 4
    LineCapType_Diamond = 5
    LineCapType_Circle = 6
    LineCapType_Custom = 7

    LineCapType_3DBox = 100
    LineCapType_3DSphere = 101
    LineCapType_3DCone = 102
    LineCapType_3DTetrahedron = 103

class IconType():
    Icon_None = 0
    Icon_DropDown = 1
    Icon_DropUp = 2
    Icon_DropDown2 = 3
    Icon_PopDown = 4
    Icon_ExpanDown = 5
    Icon_ArrowDown = 6
    Icon_ArrowUp = 7
    Icon_ArrowLeft = 8
    Icon_ArrowRight = 9
    Icon_DropLeft = 10

    Icon_DropRight = 20
    Icon_DropLeftStop = 21
    Icon_DropRightStop = 22
    Icon_DropUpStop = 23
    Icon_DropDownStop = 24
    Icon_RectCross = 25
    Icon_CrossHair = 26
    Icon_SolidCircle = 27
    Icon_MinBar = 28
    Icon_Hide = 29
    Icon_Show = 30

    Icon_Cross = 40
    Icon_Correct = 41
    Icon_Close = 42
    Icon_Star4 = 43
    Icon_Star5 = 44
    Icon_Star6 = 45
    Icon_CStar4 = 46
    Icon_CStar5 = 47
    Icon_CStar6 = 48
    Icon_Question = 49
    Icon_CQuestion = 50

    Icon_RectEmpty = 60
    Icon_RectSolid = 61
    Icon_RectDot = 62
    Icon_RectCross2 = 63
    Icon_RectPlus = 64
    Icon_RectHLine = 65
    Icon_RectVLine = 66
    Icon_RectHLFill = 67
    Icon_RectHRFill = 68
    Icon_RectVTFill = 69
    Icon_RectVBFill = 70

    Icon_CircleEmpty = 80
    Icon_CircleSolid = 81
    Icon_CircleDot = 82
    Icon_CircleCross = 83
    Icon_CirclePlus = 84
    Icon_CircleHLine = 85
    Icon_CircleVLine = 86
    Icon_CircleHLFill = 87
    Icon_CircleHRFill = 88
    Icon_CircleVTFill = 89
    Icon_CircleVBFill = 90

    Icon_UTriangleEmpty = 100
    Icon_UTriangleSolid = 101
    Icon_UTriangleDot = 102
    Icon_UTriangleCross = 103
    Icon_UTrianglePlus = 104
    Icon_UTriangleHLine = 105
    Icon_UTriangleVLine = 106
    Icon_UTriangleHLFill = 107
    Icon_UTriangleHRFill = 108
    Icon_UTriangleVTFill = 109
    Icon_UTriangleVBFill = 110

    Icon_DTriangleEmpty = 120
    Icon_DTriangleSolid = 121
    Icon_DTriangleDot = 122
    Icon_DTriangleCross = 123
    Icon_DTrianglePlus = 124
    Icon_DTriangleHLine = 125
    Icon_DTriangleVLine = 126
    Icon_DTriangleHLFill = 127
    Icon_DTriangleHRFill = 128
    Icon_DTriangleVTFill = 129
    Icon_DTriangleVBFill = 130

    Icon_LTriangleEmpty = 140
    Icon_LTriangleSolid = 141
    Icon_LTriangleDot = 142
    Icon_LTriangleCross = 143
    Icon_LTrianglePlus = 144
    Icon_LTriangleHLine = 145
    Icon_LTriangleVLine = 146
    Icon_LTriangleHLFill = 147
    Icon_LTriangleHRFill = 148
    Icon_LTriangleVTFill = 149
    Icon_LTriangleVBFill = 150

    Icon_RTriangleEmpty = 160
    Icon_RTriangleSolid = 161
    Icon_RTriangleDot = 162
    Icon_RTriangleCross = 163
    Icon_RTrianglePlus = 164
    Icon_RTriangleHLine = 165
    Icon_RTriangleVLine = 166
    Icon_RTriangleHLFill = 167
    Icon_RTriangleHRFill = 168
    Icon_RTriangleVTFill = 169
    Icon_RTriangleVBFill = 170

    Icon_DiamondEmpty = 180
    Icon_DiamondSolid = 181
    Icon_DiamondDot = 182
    Icon_DiamondCross = 183
    Icon_DiamondPlus = 184
    Icon_DiamondHLine = 185
    Icon_DiamondVLine = 186
    Icon_DiamondHLFill = 187
    Icon_DiamondHRFill = 188
    Icon_DiamondVTFill = 189
    Icon_DiamondVBFill = 190

    Icon_StarEmpty = 200
    Icon_StarSolid = 201
    Icon_StarDot = 202
    Icon_StarCross = 203
    Icon_StarPlus = 204
    Icon_StarHLine = 205
    Icon_StarVLine = 206
    Icon_StarHLFill = 207
    Icon_StarHRFill = 208
    Icon_StarVTFill = 209
    Icon_StarVBFill = 210

    Icon_Poly5Empty = 220
    Icon_Poly5Solid = 221
    Icon_Poly5Dot = 222
    Icon_Poly5Cross = 223
    Icon_Poly5Plus = 224
    Icon_Poly5HLine = 225
    Icon_Poly5VLine = 226
    Icon_Poly5HLFill = 227
    Icon_Poly5HRFill = 228
    Icon_Poly5VTFill = 229
    Icon_Poly5VBFill = 230

    Icon_Poly6Empty = 240
    Icon_Poly6Solid = 241
    Icon_Poly6Dot = 242
    Icon_Poly6Cross = 243
    Icon_Poly6Plus = 244
    Icon_Poly6HLine = 245
    Icon_Poly6VLine = 246
    Icon_Poly6HLFill = 247
    Icon_Poly6HRFill = 248
    Icon_Poly6VTFill = 249
    Icon_Poly6VBFill = 250

    Icon_3DBox = 1000
    Icon_3DSphere = 1001
    Icon_3DCone = 1002
    Icon_3DCylinder = 1003
    Icon_3DTorus = 1004
    Icon_3DDodecahedron = 1005
    Icon_3DOctahedron = 1006
    Icon_3DIcosahedron = 1007
    Icon_3DTetrahedron = 1008
    Icon_3DPie = 1009


class GraphCategory():
    XY = 0  #Graph with X-Y axes.
    Pie = 1 #Pie graph.
    Bar = 2 #Bar gGraph.
    Polar = 3  #Graph with polar axes (angle and radius) or 3-D spherical 
    Ternary = 4 #Ternary graph with triagular axes.
    Pie3D = 5  #3-D Pie graph.
    Bar3D = 6 #3-D bar graph.
    Cylindrical = 7  #Graph based on 3-D cylindical coordinates



class PlotStyle():
    #2-D style for XY graph category
    XYCurve = 0  #X-Y curves.
    XYImage = 1  #2-D image.
    XYContour = 2  #2-D contour.
    XYVector = 3  #vector plot, data are presented using a vector's position, direction and length.
    XYBubble = 4  #buble plot, data are prsented using a circle's position, size and color.
    XYScroll = 5  #Strip chart, scrolling plot

    #3-D style for XY graph category

    XYZCurve = 10  #3-D curves.
    XYZContour = 11 #3-D contour
    XYZVector = 12  #3-D vector plot, data are presented using a 3-D vector's position, direction and length.
    XYZBubble = 13  #3-D buble plot, data are prsented using a sphere's position, size and color.
    XYZUV = 14  #3-D parametric surface
    XYZSurface = 15  #3-D surface plot
    XYZTriangulation = 16  #3-D surface based on triangles
    XYZ4DVolumn = 17  #3-D volumn plot

    #Bar Style
    BarVBar = 0  #Vertical bar
    BarHBar = 1  #Horizontal bar
    BarCurve = 2  #Curve in bar plot

    #Pie Style

    PieDoughnut = 0  #Doughnut plot
    PiePie = 1  #Pie plot

    PieDoughnut3D = 10  #3-D Doughnut plot
    PiePie3D = 11 #3-D Pie plot

    #Ternary Style

    TernaryCurve = 0  #Ternary curve
    TernaryImage = 1  #Ternary image
    TernaryContour = 2  #Ternary contour

    #Polar Style

    PolarCurve = 0  #Polar curve
    PolarImage = 1  #Polar image
    PolarContour = 2  #Polar contour

    #Polar 3-D Style

    Polar3DCurve = 10  #3-D spherical curve
    Polar3DImage = 11  #3-D spherical image
    Polar3DContour = 12  #3-D spherical contour
    Polar3DSurface = 13  #3-D spherical surface
    Polar4DVolumn = 14  #4-D spherical volumn plot

    #Cylindrical 3-D Style

    Cylindrical3DCurve = 10  #3-D cylindrical curve
    Cylindrical3DImage = 11  #3-D cylindrical image
    Cylindrical3DContour = 12  #3-D cylindrical contour
    Cylindrical3DSurface = 13  #3-D cylindrical surface
    Cylindrical4DVolumn = 14  #3-D cylindrical volumn plot

class ErrBarDir():
    IVErrBarDir_None = 0  #No error bar
    IVErrBarDir_YBoth = 1  #Error bar both direction along y
    IVErrBarDir_YPos = 2  #Error bar positive direction along y
    IVErrBarDir_YNeg = 3  #Error bar negative direction along y
    IVErrBarDir_XBoth = 4  #Error bar both direction along x
    IVErrBarDir_XPos = 5  #Error bar positive direction along x
    IVErrBarDir_XNeg = 6  #Error bar negative direction along x
    IVErrBarDir_XYBoth = 7 #Error bar both direction along x and y


class ErrBarSource():
    IVErrBarSource_Per = 0  #Based on value percent
    IVErrBarSource_Fix = 1  #Based on given error value
    IVErrBarSource_SE = 2  #Based on given error value
    IVErrBarSource_STD = 3 #Based on given error value
    IVErrBarSource_User = 4 #Based on error data which are setup using SetErrorUpData, SetErrorLowData functions

class ErrBarDis():
    IVErrBarDis_Cap = 0  #Show cap
    IVErrBarDis_NoCap = 1  #No cap

class PlotOptions():
    Fill = 0x1  #For 2-D curve plot, fill the space between a curve and baseline. 

    CircularPie = 0x2  #For pie graph, show pie as circular
    PercentLabel = 0x4  #For pie graph, display percent label
    LineLabel = 0x4  #For pie graph, display line between label and its corresponding pie

    #For 3-D graph 
    ProjectXY = 0x10000  #Display X-Y project 
    ProjectXZ = 0x20000  #Display X-z project 
    ProjectYZ = 0x40000  #Display y-z project 
    Wireframe = 0x80000  #Display surface as wire frame 



class AxisOptions():
    ShowTitle = 0x1 << 0  #Shpw axis title
    LogScale = 0x1 << 1  #Using log scale
    Reversed = 0x1 << 2  #Reverse axis scale
    AutoScale = 0x1 << 3  #Automatically calculate axis scale
    AxisLine = 0x1 << 4  #Show axis line
    TickLabel = 0x1 << 5  #Show tick label
    MajorTick = 0x1 << 6  #Show major tick
    MinorTick = 0x1 << 7  #Show minor tick
    InsideTick = 0x1 << 8  #Show inside tick
    OutsideTick = 0x1 << 9  #Shpw outside tick
    AllsideTick = 0x3 << 8  #Show both inside and outside tick
    MajorGrid = 0x1 << 10  #Show major grid
    MinorGrid = 0x1 << 11  #Show minor tick
    ShowTick = 0x1 << 12  #Show tick
    ShowPeerAxisLine = 0x1 << 13  #Show peer axis axis line
    ShowPeerTick = 0x1 << 14  #Show peer axis tick
    ShowPeerLabel = 0x1 << 15  #Show peer axis label
    AutoTickNum = 0x1 << 16  #Automatically calculate tick number
    FixTickNum = 0x1 << 17  #Use fixed tick number
    Discrete = 0x1 << 18  #The axis scale is discrete
    Break = 0x1 << 19  # Show break point
    BreakLog = 0x1 << 20  #Use log scale after break point
    BreakAutoTickNum = 0x1 << 21  #Automatically calculate tick number after break point
    AutoScroll = 0x1 << 22  #Automatically scroll axis scale based on plot data
    FixPadding = 0x1 << 23  #Space around the axis is based on user-defined value (using SetTickPadding function)
    ValuePairOnly = 0x1 << 24  #Show value pair only


class AxisType():
    AxisY = 0  #Y axis on left side
    AxisY1 = 1  #Y axis on right side
    AxisX = 2  #X axis on bottom side
    AxisX1 = 3  #X axis on top side
    AxisZ = 4  #Z axis
    AxisZ1 = 5  #Z axis
    AxisArc = 6  #arc axis ( polar axis or ray) for polar graph
    AxisRadius = 7 #Radius axis (angular  axis or circular) for polar graph
    AxisTernary1 = 8  #A1 axis for ternary graph
    AxisTernary2 = 9  #A2 axis for ternary graph
    AxisTernary3 = 10  #A3 axis for ternary graph
    AxisLeft3D = 11  #Left axis for 3-D bar
    AxisBottom3D = 12  #Bottom axis for 3-D bar
    AxisLongitude = 13  #Longitude axis for 3-D spherical graph
    AxisLatidute = 14  #Latitude axis for 3-D spherical graph
    AxisPolarHeight = 15  #Height axis for 3-D spherical graph
    AxisCylindricalHeight = 16  #Height axis for 3-D cylindrical graph

class ValuePairOption():
    VPGridLine = 0x1  #Show the grid line based on value
    VPMajorTick = 0x2  #Show major tick
    VPShowName = 0x4  #Show value pair name
    VPShowValue = 0x8  #Show value pair value


class GraphObjSnapModes():
    SnapFloating = 0  #Graph objects such as cursors and annotations can be positioned freely.
    SnapNearestPoint = 1 #Graph objects such as cursors and annotations are positioned to the nearest plot point
    SnapPointsOnPlot = 2  #Graph objects such as cursors and annotations are positioned to points on a specific plot
    SnapNearestYForFixedX = 3 #Graph objects such as cursors and annotations are positioned to the y value of the nearest point on the specified plot for a fixed X location


class CursorLineShape():
    CursorNone = 0  #there is no crosshair
    CursorMinorX = 1  #the crosshair is a short horizontal line, length is based on screen pixels.
    CursorMajorX = 2  #the crosshair is a long horizontal line
    CursorMinorY = 3  #the crosshair is a short vertical line, length is based on screen pixels.
    CursorMajorY = 4  #the crosshair is a long vertical line
    CursorMajorXMajorY = 5  #the crosshair is a long horizontal line and a long vertical line.
    CursorMinorXMinorY = 6  #the crosshair is a short horizontal line and a short vertical line.
    CursorMajorXMinorY = 7  #the crosshair is a long horizontal line and a short vertical line.
    CursorMinorXMajorY = 8  #the crosshair is a short horizontal line and a long vertical line.
    CursorMinorLX = 9  #the crosshair is a short horizontal line, length is based on X axis scale.
    CursorMinorLY = 10  #the crosshair is a short vertical line, length is based on Y axis scale.
    CursorMinorLXMinorLY = 11  #the crosshair is a short horizontal line and a short vertical line, length is based on X and Y axes scale.
    CursorMajorXMinorLY = 12  #the crosshair is a long horizontal line and a short vertical line, vertical length is based on Y axis scale.
    CursorMinorLXMajorY = 13  #the crosshair is a short horizontal line and a long vertical line, horizontal length is based on X axis scale.


class CursorOptions():
    CursorVisible = 0x1  #Hide/show cursor
    CursorSavable = 0x2  #Save cursor property when save the graph.
    CursorPointTest = 0x4  #Alow moving cursor using the cross hair along X or Y.
    CursorShowLabel = 0x8  #Show position label
    CursorShowName = 0x10  #Show the cursor name
    CursorMajorLabel = 0x20  #Show position for the long cursor only
    CursorSynchronization = 0x40  #Synchroning cursor position with other graphes
    CursorCenter = 0x80  #CChange graph x and y scales to make the cursor stay at the graph center

    #3-D cursor
    CursorXYPlane = 0x10000  #Draw cursor in XY plane
    CursorXZPlane = 0x20000  #Draw cursor in XZ plane
    CursorYZPlane = 0x40000  #Draw cursor in YZ plane
    Cursor2D = 0x80000  #Draw 2-D cursor in 3-D graph

class AnnotationOptions():
    AnnVisible = 0x1  #Hide/show an annotation
    AnnClip = 0x2  #Limit annoation inside the plot area only
    AnnEditable = 0x4  #Annotation is changeable using mouse and keyboard
    AnnSavable = 0x8  #Save annotation when save a graph
    AnnDeletable = 0x10  #Allow deleting using mouse or keyboard
    AnnArrowHidden = 0x40  #Hide/show annotation arrow
    AnnTextHidden = 0x80  #Hide/show annotation text


class AnnotationCoordinate():
    AxisCoordinate = 0
    PlotAreaCoordinate = 1


class DrawItemType():
    DrawItem_None = 0  #No shape
    DrawItem_Line = 1  #Line 
    DrawItem_Circle = 2  #Circle 
    DrawItem_Arc = 3  #Arc
    DrawItem_Curve = 4  #Bezier curve
    DrawItem_Rect = 5  #Rectangle
    DrawItem_RoundRect = 6  #Rounded rectangle
    DrawItem_Polygon = 7  #Polygon
    DrawItem_SPolygon = 8  #Closed region formed by Bezier curves
    DrawItem_Text = 9  #Text
    DrawItem_RichText = 10  #Rich text
    DrawItem_VLine = 11  #Vertical line
    DrawItem_HLine = 12  #Horizontal line
    DrawItem_Image = 13  #Image
    DrawItem_Cube = 14  #3-D cubic
    DrawItem_Cylinder = 15  #3-D cylinder
    DrawItem_Cone = 16  #3-D cone
    DrawItem_Torus = 17  #3-D torus
    DrawItem_Sphere = 18  #3-S sphere
    DrawItem_Path = 19  #Arbitrary path formed by lines and curves
    DrawItem_Mesh = 20  #Triangluation mesh
    DrawItem_Field = 100  #A text field, its display text is binded with a data model.
    DrawItem_Table = 101  #Data table
    DrawItem_Group = 1000  #A group of data items

class DrawItemMeshType():
    Mesh_3DTriangle = 0  #3-D triangular mesh
    Mesh_3DQuad = 1  #3-D quadrature mesh
    Mesh_3DExtrude = 2  #3-D extrude
    Mesh_3DRevolve = 3  #3-D Revolve

class PaletteOptions():
    PalVisible = 0x1  #Show/ide palette
    PalShortTitle = 0x2  #Display short title
    PalAutoScale = 0x4  #Set auto scale for palette scale axis
    PalChangeTitle = 0x8  #Allow title to be changed by mouses
    PalContextMenu = 0x10  #Show palette context menu
    PalDecrete = 0x20  #Specify palette color as descrete
    PalFixSize = 0x40  #
    PalEnableTranspency = 0x80  #Allow transparant color in the palette


class PaletteLevelType():
    Level_Uniform = 1  #uniform color between palette color control pointers (level)
    Level_Gradient = 2  #linear gradient color between palette color control pointers (level)


class GraphStyle():
    GraphStyle_ShowCaption = 0x1  #Show /hide graph caption

    GraphStyle_KeepAspectRatio = 0x100  #Keep the aspection ratio of graph such as circle will be displayed as a circle on screen

    #polar
    GraphStyle_PolarCircular = 0x100  #keep plot area as circle for polar plot

    #ternary
    GraphStyle_TernaryEquilateral = 0x100  #For ternary plot, keep the triangle as equilateral.

    #3-D graph options
    GraphStyle_Show2D = 0x1000  #Show 3-D surface as 2-D image
    GraphStyle_ShowBitmapText = 0x2000  #Show text using bitmap text


class GraphDisplayOrder():
    GraphDisplayOrder_CursorAnnPlot = 0  #Drawing sequence as plot, annotation, and cursor
    GraphDisplayOrder_AnnCursorPlot = 1  #Drawing sequence as plot, cursor and annotation
    GraphDisplayOrder_PlotCursorAnn = 2  #Drawing sequence as annotation, cursor, then plot
    GraphDisplayOrder_PlotAnnCursor = 3  #Drawing sequence as cursor,annotation , then plot


class GraphMouseTrackingMode():
    TrackingMode_Zoom = 0x3  #Enables zooming along the x and y axes
    TrackingMode_ZoomX = 0x1  #Enables zooming along the x axis
    TrackingMode_ZoomY = 0x2  #Enables zooming along the y axis
    TrackingMode_Pan = 0xC  #Enables panning along the x and y axes
    TrackingMode_PanX = 0x4  #Enables panning along the x axis
    TrackingMode_PanY = 0x8  #Enables panning along the y axis
    TrackingMode_ZoomPan = 0xF  #Enables zooming and panning along the x and y axes
    TrackingMode_Rotation = 0x10  #Enable rotation (3-D graph)
    TrackingMode_Cursor = 0x100  #Track courve location
    TrackingMode_Annotion = 0x200  #Modify annotation location
    TrackingMode_Plot = 0x400  #Track plot location
    TrackingMode_Axis = 0x800  #Track axis location
    TrackingMode_Sizing = 0x1000  #Track graph border

class GraphQualityType():
    GraphQualityType_HighSpeed = 0  #Render the graph using high speed algorithm without anti-aliasing
    GraphQualityType_HighQuality = 1  #Render the graph with high quality algorithm with anti-aliasing

class TextOrientationStyle():
    FixedAngle = 0  #Text rotated using given angles
    FaceCamera = 1  #Text always faces the camera
    Rotation3D = 2  #3-D rotated text


class LightOptions():
    LightEnable = 0x1  #Enable a light
    LightLowQuality = 0x2  #Render the light with low quality but efficient algorithm


class PlotVolumnDisplayType():
    Tile2D = 0  #Display as 2-D 
    Stack = 1  #Plane stack along z-axis
    Block = 2  #Display on the surface of a box
    Corner001 = 3  #Open the left, front and top corner
    Corner101 = 4  #Open the right, front and top corner
    Corner011 = 5  #Open the left, back and top corner


class PlotCubicPlane():
    Plane_X0 = 0
    Plane_X1 = 1
    Plane_Y0 = 2
    Plane_Y1 = 3
    Plane_Z0 = 4
    Plane_Z1 = 5
    Plane_XZ = 6
    Plane_ZX = 7
    Plane_YZ = 8
    Plane_ZY = 9


class Projection3DType():
    Orthographic = 0  #Orthographic project style
    Perspective = 1  #Perspective project style

class DrawZoom_Mode():
    DrawZoom_02 = 0  #2% zoom scale
    DrawZoom_10 = 1  #10% zoom scale
    DrawZoom_25 = 2  #25% zoom scale
    DrawZoom_50 = 3  #50% zoom scale
    DrawZoom_75 = 4  #75% zoom scale
    DrawZoom_100 = 5  #100% zoom scale
    DrawZoom_150 = 6  #150% zoom scale
    DrawZoom_200 = 7  #200% zoom scale
    DrawZoom_AspectFitView = 8  #Fit the draw window with aspect ratio
    DrawZoom_FitView = 9  #Fir the draw window 

class DrawStyle():
    DrawStyle_HRuler = 0x1  #Show/hide the horizontal ruler
    DrawStyle_VRuler = 0x2  #Show/hide the vertical ruler
    DrawStyle_DrawBar = 0x4  #Show/hide the draw toolbar
    DrawStyle_FloatDrawBar = 0x8  #Dock/float draw toolbar
    DrawStyle_ViewOnly = 0x10  #For view report only
    DrawStyle_Grid = 0x20  #Draw the scale grid
    DrawStyle_Palette = 0x40  #Draw palette
 
class TableType():
    General = 0 #Data table
    Excel = 1   #Excel style
    Header = 2  #Has row and column header

class TableOption():
    ShowFormularBar = 0x1  #Show formula bar
    ShowTab = 0x2  #Show grid page tab
    ShowTabNavigator = 0x4  #Show grid page tab navigator
    ShowHeader = 0x8  #Show header cells
    NotifyDataChanging = 0x10  #Notify daa changing through widget plugin
    VerticalTab = 0x40  #Show vertical page tab
    AllowImportData = 0x80  #Allow data importing from a file
    AllowExportData = 0x100  #Allow data exporting to a file
    FitColWindow = 0x200  #Change column width to fit the grid width with window width
    FitRowWindow = 0x400  #Change row height to fit the grid height with window height
    NoVGridLine = 0x800  #Hide vertical grid line
    NoHGridLine = 0x1000  #Hide horizontal grid line
    NoSelection = 0x2000  #Disable cell selection
    NoHeaderSizing = 0x4000  #Disable sizing grid's row height and column width
    NoHeaderSelection = 0x8000  #Disable select cells using grid header
    WholeRowSelection =   0x20000000  #Select one row
    WholeColSelection =   0x40000000  #Select one column
    SingleCellSelection = 0x80000000  #Select one cell only

class TableMenuStyle():
    CellMenuVisible = 0x1  #enable/disable popup menu
    TabMenuVisible = 0x2  #Allow tab popup menu
    ExportDataMenu = 0x4  #Data export menu item
    Cut = 0x8  #Cut menu item
    Copy = 0x10  #Copy menu item
    Paste = 0x20  #Paste menu item
    Insert = 0x40   #Insert cell menu item
    Delete = 0x80  #Delete cell menu item
    InsertHHeader = 0x100  #Insert grid horizontal header menu item
    InsertVHeader = 0x200  #Inser grid vertical header menu item
    Clear = 0x400  #Clear cell data menu item
    JoiningCells = 0x800  #Join cells menu item
    UnJoiningCells = 0x1000  #unjoin cells menu item
    FormatCells = 0x2000  #Format cell dialog menu item
    InsertSheet = 0x4000  #Insert grid sheet menu item
    DeleteSheet = 0x8000  #Delete grid sheet menu item
    RenameSheet = 0x10000  #Rename grid sheet menu item
    TabProperties = 0x20000  #Tab setting dialog menu item
    ImportDataMenu = 0x40000  #Import data menu item
    ColIncData = 0x80000  #Set incremental column data menu item
    RowIncData = 0x100000  #Set incremental row data menu item
    ColSetData = 0x200000  #Set column data menu item
    RowSetData = 0x400000   #Set row data menu item
    ColSetSelectData = 0x800000  #Set selected column data menu item
    RowSetSelectData = 0x1000000    #Set selected row data menu item


"""Grid cell type"""

class GridCellType():
    CellText = 0  #Text cell
    CellData = 1 #Data cell (integer, float) 
    CellDropList = 2  #Dropdown list cell
    CellCheck = 3 #Checkbox cell
    CellSpin = 4 #Numeric Spinbox cell
    CellColor = 5 #Color selection box
    CellButton = 6 #Push buttin cell

"""Data category for data cell"""

class GridCellDataCategory():
    DataText = 0    #data is presented as text
    DataNumber = 1  #data s double number
    DataScientific = 2  #Scientific notation (mantissa/exponent) 
    DataPercent = 3 #Percent notation
    DataDate = 4    #Date
    DataTime = 5    #Time

"""Grid cell data format"""

class GridCellDataFormat():
    TextFormat = 0  #for DataText category 
    DataGeneral = 0 #for DataNumber category 
    DataFormated = 1    #123.4
    FormatScientific = 0  #for DataScientific category 
    FormatPercent = 0   #for Percent category 
    FormatDate = 0  #for DataDate category 
    FormatTime = 0  #for DataTime category 

"""Options for inserting cell function"""

class CellInsertOption():
    ShiftCellRight = 0
    ShiftCellDown = 1
    AddRowCol = 2

"""Options for deleting cell function"""

class CellDeleteOption():
    ShiftCellLeft = 0
    ShiftCellUp = 1
    DeleteRowCol = 2

"""Appearance of grid cell"""

class GridCellStyle():
    CellStyleNone = 0
    CellStyleThin = 1
    CellStyle3DUp = 2
    CellStyleXP1 = 3
    CellStyleXP2 = 4
    CellStyleXP3 = 5
    CellStyleXP4 = 6
 
"""Format for displaying text"""
class GridTextWrap():
    SINGLELINE = 0x1
    ELLIPSIS = 0x2
    WORD_ELLIPSIS = 0x4
    WORDBREAK = 0x8
    NOCLIP = 0x10

class FontStyleWeight():
    FontStyle_Italic = 0x1
    FontStyle_UnderLine = 0x2
    FontStyle_StrikeOut = 0x4

    FontWeight_None = 0
    FontWeight_Thin = 100 << 4
    FontWeight_ExtraLight = 200 << 4
    FontWeight_Light = 300 << 4
    FontWeight_Normal = 400 << 4
    FontWeight_Medium = 500 << 4
    FontWeight_SemiBold = 600 << 4
    FontWeight_Bold = 700 << 4
    FontWeight_ExtraBold = 800 << 4
    FontWeight_Heavy = 900 << 4


class WindowType():
    """Math FFT transform window type"""
    WindowIdeal = 0
    WindowHanning = 1
    WindowHamming = 2
    WindowBlackman = 3
    WindowBartlett = 4
    WindowGaussian = 5

class PaddingType():
    """Math FFT data padding type"""
    PaddingZero = 0
    PaddingPeodic = 1
    PaddingSymmetric = 2

class MathError():
    """Math function return error code"""
    MathNoError = 0 #Operation has no error.
    MathOutOfMemory = -1 #Not enough memory to do the operation.
    MathFFTPow2 = -2 #FFT length must be power of 2.
    MathInvalid = -3 #Invalid parameter
    MathOverOrder = -4 #Over maximum order
    MathLowAccuracy = -5 #Accuracy cannot be achieved
    MathOverflow = -6 #Overflow
    MathMatrixPositve = -7 #Matrix Not Postive Defined 
    MathMatrixSingular = -7 #Matrix singular 

class WaveletType():
    """Wavelet type"""
    
    """descrete"""
    Wavelet_Daub04 = 0
    Wavelet_Daubo6 = 1
    Wavelet_Daub08 = 2
    Wavelet_Coifo6 = 3
    Wavelet_Haar02 = 4
    Wavelet_Lege02 = 5
    Wavelet_Lege04 = 6
    Wavelet_Lege06 = 7

    """continuous"""
    Wavelet_Morlet = 100
    Wavelet_Paul = 101
    Wavelet_DOG = 102


class FilterBandType():
    """Filter type"""
    FilterBand_LowPass = 0 #Low pass filter
    FilterBand_HighPass = 1 #High pass filter
    FilterBand_BandPass = 2 #Band pass filter
    FilterBand_BandStop = 3 #Band stop filter
    FilterBand_AllPass = 4 #resonator only

class IIRFilterType():
    """infinite impulse response filter type"""
    IIR_Bessel = 0 #Bessel filter
    IIR_Butterworth = 1 #Butterworth filter
    IIR_Chebyshev = 2 #Chebyshev filter
    IIR_Resonator = 3 #Resonator filter
    IIR_Integral = 4 #Proportional integral filter

class IVImageFilterType():
    """Image filter type"""
    ImageFilter_Gaussion3 = 0 #3*3 Gaussian smooth filter
    ImageFilter_Gaussion5 = 1 #5*5 Gaussian smooth filter
    ImageFilter_Gaussion = 2 #n*n Gaussian smooth filter
    ImageFilter_Median = 3 #Median filter
    ImageFilter_Sharpen = 4 #Image sharpen
    ImageFilter_SobelX = 5,  #Sobel filter:normalized x-gradient
    ImageFilter_SobelY = 6 #Sobel filter:normalized y-gradient
    ImageFilter_SobelA = 7 #Sobel filter:normalized gradient magnitude 
    ImageFilter_Blur = 8 #Image blur
    ImageFilter_Edge = 9 #Image edge detect
    ImageFilter_Contour = 10 #Image contour detect
    ImageFilter_UnsharpMask = 11 #Unsharpness mask
    ImageFilter_Linear = 12 #General linear filter

class FittingAlgorith():
    FittingAlgorith_LeastSquare = 0
