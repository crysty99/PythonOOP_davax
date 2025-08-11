from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests.db'
db = SQLAlchemy(app)

# Import routes to register them with the app
from . import routes

# if __name__ == '__main__':
#     app.run(debug=True)
