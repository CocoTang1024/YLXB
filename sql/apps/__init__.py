from flask import Flask

import settings
from apps.user.view import user_bp
from exts import db


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(settings.DevelopmentConfig)
    # 将db对象与app进行了关联
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    # 检查路由
    # print(app.url_map)
    return app
