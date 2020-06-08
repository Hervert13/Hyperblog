import pyodbc

def MSSQL():
 #   try:
 
        print("entre al MSSQL")
        conn = pyodbc.connect('DRIVER=FreeTDS ;SERVER=172.16.100.226;PORT=1433;DATABASE=CardHolders;UID=empleados_consulta;PWD=Sisamex.#2020')
        return conn

  #  except:
   #     print("No se conecto con premisis")