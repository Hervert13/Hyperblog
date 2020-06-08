from os import getenv
import pymssql


server = getenv("172.16.100.226:1433")
user = getenv("empleados_consulta")
password = getenv("Sisamex.#2020")



def MSSQL():
 #   try:
        print("intentando entrar al MSSQL")
        conn = pymssql.connect(server, user, password, "CardHolders")
        return conn

  #  except:
   #     print("No se conecto con premisis")