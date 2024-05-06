from flask import Flask, render_template, session, request, redirect
from .model import bdd, bddGen
from .controller import function as f
import hashlib

app = Flask(__name__) 
app.template_folder = "template" 
app.static_folder = "static" 
app.config.from_object('myApp.config')

@app.route("/")
def index():
    listeMembres = bdd.get_membresData()
    params ={
        'liste':listeMembres
    }
    print(listeMembres)
    params = f.messageInfo(params)

    return render_template("index.html",**params)
 

    return render_template("sgbd.html", **params)

# ajout d'un membre
@app.route("/addMembre", methods=['POST'])
def addMembre():
# réception des données du formulaire
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['login']
    motPasse = request.form['mdp']
    mdp = hashlib.sha256(motPasse.encode())
    mdpC = mdp.hexdigest()
    statut = request.form['statut']
    avatar = request.form['avatar']
    lastId = bdd.add_membreData(nom, prenom, mail, login, motPasse, statut, avatar)
    print(lastId) # dernier id créé par le serveur de BDD

    if "errorDB" not in session:
        session["infoVert"]="Nouveau membre inséré"
    else:
        session["infoRouge"]="Problème ajout utilisateur"
    return redirect("/sgbd")


@app.route("/compte")
def compte():
    return render_template("compte.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/sgbd")
def sgbd():
    listeMembres = bdd.get_membresData()
    params ={
        'liste':listeMembres
    }
    print(listeMembres)
    params = f.messageInfo(params)

    return render_template("sgbd.html", **params)