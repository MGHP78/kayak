from flask import Flask, render_template, request, redirect, session, jsonify
from .model import bdd as bdd
from .controller import function as f
from werkzeug.utils import secure_filename
import pandas, os
from openpyxl import Workbook

app = Flask(__name__)

app.template_folder = "template"
app.static_folder = "static"
app.config.from_object('myApp.config')

# /files = répertoire de sauvegarde et de téléchargement des fichiers
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/files/'

# page accueil
@app.route("/")
def index(): 
    params = f.messageInfo()
    return render_template("index.html", **params)

# page se connecter
@app.route("/login")
def login():
    params = f.messageInfo()
    return render_template("login.html", **params)

# page contact
@app.route("/contact")
def login():
    params = f.messageInfo()
    return render_template("contact.html", **params)

# page sgbd
@app.route("/sgbd")
def sgbd():
    listeMembres = bdd.get_membresData()
    params = { 'liste': listeMembres }
    params = f.messageInfo(params)
    return render_template("sgbd.html", **params)

# gestion des fichiers
@app.route("/fichiers")
def fichiers():
    params = f.messageInfo()
    return render_template("fichiers.html", **params)

# menu se déconnecter
@app.route("/logout")
def logout():
    session.clear()  # suppression de la session
    session["infoBleu"] = "Vous êtes déconnecté. Merci de votre visite"
    return redirect("/login")


# authentification
@app.route("/connecter", methods=["POST"])
def connect():
    print("test")
    login = request.form['login']
    mdp = request.form['mdp']
    user = bdd.verifAuthData(login, mdp)

    try:
        # Authentification réussie
        session["idUser"] = user["idUser"]
        session["nom"] = user["nom"]
        session["prenom"] = user["prenom"]
        session["mail"] = user["mail"]
        session["statut"] = user["statut"]
        session["avatar"] = user["avatar"]
        session["infoVert"] = "Authentification réussie"
        return redirect("/")
    except TypeError as err:
        # Authentification refusée
        session["infoRouge"] = "Authentification refusée"
        return redirect("/login")


# suppression d'un membre
@app.route("/suppMembre")
def suppMembre():
    idUser = request.args.get("userDel")
    bdd.del_membreData(idUser)
    # la suppression a bien fonctionné
    if "errorDB" not in session:
        session["infoVert"] = "L'utilisateur a bien été supprimé"
    else:
        session["infoRouge"] = "Problème suppression utilisateur"
    return redirect("/sgbd")

# ajout d'un membre
@app.route("/addMembre", methods=['POST'])
def addMembre():
    print("ajjoutok")
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['login']
    motPasse = request.form['mdp']
    statut = request.form['statut']
    avatar = request.form['avatar']
    lastId = bdd.add_membreData(nom, prenom, mail, login, motPasse, statut, avatar)
    print(lastId)  # dernier id créé par la BDD
    if "errorDB" not in session:    
        session["infoVert"] = "Nouveau membre inséré"
    else:
        session["infoRouge"] = "Problème ajout utilisateur"
    return redirect("/")


# Mise à jour du nom et du statut d'un membre
@app.route("/updateMembre/<champ>", methods=['POST'])
def updateMembre(champ=None):
    idUser = request.form['pk']
    newvalue = request.form['value']
    if champ == "N":
        bdd.update_membreData("nom", idUser, newvalue)
    if champ == "S":
        bdd.update_membreData("statut", idUser, newvalue)
    return "1"
