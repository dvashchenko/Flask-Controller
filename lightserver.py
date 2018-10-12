from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from flask_codemirror import CodeMirror
from flask import request
import subprocess

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

@app.route("/v1")
def index():
    return render_template('v1.html')

@app.route("/run", methods = ['POST'])
def runcode():
    code = request.form['code']

    f = open('userCode/code.py', 'w')
    f.write(code)
    f.close()

    result = subprocess.Popen(['python', 'userCode/code.py'], stdout=subprocess.PIPE)
    output = result.communicate()[0]

    return output


if __name__ =='__main__':
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True;
    app.run(debug=True)
