from flask import d
from flask_script import Manager
from pylog import create_app

app = create_app()
manager = Manager(app)

@manager.command
def deploy():
    pass


if __name__ == '__main__':
    manager.run()
