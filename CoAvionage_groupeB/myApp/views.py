from flask import Flask, render_template, request, redirect, session
import model.bdd as bdd
import controller.function as f
import hashlib

app = Flask(__name__) 
app.template_folder = "template" 
app.static_folder = "static" 
app.config.from_object('myApp.config')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sgbd")
def sgbd():
    listeMembres = bdd.get_membresData()
    params ={
        'liste':listeMembres
    }
    params = f.messageInfo(params)
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
    mdp = hashlib.sha256(motPasse.encode())
    mdpC = mdp.hexdigest()
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



