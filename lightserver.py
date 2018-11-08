import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from flask_codemirror import CodeMirror
from flask import request
from subprocess import Popen, PIPE, STDOUT

CODEMIRROR_LANGUAGES = ['python', 'html']
SECRET_KEY='secret!'
CODEMIRROR_THEME = '3024-night'
CODEMIRROR_ADDONS = (
            ('display','placeholder'),
)

app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)
Bootstrap(app)

@app.route('/')
def test():
    return render_template('v2.html')

@app.route("/run", methods = ['POST'])
def runcode():
    code = request.form['code']
    input = request.form['input']

    f = open('userCode/code.py', 'w')
    f.write(code)
    f.close()

    f = open('userCode/input.txt', 'w') #user input must be concatenated
    f.write(input)
    f.close()

    result = Popen("python userCode/code.py < userCode/input.txt", stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True, preexec_fn=os.setsid) 
    output = result.communicate()[0]

    return output


if __name__ =='__main__':
    app.run(debug=True)
