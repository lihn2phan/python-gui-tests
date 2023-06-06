from comtypes.client import CreateObject, GetModule
import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range[f"A{i+1}"].Value[()] = f"group {i}"
tmp = os.path.join(project_dir, "groups.xlsx")
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()