import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_home')
def get_tasks():
    return render_template('index.html', tasks=mongo.db.tasks.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True)