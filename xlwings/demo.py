"""
In der Konsole folgende Befehle eingeben:

pip install xlwings
xlwings addin install
xlwings quickstart demo
"""

import xlwings as xw


""" def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!" """


@xw.func
def hello(name):
    return f"Hello {name}!"

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    for row in range(2, 12):
        var = sheet["a" + str(row)].value
        sheet["b"+ str(row)].value = var*2


if __name__ == "__main__":
    xw.Book("demo.xlsm").set_mock_caller()
    main()
