import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, url_for, redirect, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_mail import Mail, Message


app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

app.config['MAIL_SERVER']= os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    return render_template('pages/index.html', 
                            skills=mongo.db.skills.find(), 
                            projects=mongo.db.portfolio.find().limit(3),
                            qualifications=mongo.db.qualifications.find(),
                            experience=mongo.db.work_experience.find())


@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/portfolio')
def portfolio():
    projects = mongo.db.portfolio.find()
    return render_template('pages/portfolio.html', projects=projects)


@app.route('/project/<project_id>')
def project(project_id):
    project = mongo.db.portfolio.find_one({'_id': ObjectId(project_id)})
    return render_template('pages/project.html', project=project)


@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


@app.route('/send_mail', methods=['POST'])
def send_mail():
    if request.method == 'POST':
        print(request.form)
        recipient = os.environ.get('RECIPIENT_ADDRESS')
        msg = Message(request.form['subject'], sender = request.form['email'], recipients = [recipient])
        msg.body = request.form['query']
        mail.send(msg)
    return redirect('contact')


@app.route('/blog')
def blog():
    blog_posts = mongo.db.blog_posts.find()
    return render_template('pages/blog.html', blog_posts=blog_posts)


@app.route('/blog/<blog_id>')
def blog_entry(blog_id):
    blog_entry = mongo.db.blog_posts.find_one({'_id': ObjectId(blog_id)})
    return render_template('pages/blog_entry.html', blog_entry=blog_entry)


@app.route('/admin')
def admin():
    skill_count = mongo.db.skills.count()
    project_count = mongo.db.portfolio.count()
    qualification_count = mongo.db.qualifications.count()
    experience_count = mongo.db.work_experience.count()
    blog_posts_count = mongo.db.blog_posts.count()
    total_db_count = str(int(skill_count) + int(project_count) + int(qualification_count) + int(experience_count) + int(blog_posts_count))

    return render_template('pages/admin.html', skills=mongo.db.skills.find(),
                                                skill_count=skill_count,
                                                projects=mongo.db.portfolio.find(),
                                                project_count=project_count,
                                                qualifications=mongo.db.qualifications.find(),
                                                qualification_count=qualification_count,
                                                experience=mongo.db.work_experience.find(),
                                                experience_count=experience_count,
                                                blog_posts=mongo.db.blog_posts.find(),
                                                blog_posts_count=blog_posts_count,
                                                total_db_count=total_db_count)


@app.route('/login')
def login():
    # if 'username' in session:
    #     return redirect(url_for('admin'))
    return redirect(url_for('admin'))
    # return render_template('pages/login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)