from CoAvionage_groupeB.config import DEBUG, WEB_SERVER
from CoAvionage_groupeB.views import app
if __name__ == '__main__':
    app.run(
        host = WEB_SERVER['host'],
        port=  WEB_SERVER['port'],
        debug=DEBUG
)