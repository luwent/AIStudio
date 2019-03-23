from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import time

table = vi.IPDataTable("Data-2")
table.SetTableType(vi.TableType.General, True)
table.ModifyOption(vi.TableOption.ShowTabNavigator | vi.TableOption.ShowFormularBar, False)
table.ModifyOption(vi.TableOption.VerticalTab, True)
table.ModifyPopupMenu(0xFFFFFFFF, True)
table.SetTopHeaderNum(2)
table.SetLeftHeaderNum(0)

table.SelectSheet(0)
table.SetRowNumber(12)
table.SetColNumber(10)
table.SetSheetName(0, "Setup")

name = table.GetFont(1)
if(name is not None and len(name) > 0):
     p = 1
else:
    p = table.AddFont("", 14, 0, vi.FontStyleWeight.FontWeight_Bold)
table.JointCells(0, 0, 0, 1)
table.JointCells(1, 0, 1, 1)
table.SetCellFillColor(0, 0, 10, 1, 20)
table.SetCellFont(0, 0, 10, 0, p)
table.SetCellText(0, 0, "Channel")
table.SetCellText(1, 0, "Status")
table.JointCells(2, 0, 3, 0)
table.SetCellText(2, 0, "Connection")
table.SetCellText(2, 1, "Port")
table.SetCellText(3, 1, "IP")
table.SetReadOnly(0, 2, 0, 10, True)
table.SetCellText(4, 0, "Type")
table.JointCells(4, 0, 4, 1)
table.SetCellText(5, 0, "Display Color")
table.SetColWidth(5, 90)
table.JointCells(5, 0, 5, 1)
table.SetCellText(6, 0, "Action")
table.JointCells(6, 0, 6, 1)

table.SetCellFormat(1, 2, 1, 10, vi.GridCellType.CellCheck, vi.GridCellStyle.CellStyleNone)
table.SetCellFormat(2, 2, 2, 10, vi.GridCellType.CellSpin,  vi.GridCellStyle.CellStyleNone)
table.SetCellFormat(4, 2, 4, 10, vi.GridCellType.CellDropList,  vi.GridCellStyle.CellStyleNone)
table.SetCellFormat(5, 2, 5, 10, vi.GridCellType.CellColor,  vi.GridCellStyle.CellStyleNone)
table.SetCellFormat(6, 2, 6, 10, vi.GridCellType.CellButton,  vi.GridCellStyle.CellStyleNone)

table.SetCellText(0, 2, "1")
table.SetCellData(1, 2, 1)
table.SetCellData(2, 2, 120)
table.SetCellText(3, 2, "192.168.1.1")
table.SetCellText(4, 2, "Alarm\nI/O\nWaveform")
table.SetCellData(5, 2, 0xFFFF0000)
table.SetCellText(6, 2, "Setup")

table.SetCellText(0, 3, "2")
table.SetCellText(1, 3,  "")
table.SetCellData(2, 3, 110)
table.SetCellText(3, 3, "192.168.1.2")
table.SetCellText(4, 3, "Alarm\nI/O\nWaveform")
table.SetCellData(5, 3, 0xFF00FF00)
table.SetCellText(6, 3, "Setup")

table.SetCellText(0, 4, "3")
table.SetCellData(1, 4, 1)
table.SetCellData(2, 4, 100)
table.SetCellText(3, 4, "192.168.1.3")
table.SetCellText(4, 4, "Alarm\nI/O\nWaveform")
table.SetCellData(5, 4, 0xFF0000FF)
table.SetCellText(6, 4, "Setup")
	
if(table.GetSheetNumber() < 2):
    table.AddSheet("test")
table.SelectSheet(1)    
table.SetRowNumber(12)    
table.JointCells(0, 0, 4, 0)
table.JointCells(5, 0, 9, 0)
table.SetCellText(0, 0, "Chanel-1")
table.SetCellText(5, 0, "Chanel-2")

table.SetCellText(0, 1, "Status")
table.SetCellText(1, 1, "Amplitude(%)")
table.SetCellText(2, 1, "Frequency(MHz)")
table.SetColWidth(2, 100)
table.SetCellText(3, 1, "Alarm")
table.SetCellText(4, 1, "Output")

table.SetCellText(5, 1, "Status")
table.SetCellText(6, 1, "Amplitude(%)")
table.SetCellText(7, 1, "Frequency(MHz)")
table.SetColWidth(7, 100)
table.SetCellText(8, 1, "Alarm")
table.SetCellText(9, 1, "Output")
red = table.AddColor(0xFFFF0000)
green = table.AddColor(0xFF00FF00)
blue = table.AddColor(0xFF0000FF)

def Animation():
    table.SelectSheet(1)
    data = np.random.normal(5, 10, 10)
    table.SetColData(1, 2, data, False)
    for i in range(10):
        if data[i] > 0:
            table.SetCellText(0, i + 2, "OK", True)
        else:
             table.SetCellText(0, i + 2, "Fail", True)
        if data[i] > 10:
            table.SetCellFillColor(3, i + 2, 3, i + 2, red)
        elif data[i] > 6:
            table.SetCellFillColor(3, i + 2, 3, i + 2, blue)
        else:
            table.SetCellFillColor(3, i + 2, 3, i + 2, green)

    data = np.random.normal(5, 10, 10)
    table.SetColData(2, 2, data, False)
    table.SetColData(4, 2, data, False)

    data = np.random.normal(5, 10, 10)
    table.SetColData(6, 2, data, False)
    for i in range(10):
        if data[i] > 0:
            table.SetCellText(5, i + 2, "OK", True)
        else:
            table.SetCellText(5, i + 2, "Fail", True)
        if data[i] > 10:
            table.SetCellFillColor(8, i + 2, 8, i + 2, red)
        elif data[i] > 6:
             table.SetCellFillColor(8, i + 2, 8, i + 2, blue)
        else:
             table.SetCellFillColor(8, i + 2, 8, i + 2, green)

    data = np.random.normal(5, 10, 10)
    table.SetColData(7, 2,  data, False)
    table.SetColData(9, 2,  data, False)
    


while True:
    Animation()
    time.sleep(0.5)