from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import pandas as pd

table = vi.IPDataTable("Data-1")
table.SetTableType(vi.TableType.General, True)
table.ModifyOption(vi.TableOption.ShowTab | vi.TableOption.ShowFormularBar, False)
table.ModifyPopupMenu(0xFFFFFFFF, True)

table.SetRowNumber(14)
table.SetColNumber(14)
table.SetTopHeaderNum(1)
name = table.GetFont(1)
if(name is not None and len(name) > 0):
     p = 1
else:
    p = table.AddFont("", 14, 0, vi.FontStyleWeight.FontWeight_Bold)
table.SetCellFont(0, 0, 10, 0, p)
table.SetCellText(0, 0, "Channel")
table.SetCellText(1, 0, "Status")
table.SetCellText(2, 0, "Port Number")
table.SetCellText(3, 0, "Channel Number")
table.SetCellText(4, 0, "Status Data")
table.SetReadOnly(2, 1, 2, 3, True)
table.SetCellFillColor(2, 1, 2, 10, 21)

table.SetCellText(0, 1, "1")
table.SetCellText(1, 1, "Enabled")
table.SetCellFillColor(1, 1, 1, 1, 27)
table.SetCellData(2, 1, 120)

table.SetCellText(0, 2, "2")
table.SetCellText(1, 2, "Disabled")
table.SetCellData(2, 2, 110)

table.SetCellText(0, 3, "3")
table.SetCellText(1, 3, "Enabled")
table.SetCellFillColor(1, 3, 1, 3, 27)
table.SetCellData(2, 3, 100)
table.SetCellData(3, 2, 10)
table.SetCellData(4, 2, 11)
table.SetCellData(4, 4, 11)
sel = table.GetSelCells()
name = table.GetCellText(0, 0)

a = np.zeros(3)
n= table.GetColData(2, 1, 3, 1, a)
print(n, a)
n= table.GetRowData(2, 2, 4, 1, a)
print(n, a)
b = np.zeros(9)
n= table.GetData(2, 4, 1, 1, 4, 1, b)
print(n, b)
s= table.GetColText(1, 1, 4, 1)
print(s)

p1 = table.GetDataFrame(2, 4, 1, 4, True, True, False)
print(p1)

p2 = table.GetDataFrame(1, 4, 1, 4, True, True, True)
print(p2)

s1 = table.GetSeries(1, 1, 4, True, True)
print(s1)

s2 = table.GetSeries(2, 1, 4, True, False)
print(s2)

table.SetDataFrame(p1, 1, 6,)

df = pd.DataFrame({'A': 1.,
                       'B': pd.Timestamp('20130102'),
                       'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})

print(df)
table.SetDataFrame(df, 6, 6)

