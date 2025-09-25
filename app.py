import os
import sqlite3
from flask import Flask, g

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key-change-me')

DB_PATH = os.path.join(app.root_path, 'questions.db')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
