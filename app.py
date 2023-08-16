from flask import Flask

from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)
app.secret_key = 'GrapesNotLemonade43'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
