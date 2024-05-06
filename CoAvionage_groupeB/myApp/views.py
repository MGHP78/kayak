<<<<<<< HEAD
from flask import Flask, render_template, session 
from .model import bdd
from .controller import function as f
=======
from flask import Flask, render_template, request, redirect, session
import model.bdd as bdd
import controller.function as f
>>>>>>> be3e4b71ea3e47dca9ac95556793213ec91e6d75
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
<<<<<<< HEAD
    return render_template("index.html",**params)
 
=======
    return render_template("sgbd.html", **params)

# ajout d'un membre
@app.route("/addMembre"
, methods=['POST'])
def addMembre():
# réception des données du formulaire
    nom = request.form['nom']
    prenom = request.form['prenom']
    mail = request.form['mail']
    login = request.form['login']
    motPasse = request.form['mdp']
    statut = request.form['statut']
    avatar = request.form['avatar']
    lastId = bdd.add_membreData(nom, prenom, mail,
    login, motPasse, statut, avatar)
    print(lastId) # dernier id créé par le serveur de BDD

    if "errorDB" not in session:
        session["infoVert"]="Nouveau membre inséré"
    else:
        session["infoRouge"]="Problème ajout utilisateur"
    return redirect("/sgbd")
>>>>>>> be3e4b71ea3e47dca9ac95556793213ec91e6d75
