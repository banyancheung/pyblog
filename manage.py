from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from pylog import create_app, db
from pylog.models.User import User as UserModel
from pylog.models.Setting import Setting as SettingModel

app = create_app()
manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(db=db, UserModel=UserModel, SettingModel=SettingModel)


@manager.command
def install():
    from flask_migrate import upgrade
    from pylog.models.User import User as UserModel
    upgrade()
    # add admin user record
    UserModel.init_admin(user_name='admin', password='admin888')
    # init site settings
    SettingModel.init_setting()


if __name__ == '__main__':
    manager.run()
