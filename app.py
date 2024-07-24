from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá"

@app.route("/teste")
def teste():
    return "Página de teste"

if __name__ == "__main__":
    app.run()