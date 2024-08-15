from flask import Flask, send_from_directory, Request

app = Flask(__name__)

@app.route('/')
def hello():
    file = open('main.html', 'r')
    content = file.read()
    file.close()
    return content
#blahblahohhf

def i_anden(i):
    return i**2

@app.route("/<a>/<b>/<c>")
def hello_navn(a, b, c):
    svar = int(a), int(b), int(c)

    return str(svar)

app.run(port=3000)