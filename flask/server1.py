from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello This is Main Page <h1>WELCOME...</h1>"

if __name__ == "__main__":
    app.run()