from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
# 导入模型
from apps.user.models import User
from apps import create_app
from exts import db

# app = Flask(__name__)
app = create_app()
manager = Manager(app=app)
# 命令工具
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(
    port="5001"
))

if __name__ == '__main__':
    manager.run()
