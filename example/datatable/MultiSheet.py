from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import IStudio as vi
import numpy as np
import time

table = vi.IPDataTable("Data-3")
table.SetTableType(vi.TableType.Header, True)
table.ModifyOption(vi.TableOption.ShowTabNavigator | vi.TableOption.ShowFormularBar, False)
table.ModifyPopupMenu(0xFFFFFFFF, True)

table.SelectSheet(0)
table.SetRowNumber(1000)
table.SetColNumber(1000)
table.SetSheetName(0, "Page-1")

for col in range(100):
    data = np.random.normal(50, 50, 1000)
    table.SetColData(col, 1, data, False)
    for row in range(100):
        if data[row] > 199.9:
                table.SetCellFillColor(col, row, col, row, 16)

if table.GetSheetNumber() < 2:
    table.AddSheet("Page-2")    	
table.SelectSheet(1);
for col in range(100):
    data = np.random.normal(50, 50, 1000)
    table.SetColData(col, 1, data, False);
    for row in range(100):
        if data[row] > 189.9:
            table.SetCellFillColor(col, row, col, row, 10);
