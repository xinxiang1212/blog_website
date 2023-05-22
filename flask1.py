import os
import click
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role, Post, Permission

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission)


@app.cli.command()
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@click.command()
def update_user_roles():
    users = User.query.all()
    for user in users:
        if user.role is None:
            if user.email == current_app.config['FLASKY_ADMIN']:
                user.role = Role.query.filter_by(name='Administrator').first()
            if user.role is None:
                user.role = Role.query.filter_by(default=True).first()
            db.session.add(user)
    db.session.commit()
    print('User roles have been updated!')


# Overall, this code sets up the Flask application, configures the
# database migration, provides a shell context,
# and defines CLI commands for running tests and updating user roles.
# It demonstrates the common tasks and functionality used in a Flask application.