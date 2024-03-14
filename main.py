from flask import Flask, render_template, url_for, g
from pathlib import Path
import sqlite3


app = Flask(__name__)

##############
# Partie Web #
##############


@app.route("/", methods=["POST", "GET"])
def index():
    css_file = url_for('static', filename='style.css')
    return render_template(
        "index.html",
        css=css_file,
        title="Page d'accueil"

    )


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


###################
# Base de données #
###################


DATABASE = 'database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def show_user():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        for user in users:
            print(user['username'], 'à l\'identifiant', user['password'])


######################
# Lancement de l'app #
######################

# Lancement de l'app avec la commande → python main.py
if __name__ == "__main__":
    with app.app_context():
        # if not Path(DATABASE).is_file():  # Si la base de données n'existe pas
        init_db()
        show_user()
    # Jamais de debug en prod
    app.run(host='0.0.0.0', port=5000, debug=True)
