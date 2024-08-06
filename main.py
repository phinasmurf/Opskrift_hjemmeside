from flask import Flask, send_from_directory, Request

app = Flask(__name__)

@app.route('/')
def hello():
    file = open('main.html', 'r')
    content = file.read()
    file.close()
    return content

def i_anden(i):
    return i**2

@app.route("/hej/<a>/<b>/<c>")
def hello_navn(a, b, c):
    svar = a, b, c = int(a), int(b), int(c)
    
    return svar

#app.run(port=3000)