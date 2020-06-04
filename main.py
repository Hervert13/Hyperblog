from ODBC.conexionDB import MSSQL 
from querys.premisys.DML import getQryPeople
def qryConsultRFID(cardNumber): 
    conn = MSSQL()
    qryResult = getQryPeople(conn, cardNumber)
    print(qryResult)
    return qryResult

qryConsultRFID("2146281206")
qryConsultRFID("2600496531")
qryConsultRFID("2437743115")

