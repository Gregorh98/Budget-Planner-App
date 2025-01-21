from flask import Flask

from blueprints import auth_bp, general_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)

if __name__ == '__main__':
    app.run()
