from . import bddGen

#################################################################################
# Retourne les données de la table identification
def get_membresData():
  cnx = bddGen.connexion()
  if cnx is None: return None
  
  sql = " SELECT * FROM identification"
  param = None
  msg = {
    "success":"OKmembres",
    "error" : "Failed get membres data"
  }
  listeMembre = bddGen.selectData(cnx, sql, param, msg)
  cnx.close()
  return listeMembre


#################################################################################
#suppression d'un membre
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


#################################################################################
#ajout d'un membre
def add_membreData(nom, prenom, mail, login, motPasse, statut, avatar):
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


#################################################################################
#modification d'une donnée dans la table identification
def update_membreData(champ, idUser, newvalue):
    cnx = bddGen.connexion()
    if cnx is None: return None
    sql = " UPDATE identification SET "+champ+" = %s WHERE idUser = %s;"
    param = (newvalue, idUser)
    msg = { 
        "success":"updateMembreOK",
        "error" : "Failed update membres data"
    }
    bddGen.updateData(cnx, sql, param, msg)
    cnx.close()
    return 1


#################################################################################
#authentification des utilisateurs
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


##########################################################################
###  enregistrement des données provenant du fichier excel
def saveDataFromFile(data):
    truncateTable("identification")
    cnx = bddGen.connexion()
    if cnx is None: return None
    
    # insertion des nouvelles données avec executemany
    sql ="INSERT INTO identification (nom, prenom, mail,login, motPasse, statut, avatar) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    param = []
    for d in data:
        newData = (d['nom'],d['prenom'],d['mail'],d['login'],
                    d['motPasse'],d['statut'],d['avatar'])
        param.append(newData)
    
    msg = {
        "success":"OK saveDataFromFile",
        "error" : "Failed saveDataFromFile data"
    }  
    lastId = bddGen.addManyData(cnx, sql, param, msg)
    cnx.close()
    return lastId  

##########################################################################
def truncateTable(nomTable):
  cnx = bddGen.connexion()
  if cnx is None: return None
  
  sql = "TRUNCATE TABLE %s;"
  param = [nomTable]
  msg = {
    "succes":"truncateTableOK",
    "error" :"Failed truncate data"
  }
  return  bddGen.deleteData(cnx, sql, param, msg)
 
