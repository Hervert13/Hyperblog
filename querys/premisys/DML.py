import pyodbc
def getQryPeople(conn,cardNumber):
    try:
   
        
        cursor = conn.cursor()
        
        QUERY = ("""                        
            SELECT CH.FirstName + ' ' + CH.LastName as cardHolderName ,  CH.EmployeeNumber as employeeNumber ,  CHC.card_number as cardNumber FROM Cardholder_Card AS CHC
            INNER JOIN Cardholders AS CH
                ON (CHC.CardHolder_ID = CH.cardholder_id)
            where CHC.card_number = '"""+ cardNumber + """'
            """)
        print(QUERY)
        cursor.execute(QUERY)
        EMPLOYEE = []
        NOMBRE = []
        DATA = []
        for row in cursor:
            NOMBRE.append("cardHolderName")
            NOMBRE.append("employeeNumber")
            NOMBRE.append("cardNumber")

            EMPLOYEE.append(NOMBRE)
            DATA.append(row[0])
            DATA.append(row[1])
            DATA.append(row[2])
            EMPLOYEE.append(DATA)
        return EMPLOYEE

    except :
        print("entre al ereror")
        conn.close()
 