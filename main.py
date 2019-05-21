from api import app

def runserver():
    app.run(host='0.0.0.0', port=5000, debug=True)