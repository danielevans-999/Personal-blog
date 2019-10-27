from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Post,Comment
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')

manage = Manager(app)
migrate = (app,db)
manage.add_command('db',MigrateCommand)
manage.add_command('server',Server)

@manage.shell
def make_shell_context():
    return dict(app=app, User=User, Post=Post, Comment=Comment)

if __name__ == '__main__':
    manage.run()
