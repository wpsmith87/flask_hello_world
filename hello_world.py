from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="https://unsplash.com/photos/48bZh32St1Q">
    """
    return html.format(name.title())
    
@app.route("/jedi/<fname>/<lname>")
def jedi_name(fname, lname):
    name = lname[0:3] + fname[0:2]
    return "Your Jedi name is {}".format(name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
