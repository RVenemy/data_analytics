from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello This is Main Page <h1>WELCOME...to main</h1>"

@app.route("/<name>")
def any(name):
    return f"Hello This is Page <h1>WELCOME...to {name}</h1>"

if __name__ == "__main__":
    app.run()