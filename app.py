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
@app.route('/home')
def home():
    """
    Retrieve data from MongoDB Atlas and return a rendered template 
    which passes the data to the home page
    """
    skills = mongo.db.skills.find()
    projects = mongo.db.portfolio.find().limit(3)
    qualifications = mongo.db.qualifications.find()
    experience = mongo.db.work_experience.find()

    return render_template('pages/index.html', 
                            skills=skills, 
                            projects=projects,
                            qualifications=qualifications,
                            experience=experience)


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


@app.route('/blogs')
def blogs():
    blog_posts = mongo.db.blog_posts.find()
    return render_template('pages/blogs.html', blog_posts=blog_posts)


@app.route('/blogs/<blog_id>')
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

    return render_template('pages/admin.html', skill_count=skill_count,
                                                project_count=project_count,
                                                qualification_count=qualification_count,
                                                experience_count=experience_count,
                                                blog_posts_count=blog_posts_count)


@app.route('/admin/add_skill', methods=['GET','POST'])
def add_skill():
    if request.method == 'POST':
        skills = mongo.db.skills
        skills.insert_one(request.form.to_dict())
        return redirect('add_skill')
    return render_template('pages/add_skill.html')


@app.route('/admin/manage_skills')
def manage_skills():
    return render_template('pages/manage_skills.html', skills=mongo.db.skills.find())


@app.route('/admin/edit_skill/<skill_id>')
def edit_skill(skill_id):
    skill = mongo.db.skills.find_one({'_id': ObjectId(skill_id)})
    return render_template('pages/edit_skill.html', skill=skill)


@app.route('/admin/update_skill/<skill_id>', methods=['POST'])
def update_skill(skill_id):
    if request.method == 'POST':
        skills = mongo.db.skills
        skills.update({'_id': ObjectId(skill_id)},
        {
            'skill_name': request.form.get('skill_name'),
            'skill_img_url': request.form.get('skill_img_url'),
            'skill_level': request.form.get('skill_level')
        })

        return redirect(url_for('admin'))
    else:
        return redirect(url_for('edit_skill'))


@app.route('/admin/delete_skill/<skill_id>')
def delete_skill(skill_id):
    mongo.db.skills.remove({'_id': ObjectId(skill_id)})
    return redirect(url_for('manage_skills'))


@app.route('/admin/add_project', methods=['GET','POST'])
def add_project():
    technologies = mongo.db.technologies.find()
    technology_list = technologies[0]['technology_name']
    if request.method == 'POST':
        projects = mongo.db.portfolio
        form_body = request.form.to_dict()
        form_body['project_description'] = request.form.getlist('project_description')
        form_body['project_technologies'] = request.form.getlist('project_technologies')
        projects.insert_one(form_body)
        return redirect('add_project')
    return render_template('pages/add_project.html', technology_list=technology_list)


@app.route('/admin/manage_projects')
def manage_projects():
    return render_template('pages/manage_projects.html', projects=mongo.db.portfolio.find())


@app.route('/admin/edit_project/<project_id>')
def edit_project(project_id):
    project = mongo.db.portfolio.find_one({'_id': ObjectId(project_id)})
    technologies = mongo.db.technologies.find()
    technology_list = technologies[0]['technology_name']
    return render_template('pages/edit_project.html', project=project, technology_list=technology_list)


@app.route('/admin/update_project/<project_id>', methods=['POST'])
def update_project(project_id):
    if request.method == 'POST':
        portfolio = mongo.db.portfolio
        portfolio.update({'_id': ObjectId(project_id)},
        {
            'project_name': request.form.get('project_name'),
            'project_img_url': request.form.get('project_img_url'),
            'project_github_url': request.form.get('project_github_url'),
            'project_deployed_url': request.form.get('project_deployed_url'),
            'project_technologies': request.form.getlist('project_technologies'),
            'project_description': request.form.getlist('project_description')
        })

        return redirect(url_for('admin'))
    else:
        return redirect(url_for('edit_project'))


@app.route('/admin/delete_project/<project_id>')
def delete_project(project_id):
    mongo.db.portfolio.remove({'_id': ObjectId(project_id)})
    return redirect(url_for('manage_projects'))


@app.route('/admin/add_qualification', methods=['GET','POST'])
def add_qualification():
    if request.method == 'POST':
        qualifications = mongo.db.qualifications
        qualifications.insert_one(request.form.to_dict())
        return redirect('add_qualification')
    return render_template('pages/add_qualification.html')


