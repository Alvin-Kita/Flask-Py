from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def login():
    css_file = url_for('static', filename='style.css')
    # if request.method == "POST":
    #     username = request.form["username"]
    #     password = request.form["password"]
    #     if username == "almosk" and password == "mdp":
    #         return redirect(url_for("dashboard"))
    #     else:
    #         return render_template(
    #             "index.html",
    #             css=css_file,
    #             title="Page d'accueil",
    #             badAttempt="Utilisateur ou mot de passe incorrect"
    #         )

    return render_template(
        "index.html",
        css=css_file,
        title="Page d'accueil"
    )


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    # Jamais de debbug en prod
    app.run(host='0.0.0.0', port=5000, debug=True)

