from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello This is Main Page <h1>WELCOME...to main</h1>"

@app.route("/home")
def home():
    return "Hello This is Main Page <h1>WELCOME...to home</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run()