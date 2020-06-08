import pymssql
import psycopg2
import datetime
import time





def MSSQL():
    try:
#        print("intentando entrar al MSSQL")
        server = ("172.16.100.226:1433")
        user = ("empleados_consulta")
        password = ("Sisamex.#2020")
        conn = pymssql.connect(server, user, password, "CardHolders")
        return conn
    except:
        print("no se conecto a MSSQL")



def insert_transactions(cardNumber, employeeNumber, cardHolderName, doorId):
    try:
        server_postgres        = ["172.16.100.219","5432","smx_meraki","smxdba","Metallica.2017"]
        config = "host= "+ server_postgres[0] + " port="+ server_postgres[1]+  " dbname="+server_postgres[2]+ " user="+server_postgres[3]+ " password="+server_postgres[4]
        conn   = psycopg2.connect(config)
        cursor = conn.cursor()

        fecha   = datetime.now
        data  = [cardNumber, employeeNumber, cardHolderName, fecha, fecha, fecha, doorId]

        insert_stmt = (
           """INSERT INTO public.meraki_transaction_header ("cardNumber", "employeeNumber", "cardHolderName", "transTime", fecha_creacion, fecha_modificacion, "doorName_id")"""
           """VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                  )
        cursor.execute(insert_stmt, data)
        conn.commit()
        conn.close()

    except:
        print("NO SE ENCONTRo EL SERVIDOR postgres de transacciones meraki")



def get_doorId(MAC):
    try:
        server_postgres        = ["172.16.100.219","5432","smx_meraki","smxdba","Metallica.2017"]
        config = "host= "+ server_postgres[0] + " port="+ server_postgres[1]+  " dbname="+server_postgres[2]+ " user="+server_postgres[3]+ " password="+server_postgres[4]
        conn   = psycopg2.connect(config)
        cursor = conn.cursor()

        SELECT_V = ("""SELECT id FROM public."meraki_door_name" WHERE (macAddress = \'""" + MAC + """\' );""")
        SELECT = (str(SELECT_V))
        cursor.execute(SELECT)
        doorId = cursor.fetchall()

        conn.close()
        return (doorId[0][0])
        
        

# def MSSQL():
#  #   try:
#         print("intentando entrar al MSSQL")
#         conn = pymssql.connect(server, user, password, "CardHolders")
#         return conn

#   #  except:
#    #     print("No se conecto con premisis")