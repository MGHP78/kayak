from flask import Flask, render_template, session 
from .model import bdd
from .controller import function as f
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
 
