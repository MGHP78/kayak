import mysql.connector
from flask import session, request
from . import bddGen
from .. import views

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

<<<<<<< Updated upstream
def update_membreData(champ, idUser, newvalue):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = " UPDATE identification SET "+champ+" = %s WHERE idUser = %s;"
    param = (newvalue, idUser)
    msg = { "success":"updateMembreOK"
    ,
    "error" : "Failed update membres data"
    }
    bddGen.updateData(cnx, sql, param, msg)
    cnx.close()
    return 1

def updateNom():
    # réception des données du formulaire
    idUser = request.form['pk']
    newvalue = request.form['value']
    update_membreData("nom", idUser, newvalue)
    return "1"

def updateStatut():
    # réception des données du formulaire
    idUser = request.form['pk']
    newvalue = request.form['value']
    update_membreData("statut", idUser, newvalue)
    return "1"

=======
def verifAuthData(login, mdp):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = "SELECT * FROM identification WHERE login=%s and motPasse=%s"
    param=(login, mdp)
    msg = {
        "success":"authOK",
        "error" : "Failed get Auth data"
    }
    # requête par fetchone
    user = bddGen.selectOneData(cnx,sql,param,msg)
    cnx.close()
    return user
>>>>>>> Stashed changes