@app.route('/admin/manage_qualifications')
def manage_qualifications():
    return render_template('pages/manage_qualifications.html', qualifications=mongo.db.qualifications.find())


@app.route('/admin/edit_qualification/<qualification_id>')
def edit_qualification(qualification_id):
    qualification = mongo.db.qualifications.find_one({'_id': ObjectId(qualification_id)})
    
    return render_template('pages/edit_qualification.html', qualification=qualification)


@app.route('/admin/update_qualification/<qualification_id>', methods=['POST'])
def update_qualification(qualification_id):
    if request.method == 'POST':
        qualifications = mongo.db.qualifications
        qualifications.update({'_id': ObjectId(qualification_id)},
        {
            'qualification_name': request.form.get('qualification_name'),
            'qualification_from': request.form.get('qualification_from'),
            'qualification_issue_date': request.form.get('qualification_issue_date'),
            'qualification_view_url': request.form.get('qualification_view_url'),
            'qualification_info_url': request.form.getlist('qualification_info_url')
        })

        return redirect(url_for('admin'))
    else:
        return redirect(url_for('edit_project'))


@app.route('/admin/delete_qualification/<qualification_id>')
def delete_qualification(qualification_id):
    mongo.db.qualifications.remove({'_id': ObjectId(qualification_id)})
    return redirect(url_for('manage_qualifications'))


@app.route('/admin/add_blog_post', methods=['GET','POST'])
def add_blog_post():
    if request.method == 'POST':
        blog_posts = mongo.db.blog_posts
        form_body = request.form.to_dict()
        form_body['blog_body'] = request.form.getlist('blog_body')
        blog_posts.insert_one(form_body)
        return redirect('add_blog_post')
    return render_template('pages/add_blog_post.html')


@app.route('/admin/manage_blogs')
def manage_blogs():
    return render_template('pages/manage_blogs.html', blog_posts=mongo.db.blog_posts.find())


@app.route('/admin/edit_blog_post/<blog_post_id>')
def edit_blog_post(blog_post_id):
    blog_post = mongo.db.blog_posts.find_one({'_id': ObjectId(blog_post_id)})
    return render_template('pages/edit_blog_post.html', blog_post=blog_post)


@app.route('/admin/update_blog_post/<blog_post_id>', methods=['POST'])
def update_blog_post(blog_post_id):
    if request.method == 'POST':
        blog_posts = mongo.db.blog_posts
        blog_posts.update({'_id': ObjectId(blog_post_id)},
        {
            'blog_title': request.form.get('blog_title'),
            'blog_title': request.form.get('blog_title'),
            'blog_summary': request.form.get('blog_summary'),
            'blog_date': request.form.get('blog_date'),
            'blog_body': request.form.getlist('blog_body')
        })

        return redirect(url_for('admin'))
    else:
        return redirect(url_for('edit_blog_post'))


@app.route('/admin/delete_blog_post/<blog_post_id>')
def delete_blog_post(blog_post_id):
    mongo.db.blog_posts.remove({'_id': ObjectId(blog_post_id)})
    return redirect(url_for('manage_blogs'))


@app.route('/admin/add_experience', methods=['GET','POST'])
def add_experience():
    if request.method == 'POST':
        experience = mongo.db.work_experience
        form_body = request.form.to_dict()
        experience.insert_one(form_body)
        return redirect('add_experience')
    return render_template('pages/add_experience.html')


@app.route('/admin/manage_experience')
def manage_experience():
    return render_template('pages/manage_experience.html', experience=mongo.db.work_experience.find())


@app.route('/admin/edit_experience/<experience_id>')
def edit_experience(experience_id):
    experience = mongo.db.work_experience.find_one({'_id': ObjectId(experience_id)})

    return render_template('pages/edit_experience.html', experience=experience)

@app.route('/admin/update_experience/<experience_id>', methods=['POST'])
def update_experience(experience_id):
    if request.method == 'POST':
        experience = mongo.db.work_experience
        experience.update({'_id': ObjectId(experience_id)},
        {
            'job_title': request.form.get('job_title'),
            'job_dates': request.form.get('job_dates')
        })

        return redirect(url_for('admin'))
    else:
        return redirect(url_for('edit_experience'))


@app.route('/admin/delete_experience/<experience_id>')
def delete_experience(experience_id):
    mongo.db.work_experience.remove({'_id': ObjectId(experience_id)})
    return redirect(url_for('manage_experience'))


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