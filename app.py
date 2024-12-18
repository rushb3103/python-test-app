













from libraries.db import db
from route.user import user_blueprint

from flask import Flask

app = Flask(__name__)
dbObj = db()

@app.route("/")
def hello_world():
    return "<p>Hello, I am Rushit !!</p>"

app.register_blueprint(user_blueprint, url_prefix='/user')

if  __name__ ==  '__main__':
	app.run(debug=True)


