'''
    此文件仅作为开启flask程序的入口，没有包含任何开发逻辑
'''

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from ihome import create_app, db


app = create_app("develop")
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == "__main__":
    manager.run()