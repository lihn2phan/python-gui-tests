import os

import pytest
from comtypes.client import CreateObject

from fixture.application import Application
@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Tools\\AddressBook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    r = metafunc.fixturenames
    for fixture in metafunc.fixturenames:
        if fixture.startswith("excel_"):
            testdata = load_from_excel(fixture[6:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
def load_from_excel(file):
    group_list = []
    app = CreateObject("Excel.Application")
    app.Visible = True
    wb = app.Workbooks.Open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/groups.xlsx"))
    worksheet = wb.Sheets[1]
    row = 1
    while worksheet.Cells[row, 1].Value() != None:
        data = worksheet.Cells[row, 1].Value()
        group_list.append(data)
        row += 1
    app.Quit()
    return group_list