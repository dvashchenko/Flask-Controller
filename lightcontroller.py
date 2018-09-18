from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from flask_codemirror import CodeMirror

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(
SECRET_KEY='secret!'
CODEMIRROR_LANGUAGES = ['python', 'html']
)
codemirror = CodeMirror(app)


class MyForm(Form):
    source_code = CodeMirrorField(language='python', config={'lineNumbers' : 'true'})
    submit = SubmitField('Submit')

@app.route('/test', methods = ['GET', 'POST'])
def test():
    form = MyForm()
    if form.validate_on_submit():
        text = form.source_code.data
    return render_template('test.html', form = form)


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True)
