import mysql.connector
from flask import session


from . import bddGen
# connexion au serveur de la base de données
 
def close_bd(cursor,cnx):
    cursor.close()
    cnx.close()
    
def get_membresData():
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    
    try:
        cursor = cnx.cursor(dictionary=True)
        sql = "SELECT * FROM identification"
        cursor.execute(sql)
        listeMembres = cursor.fetchall()
        close_bd(cursor, cnx)
        
    except mysql.connector.Error as err:
        listeMembres = None
        session['errorDB'] = "Failed get membres data : {}".format(err)

    return listeMembres


def del_membreData(idUser):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "DELETE FROM identification WHERE idUser=%s;"
    param = (idUser,)
    msg = {
        "success":"suppMembreOK",
        "error" : "Failed del membres data"
    }
    bddGen.deleteData(cnx, sql, param, msg)
    cnx.close()