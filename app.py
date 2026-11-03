import hashlib
import sqlite3
import subprocess

from flask import Flask, request

app = Flask(__name__)

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "supersecret123"


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


@app.route("/user")
def get_user():
    username = request.args.get("name", "")
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '%s'" % username)
    return str(cur.fetchall())


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/calc")
def calc():
    expr = request.args.get("expr", "1+1")
    return str(eval(expr))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
