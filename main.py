# Documentations utilisées
#
# Documentations Flask
# Accueil : https://flask.palletsprojects.com/en/3.0.x/
# Quickstart : https://flask.palletsprojects.com/en/3.0.x/quickstart/
# SQLite3 : https://flask.palletsprojects.com/en/3.0.x/patterns/sqlite3/
#
# Documentation des fonctions Python3 : https://docs.python.org/3.11/library/functions.html


from flask import Flask, render_template, url_for, g, request, redirect
import sqlite3

app = Flask(__name__)

##############
# Partie Web #
##############


# Au lancement, envoi sur la page d'accueil
@app.get('/')
def login_get():
    """
    Affiche la page de connexion
    """
    css_file = url_for('static', filename='style.css')
    return render_template(
        "index.html",
        css=css_file,
        title="Page d'accueil"
    )


# TODO : Rendre la connexion plus professionel
@app.post('/')
def login_post():
    """
    Traite les informations du formulaire de connexion
    Return : Redirige vers le dashboard de l'utilisateur si les informations sont correctes
             sinon affiche un message d'information incorrect
    """
    css_file = url_for('static', filename='style.css')
    username = request.form['username']
    password = request.form['password']
    user = login_user(username, password)
    if user:
        return redirect(url_for('dashboard', username=username))
    else:
        bad_attempt = "Utilisateur ou mot de passe incorrect."

    return render_template(
        "index.html",
        css=css_file,
        title="Page d'accueil",
        badAttempt=bad_attempt
    )


# TODO: A faire
#  - Rendre la page plus attrayante,
#  - Possibilité de changer le mot de passe
#  - Affichage d'un message type "Vous �tes le {id}ème utilisateur crée"
#  - Ajout de fonctionnalité qui utilise la base de donnée (Pokedex ?)
#  - Bouton déconnexion
@app.route("/dashboard/<username>")
def dashboard(username):
    """
    Retourne le dashboard de l'utilisateur (après connexion)
    """
    return render_template(
        "dashboard.html",
        title="Dashboard",
        username=username
    )


@app.route("/logout", methods=["POST"])
def logout_get():
    """
    Déconnecte l'utilisateur et le redirige vers la page d'accueil.
    """
    return redirect(url_for("login_get"))


###################
# Base de données #
###################


DATABASE = 'database.db'


# Récupération de la base de donnée
def get_db():
    db = getattr(g, '_database', None)  # Récupération de la base de donnée
    if db is None:  # Si elle n'existe pas : création de la connexion
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


# Ferme la connexion à la base de donnée à la fin de get_db()
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Initialisation de la base de donnée "database.db" à partir de schema.sql
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# Authentification de l'utilisateur à partir de la base de donnée
def login_user(username, password):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        return user


# TODO: Debug à supprimer
def db_test():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('select * from users where username = ?', ["toto"])
        user = cursor.fetchone()
        if user is None:
            print('No such user')
        else:
            print("toto", 'has the id', user['username'])


######################
# Lancement de l'app #
######################

# Lancement de l'app avec la commande → python main.py
if __name__ == "__main__":
    with app.app_context():
        # if not Path(DATABASE).is_file():  # Si la base de données n'existe pas
        init_db()
        db_test()
    # Jamais de debug en prod
    app.run(host='0.0.0.0', port=5000, debug=True)
