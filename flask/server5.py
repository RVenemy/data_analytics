from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello This is Main Page <h1>WELCOME...to main</h1>"

@app.route("/<name>")
def any(name):
    return f"Hello This is Page <h1>WELCOME...to {name}</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("any", name="admiin"))

if __name__ == "__main__":
    app.run()