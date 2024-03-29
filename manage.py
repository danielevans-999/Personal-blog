from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Post,Comment
from flask_migrate import Migrate,MigrateCommand

#creating app instance
app = create_app('development')

manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)
manage.add_command('server',Server)


@manage.command
def test():
    '''Run the unit tests.'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manage.shell
def make_shell_context():
    return dict(app = app, db = db , User = User, Post = Post, Comment = Comment)

if __name__ == '__main__':
    manage.run()
