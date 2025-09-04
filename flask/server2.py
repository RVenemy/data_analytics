from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello This is Main Page <h1>WELCOME...to main</h1>"

@app.route("/home")
def home():
    return "Hello This is Main Page <h1>WELCOME...to home</h1>"

if __name__ == "__main__":
    app.run()