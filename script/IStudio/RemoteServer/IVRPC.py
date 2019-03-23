
class RPCChannelID():
    AIAcq_ID = 1
    AICaffe_ID = 2
    AITensorflow_ID = 3
    Python_ID = 4
    Shell_ID = 5
    
class RPCMessageID():
    IPCMsg_Has_Stream = 0x10000
    IPCMsg_Need_Response = 0x20000
    IPCMsg_Is_Response = 0x40000
    IPCMsg_Has_EndStream = 0x80000
    
    IPCMsg_Channel_Connection = 0xFFFF
    IPCMsg_Channel_DisConnection = 0xFFFE
    IPCMsg_Channel_IsAlive = 0xFFFD
    
    #1-200 IPGraph
    IPCMsg_Widget_SetFrameColor = 1
    IPCMsg_Widget_SetPlotAreaColor = 2
    IPCMsg_Widget_SetCaption = 3
    IPCMsg_Widget_SetCaptionAlign = 4
    IPCMsg_Widget_SetCaptionColor = 5
    IPCMsg_Widget_SetDisplayOrder = 6
    IPCMsg_Widget_TrackMode = 7
    IPCMsg_Widget_SetGraphQuality = 8
    IPCMsg_Widget_SetGraphCategory = 9
    IPCMsg_Widget_RedrawPlotArea = 14
    IPCMsg_Widget_Redraw = 15
    
    IPCMsg_Widget_GetAxisCount = 10
    IPCMsg_Widget_AddAxis = 11
    IPCMsg_Widget_RemoveAxis = 12
    IPCMsg_Widget_RemoveAxisByName = 13
    
    IPCMsg_Widget_GetPlotsCount = 20
    IPCMsg_Widget_AddPlot = 21
    IPCMsg_Widget_RemovePlot = 22
    IPCMsg_Widget_RemovePlotByName = 23
    IPCMsg_Widget_BarOffset = 24
    
    IPCMsg_Widget_GetCursorCount = 30
    IPCMsg_Widget_AddCursor = 31
    IPCMsg_Widget_RemoveCursor = 32
    IPCMsg_Widget_RemoveCursorByName = 33
    IPCMsg_Widget_RemoveCursorByIndex = 34
    
    IPCMsg_Widget_GetAnnotationCount = 40
    IPCMsg_Widget_AddAnnotation = 41
    IPCMsg_Widget_RemoveAnnotation = 42
    IPCMsg_Widget_RemoveAnnotationByName = 43
    IPCMsg_Widget_ShowAnnotationEditBar = 44
    IPCMsg_Widget_AddBoundingBox = 45
    IPCMsg_Widget_AddMaskImage = 46
    IPCMsg_Widget_ClearBoundingBox = 47
    IPCMsg_Widget_SetPalette = 50
    
    IPCMsg_Widget_ProjectionType = 51
    IPCMsg_Widget_SetOrientation = 52
    IPCMsg_Widget_SetViewCenter = 53
    IPCMsg_Widget_SetViewScale = 54
    IPCMsg_Widget_SetPlotAreaScale = 55
    IPCMsg_Widget_SetClip = 56
    IPCMsg_Widget_GetLightCount = 57
    IPCMsg_Widget_AddLight = 58
    IPCMsg_Widget_RemoveLightByName = 59
    IPCMsg_Widget_GetLight = 60
    IPCMsg_Widget_GetLightByName = 61
    IPCMsg_Widget_RemoveLightByIndex = 62
    IPCMsg_Widget_GraphSetSkyBackground = 63
    
    IPCMsg_Widget_AddDrawGroup = 73
    IPCMsg_Widget_FindDrawGroup = 74
    IPCMsg_Widget_ActiveDrawGroup = 75
    IPCMsg_Widget_AddDrawItem = 76
    IPCMsg_Widget_FindDrawItem = 77
    IPCMsg_Widget_DeleteDrawItem = 78
    IPCMsg_Widget_DrawBackgroundColor = 79
    IPCMsg_Widget_DrawPageSize = 80
    IPCMsg_Widget_DrawZoomMode = 81
    IPCMsg_Widget_DrawDrawTools = 82
    IPCMsg_Widget_DrawDrawModel = 83
    IPCMsg_Widget_AddDrawCursor = 84
    IPCMsg_Widget_RemoveDrawCursorByName = 85
    IPCMsg_Widget_RemoveDrawCursorByIndex = 86
    IPCMsg_Widget_SetDrawOrientation = 87
    IPCMsg_Widget_SetDrawViewCenter = 88
    IPCMsg_Widget_SetDrawViewScale = 89
    IPCMsg_Widget_GetDrawLightCount = 90
    IPCMsg_Widget_AddDrawLight = 91
    IPCMsg_Widget_GetDrawLight = 92
    IPCMsg_Widget_GetDrawLightByName = 93
    IPCMsg_Widget_RemoveDrawLightByName = 94
    IPCMsg_Widget_RemoveDrawLightByIndex = 95
    IPCMsg_Widget_SetSkyBackground = 97
    IPCMsg_Widget_GetDrawImage = 98
    
    #200-400 IPPlot
    IPCMsg_Widget_PlotLineColor = 200
    IPCMsg_Widget_PlotLineWidth = 201
    IPCMsg_Widget_PlotLineStyle = 202
    IPCMsg_Widget_PlotPointerWidth = 204
    IPCMsg_Widget_PlotPointerColor = 205
    IPCMsg_Widget_PlotPointerSize = 206
    IPCMsg_Widget_PlotPointerStyle = 207
    IPCMsg_Widget_PlotPointerFillColor = 208
    IPCMsg_Widget_PlotSetXAxis = 209
    IPCMsg_Widget_PlotSetYAxis = 210
    IPCMsg_Widget_PlotY = 211
    IPCMsg_Widget_PlotXRange = 212
    IPCMsg_Widget_PlotX = 213
    IPCMsg_Widget_PlotYRange = 214
    IPCMsg_Widget_PlotXY = 215
    IPCMsg_Widget_ChartY = 216
    IPCMsg_Widget_ChartX = 217
    IPCMsg_Widget_ChartXRange = 218
    IPCMsg_Widget_ChartYRange = 219
    IPCMsg_Widget_ChartRollbackX = 220
    IPCMsg_Widget_ChartRollbackY = 221
    IPCMsg_Widget_ChartXY = 222
    IPCMsg_Widget_ChartXYRange = 223
    IPCMsg_Widget_ImageXY = 224
    IPCMsg_Widget_ImageXYZ = 225
    IPCMsg_Widget_PlotVisible = 226
    IPCMsg_Widget_PlotBar = 227
    IPCMsg_Widget_PlotBarLabel = 228
    IPCMsg_Widget_PlotBarData = 229
    IPCMsg_Widget_PlotBarColor = 230
    IPCMsg_Widget_PlotBarPara = 231
    IPCMsg_Widget_PlotPie = 232
    IPCMsg_Widget_PlotPieLabel = 233
    IPCMsg_Widget_PlotPieData = 234
    IPCMsg_Widget_PlotPieColor = 235
    IPCMsg_Widget_PlotPieParaColor = 236
    IPCMsg_Widget_PlotPieParaOffset = 237
    IPCMsg_Widget_PlotPieParaLabelOffset = 238
    IPCMsg_Widget_PlotPiePara = 239
    IPCMsg_Widget_PlotPiePara3D = 240
    IPCMsg_Widget_PlotVectorXY = 241
    IPCMsg_Widget_PlotVectorAL = 242
    IPCMsg_Widget_PlotVectorPara = 243
    IPCMsg_Widget_PlotBubleXY = 244
    IPCMsg_Widget_PlotBublePara = 245
    IPCMsg_Widget_PlotErrPer = 246
    IPCMsg_Widget_PlotErrUp = 247
    IPCMsg_Widget_PlotErrLow = 248
    IPCMsg_Widget_PlotErrStyle = 249
    IPCMsg_Widget_Plot3DZ = 250
    IPCMsg_Widget_Plot3DZRange = 251
    IPCMsg_Widget_Chart3DZ = 252
    IPCMsg_Widget_Chart3DZRange = 253
    IPCMsg_Widget_Chart3DZRollback = 254
    IPCMsg_Widget_Chart3DXYZ = 255
    IPCMsg_Widget_Chart3DXYZRange = 256
    IPCMsg_Widget_Plot3DXYZ = 257
    IPCMsg_Widget_Plot3DSurfaceXYZ = 258
    IPCMsg_Widget_Plot3DSurfacePara = 259
    IPCMsg_Widget_Plot3DSurfaceZ = 260
    IPCMsg_Widget_Plot3DSurfaceRange = 261
    IPCMsg_Widget_Plot3DVolRange = 262
    IPCMsg_Widget_Plot3DVolData = 263
    IPCMsg_Widget_Plot3DVolType = 264
    IPCMsg_Widget_Plot3DVolCut = 265
    IPCMsg_Widget_Plot3DBar = 266
    IPCMsg_Widget_Plot3DBarLabel = 267
    IPCMsg_Widget_Plot3DVector = 268
    IPCMsg_Widget_Plot3DVectorABL = 269
    IPCMsg_Widget_Plot3DBubble = 270
    IPCMsg_Widget_PlotStyle = 271
    IPCMsg_Widget_PlotDataOffset = 272
    IPCMsg_Widget_SurfaceImage = 273
    IPCMsg_Widget_ImageRange = 274
    IPCMsg_Widget_PlotSetName= 275
    IPCMsg_Widget_PlotOption = 276

    #400-600 IPAxis
    IPCMsg_Widget_AxisSetTitle = 400
    IPCMsg_Widget_AxisColor = 401
    IPCMsg_Widget_AxisOption = 402
    IPCMsg_Widget_AxisType = 403
    IPCMsg_Widget_AxisSetMinimum = 404
    IPCMsg_Widget_AxisSetMaximum = 405
    IPCMsg_Widget_AxisGetMinimum = 406
    IPCMsg_Widget_AxisGetMaximum = 407
    IPCMsg_Widget_AxisLabelFont = 408
    IPCMsg_Widget_AxisLabelColor = 409
    IPCMsg_Widget_AxisTickPad = 410
    IPCMsg_Widget_AxisTickMajorSize = 411
    IPCMsg_Widget_AxisTickMinorSize = 412
    IPCMsg_Widget_AxisTickScale = 413
    IPCMsg_Widget_AxisTickRange = 414
    IPCMsg_Widget_AxisTickMajorNumber = 415
    IPCMsg_Widget_AxisTickMinorNumber = 416
    IPCMsg_Widget_AxisGridColor = 417
    IPCMsg_Widget_AxisGridStyle = 418
    IPCMsg_Widget_AxisGridWidth = 419
    IPCMsg_Widget_AxisGridMinorColor = 420
    IPCMsg_Widget_AxisGridMinorStyle = 421
    IPCMsg_Widget_AxisGridMinorWidth = 422
    IPCMsg_Widget_AxisVPOption = 423
    IPCMsg_Widget_AxisVPAdd = 424
    IPCMsg_Widget_AxisVPSet = 425
    IPCMsg_Widget_AxisVPRemove = 426
    IPCMsg_Widget_AxisLabelOrientation = 427
    IPCMsg_Widget_AxisVPRemoveAll = 428
    
    #600-800 IPCursor
    IPCMsg_Widget_CursorColor = 600
    IPCMsg_Widget_CursorLineStyle = 601
    IPCMsg_Widget_CursorLineWidth = 602
    IPCMsg_Widget_CursorStyle = 603
    IPCMsg_Widget_CursorWidth = 604
    IPCMsg_Widget_CursorHeight = 605
    IPCMsg_Widget_CursorLabelColor = 606
    IPCMsg_Widget_CursorLabelFont = 607
    IPCMsg_Widget_CursorLabelDecimal = 608
    IPCMsg_Widget_CursorSnapMode = 609
    IPCMsg_Widget_CursorPlotIndex = 610
    IPCMsg_Widget_CursorPos = 611
    IPCMsg_Widget_CursorPos3D = 612
    IPCMsg_Widget_CursorSetPos3D = 613
    IPCMsg_Widget_CursorLength = 614
    IPCMsg_Widget_CursorOrientation = 615
    IPCMsg_Widget_CursorOption = 616
    IPCMsg_Widget_CursorSetPosition = 617
    
    #800-1000 IPDrawItem
    IPCMsg_Widget_DrawItemType = 800
    IPCMsg_Widget_DrawItemLineStyle = 801
    IPCMsg_Widget_DrawItemLineWidth = 802
    IPCMsg_Widget_DrawItemLineColor = 803
    IPCMsg_Widget_DrawItemLineBCap = 804
    IPCMsg_Widget_DrawItemLineECap = 805
    IPCMsg_Widget_DrawItemFillStyle = 806
    IPCMsg_Widget_DrawItemFillColor = 807
    IPCMsg_Widget_DrawItemFont = 808
    IPCMsg_Widget_DrawItemTextColor = 809
    IPCMsg_Widget_DrawItemOption = 810
    IPCMsg_Widget_DrawItemText = 811
    IPCMsg_Widget_DrawItemAlign = 812
    IPCMsg_Widget_DrawItemCoord = 813
    IPCMsg_Widget_DrawItemCoord3D = 814
    IPCMsg_Widget_DrawItemRotation = 815
    IPCMsg_Widget_DrawGroupAddGroup = 816
    IPCMsg_Widget_DrawGroupRemoveGroup = 817
    IPCMsg_Widget_DrawGroupFindGroup = 818
    IPCMsg_Widget_DrawGroupAddItem = 819
    IPCMsg_Widget_DrawGroupFindItem = 820
    IPCMsg_Widget_DrawGroupDeleteItem = 821
    IPCMsg_Widget_DrawGroupRemoveAll = 822
    
    #1000-1200 IPAnnotation
    IPCMsg_Widget_AnnotationCaption = 1000
    IPCMsg_Widget_AnnotationCaptionColor = 1001
    IPCMsg_Widget_AnnotationCaptionBorder = 1002
    IPCMsg_Widget_AnnotationCaptionLoc = 1003
    IPCMsg_Widget_AnnotationArrowLineWidth = 1004
    IPCMsg_Widget_AnnotationArrowLineColor = 1005
    IPCMsg_Widget_AnnotationArrowLineStyle = 1006
    IPCMsg_Widget_AnnotationArrowLineBCap = 1007
    IPCMsg_Widget_AnnotationArrowLineECap = 1008
    IPCMsg_Widget_AnnotationArrowPos = 1009
    IPCMsg_Widget_AnnotationType = 1010
    IPCMsg_Widget_AnnotationCaptionLoc3D = 1011
    IPCMsg_Widget_AnnotationCaptionOrientation = 1012
    IPCMsg_Widget_AnnotationArrowPos3D = 1013
    
    #1200-1400 IPPalette
    IPCMsg_Widget_PaletteMax = 1200
    IPCMsg_Widget_PaletteMin = 1201
    IPCMsg_Widget_PaletteGetColor = 1202
    IPCMsg_Widget_PaletteSetColor = 1203
    IPCMsg_Widget_PaletteLevelNum = 1204
    IPCMsg_Widget_PaletteLevelValue = 1205
    IPCMsg_Widget_PaletteLevelType = 1206
    IPCMsg_Widget_PaletteOption = 1207
    IPCMsg_Widget_PaletteTitle = 1208
    IPCMsg_Widget_PaletteAlign = 1209
    IPCMsg_Widget_PaletteTransparency = 1210

    #1400-1600 IPLegend
    IPCMsg_Widget_LegendVisible = 1400
    IPCMsg_Widget_LegendLength = 1401
    IPCMsg_Widget_LegendPad = 1402
    IPCMsg_Widget_LegenLoc = 1403
    IPCMsg_Widget_LegenFont = 1404
    
    #1600-1800 IPLight
    IPCMsg_Widget_LightOption = 1600
    IPCMsg_Widget_LightDir = 1601
    IPCMsg_Widget_LightPos = 1602
    IPCMsg_Widget_LightDirLight = 1603
    IPCMsg_Widget_LightPointLight = 1604
    IPCMsg_Widget_LightSpotLight = 1605
    IPCMsg_Widget_LightColor = 1606
    IPCMsg_Widget_LightAtt = 1607
    
    #1800-2000 IPGrid 
    IPCMsg_Widget_GridType = 1801
    IPCMsg_Widget_GridGetColNumber = 1802
    IPCMsg_Widget_GridGetRowNumber = 1803
    IPCMsg_Widget_GridColNumber = 1804
    IPCMsg_Widget_GridRowNumber = 1805
    IPCMsg_Widget_GridAppendRow = 1806
    IPCMsg_Widget_GridAppendCol = 1807
    IPCMsg_Widget_GridInsertRow = 1808
    IPCMsg_Widget_GridInsertCol = 1809
    IPCMsg_Widget_GridInsertCell = 1810
    IPCMsg_Widget_GridRemoveCell = 1811
    IPCMsg_Widget_GridRemoveRow = 1812
    IPCMsg_Widget_GridRemoveCol = 1813
    IPCMsg_Widget_GridRemoveAll = 1814
    IPCMsg_Widget_GridSelCell = 1815
    IPCMsg_Widget_GridGetSelCell = 1816
    IPCMsg_Widget_GridJointCell = 1817
    IPCMsg_Widget_GridUnJointCell = 1818
    IPCMsg_Widget_GridCellData = 1819
    IPCMsg_Widget_GridCellText = 1820
    IPCMsg_Widget_GridCellChar = 1821
    IPCMsg_Widget_GridColData = 1822
    IPCMsg_Widget_GridRowData = 1823
    IPCMsg_Widget_GridColDataArray = 1824
    IPCMsg_Widget_GridData = 1825
    IPCMsg_Widget_GridReadOnly = 1826
    IPCMsg_Widget_GridColReadOnly = 1827
    IPCMsg_Widget_GridRowReadOnly = 1828
    IPCMsg_Widget_GridGetCellData = 1829
    IPCMsg_Widget_GridGetCellText = 1830
    IPCMsg_Widget_GridGetData = 1831
    IPCMsg_Widget_GridGetColData = 1832
    IPCMsg_Widget_GridGetColText = 1833
    IPCMsg_Widget_GridGetRowData = 1834
    IPCMsg_Widget_GridClearData = 1835
    IPCMsg_Widget_GridDeleteData = 1836
    IPCMsg_Widget_GridDefaultColWidth = 1837
    IPCMsg_Widget_GridDefaultRowHeight = 1838
    IPCMsg_Widget_GridColWidth = 1839
    IPCMsg_Widget_GridRowHeight = 1840
    IPCMsg_Widget_GridFitCol = 1841
    IPCMsg_Widget_GridFitRow = 1842
    IPCMsg_Widget_GridEnableScroll = 1843
    IPCMsg_Widget_GridTopHeaderNum = 1844
    IPCMsg_Widget_GridLeftHeaderNum = 1845
    IPCMsg_Widget_GridGetColName = 1846
    IPCMsg_Widget_GridCellFormat = 1847
    IPCMsg_Widget_GridCellAlignment = 1848
    IPCMsg_Widget_GridDataFormat = 1849
    IPCMsg_Widget_GridCellStyle = 1850
    IPCMsg_Widget_GridCellType = 1851
    IPCMsg_Widget_GridCellTypeStyle = 1852
    IPCMsg_Widget_GridCellhAlign = 1853
    IPCMsg_Widget_GridCellvAlign = 1854
    IPCMsg_Widget_GridTextWrap = 1855
    IPCMsg_Widget_GridTextRotation = 1856
    IPCMsg_Widget_GridDecimal = 1857
    IPCMsg_Widget_GridDataCategory = 1858
    IPCMsg_Widget_GridCellDataFormat = 1859
    IPCMsg_Widget_GridAddFont = 1860
    IPCMsg_Widget_GridSetFont = 1861
    IPCMsg_Widget_GridAddColor = 1862
    IPCMsg_Widget_GridTextColor = 1863
    IPCMsg_Widget_GridFillColor = 1864
    IPCMsg_Widget_GridTab = 1865
    IPCMsg_Widget_GridSheetName = 1866
    IPCMsg_Widget_GridAddSheet = 1867
    IPCMsg_Widget_GridInsertSheet = 1868
    IPCMsg_Widget_GridRemoveSheet = 1869
    IPCMsg_Widget_GridSelectSheet = 1870
    IPCMsg_Widget_GridGetSheetNumber = 1871
    IPCMsg_Widget_GridOption = 1872
    IPCMsg_Widget_GridMemuStyle = 1873
    IPCMsg_Widget_GridGetFont = 1874
    IPCMsg_Widget_GridGetRowText = 1875
    IPCMsg_Widget_GridGetText = 1876
    IPCMsg_Widget_GridText = 1877

    IPCMsg_Log_Info = 9000
    IPCMsg_Log_Warning = 9001
    IPCMsg_Log_Error = 9002
    IPCMsg_Log_Fatal = 9003
    IPCMsg_Debug_Info = 9004
    IPCMsg_Debug_Status = 9005
    IPCMsg_PY_DebugWait = 9006
    IPCMsg_PY_SaveGraphDef = 9007
    IPCMsg_PY_GetInputText = 9008
    
    IPCMsg_Device_GetCameraImage = 9100
    IPCMsg_Device_GetAudioWave = 9101
    
    IPCMsg_Min_Widget = 1
    IPCMsg_Max_Widget = 9999
    
    IPCMsg_PY_SaveTensor = 10000
    IPCMsg_PY_SaveText = 10001
    IPCMsg_PY_SaveScalar = 10002
    IPCMsg_PY_LoadDebugInfo = 10003
    
    IPCMsg_Tool_Exit = 10005
    IPCMsg_Tool_Download = 10006
    IPCMsg_Tool_Train = 10007
    IPCMsg_Tool_Test = 10008
    IPCMsg_PY_GetFolder = 10009
    IPCMsg_PY_GetProjectSettings = 10010
    IPCMsg_Acq_GetAudio = 10011
    
    IPCMsg_Min_Cmd = 10000
    IPCMsg_Max_Cmd = 20000
    
    IPCMsg_Debug_PostInfo = 20001
    IPCMsg_PY_ReadLine = 20002
    

class TensorType():
    Unknown = 0
    Variable = 1
    Image = 2
    Waveform = 3
    Scalar = 4
    Tensor = 5
    Text = 6
        
class IPCStatus():
    IPC_Unknown = 0
    IPC_OK = 1
    IPC_Cancel = 2


