from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = 'POST'>
            <div>Rotate By:
                <input name="rot" value='0' type="text"/>
            </div>
            <div>
                <textarea input type="text" name="text">{0}</textarea>
            </div>
            <input type="submit" />
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format(rot='', text = '')


@app.route("/", methods = ['POST'])
def encrypt():
    rot = request.form["rot"]
    rot = int(rot)
    text = request.form["text"]
    encryption = rotate_string(text,rot)
    return form.format(encryption)



app.run()
