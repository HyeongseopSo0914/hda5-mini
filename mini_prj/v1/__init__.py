from flask import Flask
from flask import render_template

######추가######
from flask_login import LoginManager # install
from flask_migrate import Migrate # DB 관리
from flask_sqlalchemy import SQLAlchemy # SQL Query 관리
###############
##
from .views import main_view

# 확장 모듈 초기화
#db = SQLAlchemy()
#login_manager = LoginManager()
#migrate = Migrate()

# 앱 생성 함수
def create_app(config_class):
    app = Flask(__name__)

    # 설정 파일 로드
    app.config.from_object(config_class)

    # 확장 모듈 초기화
    #db.init_app(app)
    #login_manager.init_app(app)
    #migrate.init_app(app, db)

    # Blueprint 등록
    # 직접적으로 Blueprint를 import하여 등록
    from .views import main_view  # main_view는 views.py에서 Blueprint를 정의한다고 가정
    app.register_blueprint(main_view.main_bp)

    # 데이터베이스 초기화 및 마이그레이션
    # 예시: 데이터베이스 마이그레이션 처리 방법을 설정합니다.
    #@app.before_first_request
    #def initialize_database():
        # db.create_all() 대신 마이그레이션을 사용할 수 있습니다.
        # db.create_all()은 초기화 시에만 사용하고, 실제 앱에서는 마이그레이션이 필요합니다.
    #    pass

    #@app.teardown_request
    #def shutdown_session(exception=None):
    #    db.session.remove()

    return app