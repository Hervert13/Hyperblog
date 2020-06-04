import pyodbc
def MSSQL():
    print("entre al MSSQL")
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.100.226;PORT=1433;DATABASE=CardHolders;UID=empleados_consulta;PWD=Sisamex.#2020')
    return conn