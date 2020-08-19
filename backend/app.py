import logging, os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from backend.db_manager import db


logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()

def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    from backend.views.user_views import user_app
    from backend.views.quiz_views import quiz_app
    from backend.views.player_views import player_app
    from backend.views.game_views import game_app
    app.register_blueprint(user_app)
    app.register_blueprint(quiz_app)
    app.register_blueprint(player_app)
    app.register_blueprint(game_app)

def run_manager(app):
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()

def run_app(app):
    app.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    from manager import app
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    register_extensions(app)
    register_blueprints(app)
    run_manager(app)
    run_app(app)