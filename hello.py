from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtfomrs import StringField, SubmitField
from wtforms import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)

moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('what is your name', validators=[DataRequired()])
    submit = SubmitField('submit')


app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template(500), 500

