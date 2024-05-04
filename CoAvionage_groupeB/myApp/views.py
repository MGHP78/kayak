from flask import Flask, render_template 
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