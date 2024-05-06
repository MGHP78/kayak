import mysql.connector
from flask import session
from ..config import DB_SERVER, COLOR
import myApp.model.bddGen as bddGen
# connexion au serveur de la base de données
def connexion():
    try:
        cnx = mysql.connector.connect(**DB_SERVER)
        print(COLOR['green'] + 'connexion BDD OK' + COLOR['end'])
        return cnx
    
    except mysql.connector.Error as err: # problème
        session['errorDB'] = format(err)
        print(COLOR['red'] + session['errorDB'] + COLOR['end'])
        return None
    
def close_bd(cursor,cnx):
    cursor.close()
    cnx.close()
    
def get_membresData():
    cnx = connexion()
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

def add_membreData(nom, prenom, mail, login, motPasse, statut,avatar):
    cnx = bddGen.connexion()
    if cnx is None:
        return None
    sql = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut, avatar) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    param = (nom, prenom, mail, login, motPasse, statut, avatar)
    msg = {
        "success":"addMembreOK",
        "error" : "Failed add membres data"
    }
    lastId = bddGen.addData(cnx, sql, param, msg)
    cnx.close()
    #dernier id créé = id du nouvel utilisateur
    return lastId