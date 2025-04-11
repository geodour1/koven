from helpers.logger import Logger

from db.connector import DBConnector
from controllers.user_controller import UserController
from flask import Flask, request, render_template, send_from_directory, jsonify, redirect

import os


# initialize application
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "")

# initialize DAL layer
db_connector = DBConnector()

# initialize controllers
user_controller = UserController(db_connector)

@app.route("/", methods=['GET'])
def index():
    return render_template(
        'index.html'
    )

### USERS
@app.route("/users", methods=['GET'])
def users():
    return user_controller.get_users(request)

@app.route("/user", methods=['GET', 'POST'])
def user_add():
    return user_controller.add_user(request)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


# run application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
