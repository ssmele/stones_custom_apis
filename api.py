from flask import Flask
from flask import render_template
from flask_restful import Api
from controllers import helloController
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

@app.route('/')
def home():
    return render_template('index.html')

db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/hello')

if __name__ == '__main__':
    app.run(debug=True)
