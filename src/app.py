from flask import Flask
from config import config_env
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(db):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config_env['psg_uri']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    from routes.blueprint import category_blueprint
    app.register_blueprint(category_blueprint, url_prefix="/category")
    app.run(debug=True, host='0.0.0.0', port=config_env['api_port'])

if __name__ == "__main__":
    create_app(db)