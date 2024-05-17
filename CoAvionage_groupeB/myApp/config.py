ENV = "development" 
DEBUG = True
SEND_FILE_MAX_AGE_DEFAULT = 0 #vider le cache SECRET_KEY="maCleSuperSecurisee"
#Configuration du serveur web

SECRET_KEY="kjhgkjfhkjh"
WEB_SERVER = {
  "host": "localhost",
  "port":8081,
}
#Configuration du serveur de BDD
DB_SERVER = {
   "user": "admin",
   "password": "admin",
   "host": "localhost",
   "port": 8889, #8889 mac 3306 windows
   "database": "IENAC23_coavionage_groupeB",  #nom de la BDD
   "raise_on_warnings": True
}

#couleur du texte dans terminal de vscode
COLOR ={
'header' : '\033[95m',
'blue' : '\033[94m',
'green' : '\033[92m',
'orange' : '\033[93m',
'red' : '\033[31m',
'end' : '\033[0m',
}