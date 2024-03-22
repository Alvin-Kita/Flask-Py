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

#############
# Web part #
############


# At launch, redirect to the homepage
@app.get('/')
def login_get():
    """
    Display the login page
    """
    css_file = url_for('static', filename='style.css')
    return render_template(
        "index.html",
        css=css_file,
        title="Page d'accueil"
    )


@app.post('/')
def login_post():
    """
    Process the information from the login form."
    Return: Redirects to the user's dashboard if the information is correct,
    otherwise displays an incorrect information message.
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
#  - Ajout de fonctionnalité qui utilise la base de donnée (Pokedex ?)
#  - Bouton déconnexion
#  - Création d'utilisateur
@app.route("/dashboard/<username>")
def dashboard(username):
    """
    Return the user's dashboard (after login).
    """
    css_file = url_for('static', filename='style.css')
    pokemons = get_pokemon(username)
    return render_template(
        "dashboard.html",
        title="Dashboard",
        username=username,
        pokemons=pokemons,
        css=css_file
    )


@app.route("/logout", methods=["POST"])
def logout_get():
    """
    Log out the user and redirect them to the homepage.
    """
    return redirect(url_for("login_get"))


#############
# DATABASE #
############


DATABASE = 'database.db'


# Database retrieval
def get_db():
    db = getattr(g, '_database', None)
    if db is None:  # If it doesn't exist: create the connection.
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


# Close
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# Initialization of the database "database.db" from schema.sql
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


# User authentication from the database
def login_user(username, password):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        return user
#

############
# Pokedex #
###########

def get_pokemon(username):
    """
    Display the list of Pokémon for a user in the database.
    """
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pokedex WHERE username = ?", (username,))
        pokemons = cursor.fetchall()
        return pokemons


@app.route("/dashboard/<username>", methods=["POST"])
def add_pokemon(username):
    """
    Add a Pokémon to the user based on the information entered in the form.
    """
    pokemon_name = request.form["pkmn_name"]
    pokemon_picture_url = request.form["pkmn_picture_url"]
    pokemon_type1 = request.form["pkmn_type1"]
    pokemon_type2 = request.form.get("pkmn_type2", None)

    if not pokemon_type1 or not pokemon_name or not pokemon_picture_url:
        message = "Tous les champs sont obligatoire (sauf type 2)"
        return redirect(url_for('dashboard', username=username, badAttempt=message))

    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO pokedex (username, pkmn_name, pkmn_picture_url, pkmn_type1, pkmn_type2) VALUES (?, ?, ?, ?, ?)",
                       (username, pokemon_name, pokemon_picture_url, pokemon_type1, pokemon_type2))
        db.commit()

    return redirect(url_for('dashboard', username=username))

###########
# LAUNCH #
#########


# # Lancement de l'app avec la commande → python main.py
# if __name__ == "__main__":
#     with app.app_context():
#         # if not Path(DATABASE).is_file():  # Si la base de données n'existe pas
#         init_db()
#     # Jamais de debug en prod
#     app.run(host='0.0.0.0', port=5000, debug=True)
