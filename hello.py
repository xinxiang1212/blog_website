from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(FlaskForm):
    name = StringField('what is your name', validators=[DataRequired()])
    submit = SubmitField('submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'))

