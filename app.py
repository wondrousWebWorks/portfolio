import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, url_for, redirect, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('pages/index.html', 
                            skills=mongo.db.skills.find(), 
                            projects=mongo.db.portfolio.find().limit(3))


@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/portfolio')
def portfolio():
    return render_template('pages/portfolio.html')


@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


@app.route('/admin')
def admin():
    return render_template('pages/admin.html')

@app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('admin'))
    
    return render_template('pages/login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)