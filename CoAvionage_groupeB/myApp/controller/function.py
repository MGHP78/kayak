from flask import session

<<<<<<< HEAD
# passe les messages d'info en paramètres
def messageInfo(params):
=======
#passe les messages d'info en parametres
def messageInfo(params = None):
>>>>>>> be3e4b71ea3e47dca9ac95556793213ec91e6d75
    if params is None:
        params = {}
        
    #messages d'infos du views.py
    if "infoVert" in session:
        params["infoVert"] = session['infoVert']
        session.pop("infoVert", None)
<<<<<<< HEAD
        
    if "infoRouge" in session:
        params["infoRouge"] = session['infoRouge']
        session.pop("infoRouge", None)
        
    if "infoBleu" in session:
        params["infoBleu"] = session['infoBleu']
        session.pop("infoBleu", None)
        
    #messages d'info du bdd.py
    if "errorDB" in session:
        params["errorDB"] = session['errorDB']
        session.pop("errorDB", None)
            
    if "successDB" in session:
        params["successDB"] = session['successDB']
        session.pop("successDB", None)
    
    return params
=======
    
    if "infoRouge" in session:
        params["infoRouge"] = session['infoRouge']
        session.pop("infoRouge", None)
    
    if "infoBleu" in session:
        params["infoBleu"] = session['infoBleu']
        session.pop("infoBleu", None)
    
    #message d'infos du bdd.py 
    if "errorDB" in session:
        params["errorDB"] = session['errorDB']
        session.pop("errorDB", None)
    
    return params
        
    
    
>>>>>>> be3e4b71ea3e47dca9ac95556793213ec91e6d75
