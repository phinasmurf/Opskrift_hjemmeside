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

    try:
        svar = int(a), int(b), int(c)
        division = int(a) / int(b) / int(c)

    except ValueError as fejl:
        return "der er en valueerror: " + fejl.args[0]

    except ZeroDivisionError:
        return "vi ka ikke dividere med nul"

    return f"{svar} divideret sammen er lig {division}"

app.run(port=3000)