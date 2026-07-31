from flask import Flask, render_template, request
import sqlite3
import bcrypt

app = Flask(__name__)

DATABASE = "database/users.db"


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        stored_password = row[0]

        if bcrypt.checkpw(
            password.encode(),
            stored_password
        ):
            return render_template(
                "welcome.html",
                username=username
            )

    return render_template(
        "login.html",
        error="Invalid Username or Password"
    )


@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "SecureBank"
    }, 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
