from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)

   app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome home"

if __name__ == "__main__":
    app.run(debug=True) 

    app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome back"

if __name__ == "__main__":
    app.run(debug=True)