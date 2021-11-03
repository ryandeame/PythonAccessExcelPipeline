import pyodbc

try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Projects\PythonAccessExcelPipeline\Database\db.accdb;'
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()

except pyodbc.Error as e:
    print("Error when connecting.", e)