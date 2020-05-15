import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, url_for, redirect, request, session, flash, jsonify, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_mail import Mail, Message
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required
from user import User

app = Flask(__name__)
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

app.config['MAIL_SERVER']= os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.route('/')
@app.route('/home')
def home():
    """Return a rendered template of the HOME page with data passed to page

    Retrieve data from skills, projects (limited in number), qualifications 
    and experience collections from MongoDB Atlas.  Return a rendered template 
    of the home page and pass the retrieved data to it
    """
    skills = mongo.db.skills.find()
    projects = mongo.db.portfolio.find().limit(3)
    qualifications = mongo.db.qualifications.find()
    experience = mongo.db.work_experience.find()
    return render_template(
        'pages/index.html', 
        skills=skills, 
        projects=projects,
        qualifications=qualifications,
        experience=experience,
        image_height='full-screen'
    )


@app.route('/about')
def about():
    """Return a rendered template of the ABOUT page"""
    return render_template(
        'pages/about.html', 
        view='about'
    )


@app.route('/projects')
def projects():
    """Return a rendered template of the PROJECTS page with data passed to page
    
    Retrieve all projects from the PORTFOLIO collection from MongoDB Atlas.
    Return a rendered template of the PROJECTS page and pass data to it
    """
    projects = mongo.db.portfolio.find()
    return render_template(
        'pages/projects.html', 
        projects=projects, 
        view='projects'
    )


@app.route('/project/<project_id>')
def project(project_id):
    """Return a rendered template of a specific PROJECT PAGE based on Id

    Convert the Id passed here from url_for in a PROJECT CARD into bson
    format.  Use the converted Id value to retrieve data for a specific 
    project from MongoDB Atlas.  Return a rendered remplate of a specific
    PROJECT PAGE and pass data to it 
    """
    project = mongo.db.portfolio.find_one({'_id': ObjectId(project_id)})
    return render_template(
        'pages/project.html', 
        project=project, 
        view='project'
    )


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Return a rendered template of the CONTACT page or send email"""
    if request.method == 'GET':
        return render_template('pages/contact.html', view='contact')
    elif request.method == 'POST':
        recipient = os.environ.get('RECIPIENT_ADDRESS')
        msg = Message(request.form['subject'], 
                      sender = request.form['email'], 
                      recipients = [recipient])
        msg.body = request.form['query']
        print(request.form)
        mail.send(msg)
        return redirect('home')


@app.route('/blogs')
def blogs():
    """Return a rendered template with all blog data of the BLOGS page
    
    Retrieve all blog posts from MongoDB altas blog_posts collection.
    Return a rendered template of the BLOGS page and send data to it
    """
    blog_posts = mongo.db.blog_posts.find()
    return render_template(
        'pages/blogs.html', 
        blog_posts=blog_posts, 
        view='blogs'
    )


@app.route('/blogs/<blog_id>')
def blog_entry(blog_id):
    """Return a rendered template of a spefic BLOG POST based on Id
    
    Convert the Id passed here from url_for in a BLOG POST CARD into bson
    format.  Use the converted Id value to retrieve data for a specific 
    blog entry from the blog_posts collection in MongoDB Atlas.  Return a 
    rendered remplate of a specific BLOG POST PAGE and pass data to it 
    """
    blog_entry = mongo.db.blog_posts.find_one({'_id': ObjectId(blog_id)})
    return render_template(
        'pages/blog-entry.html', 
        blog_entry=blog_entry, 
        view='blog post'
    )


@app.route('/admin')
@login_required
def admin():
    """Return a rendered template of the ADMIN page and pass data to it
    
    Retrieve all documents from the skills, portfolio, qualifications,
    work_experience and blog_posts collections. Return a rendered template
    of the ADMIN page and pass all retrieved data to it
    """
    skill_count = mongo.db.skills.count()
    project_count = mongo.db.portfolio.count()
    qualification_count = mongo.db.qualifications.count()
    experience_count = mongo.db.work_experience.count()
    blog_posts_count = mongo.db.blog_posts.count()

    return render_template(
        'pages/admin/admin.html', 
        skill_count=skill_count,
        project_count=project_count,
        qualification_count=qualification_count,
        experience_count=experience_count,
        blog_posts_count=blog_posts_count
    )


@app.route('/admin/skills')
@login_required
def manage_skills():
    """Return a rendered template of SKILLS page with all skills sent to it"""
    skills = mongo.db.skills.find()
    return render_template(
        'pages/admin/skills.html', 
        skills=skills, 
        view='admin'
    )


@app.route('/admin/skills/add', methods=['POST'])
@login_required
def add_skill():
    """Insert a new document into skills collection"""
    if request.method == 'POST':
        try:
            skills = mongo.db.skills
            skill_to_insert_dict = request.get_json()
            skills.insert_one(skill_to_insert_dict)
            find_inserted_skill = skills.find_one({'skill_name': skill_to_insert_dict['skill_name']})
            
            if find_inserted_skill:
                flash('Skill added successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to add skill.', 'failure')
                response = make_response(jsonify({'message': 'failed'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'failed'}), 500)
    return response


@app.route('/admin/skills/update/<skill_id>', methods=['GET', 'PUT'])
@login_required
def update_skill(skill_id):
    """Update a skill based on its Id"""
    skills = mongo.db.skills
    if request.method == 'GET':
        skill_to_return = skills.find_one({'_id': ObjectId(skill_id)})
        del skill_to_return['_id']
        response = make_response(jsonify(skill_to_return), 200)
    elif request.method == 'PUT':
        skill_to_update_dict = request.get_json()
        skills.update({'_id': ObjectId(skill_id)},
        {
            'skill_name': skill_to_update_dict['skill_name'],
            'skill_level': skill_to_update_dict['skill_level']
        })

        flash('Skill updated successfully!', 'success')
        response = make_response(jsonify({'message': 'success'}), 200)
    return response


@app.route('/admin/skills/delete/<skill_id>', methods=['DELETE'])
@login_required
def delete_skill(skill_id):
    """Remove a skill from skills collection based on Id"""
    if request.method == 'DELETE':
        skills = mongo.db.skills
        skills.remove({'_id': ObjectId(skill_id)})
        skill_to_confirm_deleted = skills.find_one({'_id': ObjectId(skill_id)})

        if not skill_to_confirm_deleted:
            flash('Skill deleted successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to delete skill.', 'failure')
            response = make_response(jsonify({'message': 'failure'}), 503)
    return response


@app.route('/admin/projects')
@login_required
def manage_projects():
    """Return a rendered template of PROJECTS page with all projects sent to it"""
    projects = mongo.db.portfolio.find()
    technologies = mongo.db.technologies.find()
    technology_list = technologies[0]['technology_name']
    return render_template(
        'pages/admin/projects.html', 
        projects=projects, 
        technology_list=technology_list,
        view='admin'
    )


@app.route('/admin/projects/add', methods=['POST'])
@login_required
def add_project():
    """Insert a new document into portfolio collection"""
    if request.method == 'POST':
        projects = mongo.db.portfolio
        project_to_insert_dict = request.get_json()
        projects.insert_one(project_to_insert_dict)
        find_inserted_project = projects.find_one({'project_name': project_to_insert_dict['project_name']})
        
        if find_inserted_project:
            flash('Project added successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to add project.', 'failure')
            response = make_response(jsonify({'message': 'failed'}), 503)
    return response


@app.route('/admin/projects/update/<project_id>', methods=['GET', 'PUT'])
@login_required
def update_project(project_id):
    portfolio = mongo.db.portfolio
    if request.method == 'GET':
        project_to_return = portfolio.find_one({'_id': ObjectId(project_id)})
        del project_to_return['_id']
        response = make_response(jsonify(project_to_return), 200)
    elif request.method == 'PUT':
        project_to_update_dict = request.get_json()
        portfolio.update({'_id': ObjectId(project_id)}, project_to_update_dict)
        flash('Project updated successfully!', 'success')
        response = make_response(jsonify({'message': 'success'}), 200)
    return response


@app.route('/admin/projects/delete/<project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id):
    """Remove a project from portfolio collection based on Id"""
    if request.method == 'DELETE':
        projects = mongo.db.portfolio
        projects.remove({'_id': ObjectId(project_id)})
        project_to_confirm_deleted = projects.find_one({'_id': ObjectId(project_id)})

        if not project_to_confirm_deleted:
            flash('Project deleted successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to delete project.', 'failure')
            response = make_response(jsonify({'message': 'failure'}), 503)
    return response


@app.route('/admin/qualifications')
@login_required
def manage_qualifications():
    """Return a rendered template of MANAGE QUALIFICATIONS page
    
    Retrieve all qualification documents from the qualifications collection.  
    Pass retrieved data to a rendered template of the MANMAGE QUALIFICATIONS page.
    """
    qualifications = mongo.db.qualifications.find()
    return render_template(
        'pages/admin/qualifications.html', 
        qualifications=qualifications,
        view='admin'
    )


@app.route('/admin/qualifications/add', methods=['POST'])
@login_required
def add_qualification():
    """Insert a new document into qualifications collection"""
    if request.method == 'POST':
        qualifications = mongo.db.qualifications
        qualification_to_insert = request.get_json()
        qualifications.insert_one(qualification_to_insert)
        find_inserted_qualification = qualifications.find_one({'qualification_name': qualification_to_insert['qualification_name']})
        
        if find_inserted_qualification:
            flash('Qualification added successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to delete qualification.', 'failure')
            response = make_response(jsonify({'message': 'failed'}), 503)
    return response


@app.route('/admin/qualifications/update/<qualification_id>', methods=['GET', 'PUT'])
@login_required
def update_qualification(qualification_id):
    """Update a qualification based on its Id"""
    qualifications = mongo.db.qualifications
    if request.method == 'GET':
        qualification_to_return = qualifications.find_one({'_id': ObjectId(qualification_id)})
        del qualification_to_return['_id']
        response = make_response(jsonify(qualification_to_return), 200)
    elif request.method == 'PUT':
        qualification_to_update_dict = request.get_json()
        qualifications.update({'_id': ObjectId(qualification_id)},
            {
                'qualification_name': qualification_to_update_dict['qualification_name'],
                'qualification_from': qualification_to_update_dict['qualification_from'],
                'qualification_issue_date': qualification_to_update_dict['qualification_issue_date'],
                'qualification_view_url': qualification_to_update_dict['qualification_view_url'],
                'qualification_info_url': qualification_to_update_dict['qualification_info_url']
            })
        flash('Qualification updated successfully!', 'success')
        response = make_response(jsonify({'message': 'success'}), 200)
    return response


@app.route('/admin/qualifications/delete/<qualification_id>', methods=['DELETE'])
@login_required
def delete_qualification(qualification_id):
    """Remove a qualification from qualifications collection based on Id"""
    if request.method == 'DELETE':
        qualifications = mongo.db.qualifications
        qualifications.remove({'_id': ObjectId(qualification_id)})
        qualification_to_confirm_deleted = qualifications.find_one({'_id': ObjectId(qualification_id)})

        if not qualification_to_confirm_deleted:
            flash('Qualification deleted successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to delete qualification.', 'failure')
            response = make_response(jsonify({'message': 'failure'}), 503)
    return response


@app.route('/admin/blogs')
@login_required
def manage_blogs():
    """Return a rendered template of BLOGS page with all blog posts sent to it"""
    blog_posts = mongo.db.blog_posts.find()
    return render_template(
        'pages/admin/blogs.html', 
        blog_posts=blog_posts,
        view='admin'
    )


@app.route('/admin/blogs/add', methods=['POST'])
@login_required
def add_blog_post():
    """Insert a new document into blog_posts collection"""
    if request.method == 'POST':
        blog_posts = mongo.db.blog_posts
        blog_post_to_insert_dict = request.get_json()
        blog_posts.insert_one(blog_post_to_insert_dict)
        find_inserted_blog_post = blog_posts.find_one({'blog_title': blog_post_to_insert_dict['blog_title']})
        
        if find_inserted_blog_post:
            flash('Blog post added successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to add blog post', 'failure')
            response = make_response(jsonify({'message': 'failed'}), 503)
    return response


@app.route('/admin/blogs/update/<blog_post_id>', methods=['GET','PUT'])
@login_required
def update_blog_post(blog_post_id):
    """Update a blog post based on its Id"""
    blog_posts = mongo.db.blog_posts
    if request.method == 'GET':
        blog_post_to_return = blog_posts.find_one({'_id': ObjectId(blog_post_id)})
        del blog_post_to_return['_id']
        response = make_response(jsonify(blog_post_to_return), 200)
    elif request.method == 'PUT':
        blog_post_to_update_dict = request.get_json()
        blog_posts.update({'_id': ObjectId(blog_post_id)},
            {
                'blog_title': blog_post_to_update_dict['blog_title'],
                'blog_img_url': blog_post_to_update_dict['blog_img_url'],
                'blog_summary': blog_post_to_update_dict['blog_summary'],
                'blog_date': blog_post_to_update_dict['blog_date'],
                'blog_body': blog_post_to_update_dict['blog_body']
            })
        flash('Blog post successfully updated!', 'success')
        response = make_response(jsonify({'message': 'success'}), 200)
    return response


@app.route('/admin/blogs/delete/<blog_post_id>', methods=['DELETE'])
@login_required
def delete_blog_post(blog_post_id):
    """Remove a blog post from blog_posts collection based on Id"""
    if request.method == 'DELETE':
        blog_posts = mongo.db.blog_posts
        blog_posts.remove({'_id': ObjectId(blog_post_id)})
        blog_post_to_confirm_deleted = blog_posts.find_one({'_id': ObjectId(blog_post_id)})

        if not blog_post_to_confirm_deleted:
            flash('Blog post deleted successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to delete blog post', 'failure')
            response = make_response(jsonify({'message': 'failure'}), 503)
    return response

@app.route('/admin/experience')
@login_required
def manage_experience():
    """Return a rendered template of EXPERIENCE page with all work experience sent to it"""
    experience = mongo.db.work_experience.find()
    return render_template(
        'pages/admin/experience.html', 
        experience=experience,
        view='admin'
    )


@app.route('/admin/experience/add', methods=['POST'])
@login_required
def add_experience():
    """Insert a new document into experience collection"""
    if request.method == 'POST':
        experience = mongo.db.work_experience
        experience_to_insert_dict = request.get_json()
        experience.insert_one(experience_to_insert_dict)
        find_inserted_experience = experience.find_one({'job_title': experience_to_insert_dict['job_title']})
        
        if find_inserted_experience:
            flash('Experience added successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to add experience.', 'failure')
            response = make_response(jsonify({'message': 'failed'}), 503)
    return response


@app.route('/admin/experience/update/<experience_id>', methods=['GET','PUT'])
@login_required
def update_experience(experience_id):
    """Update experience document based on its Id"""
    experience = mongo.db.work_experience
    if request.method == 'GET':
        experience_to_return = experience.find_one({'_id': ObjectId(experience_id)})
        del experience_to_return['_id']
        response = make_response(jsonify(experience_to_return), 200)
    elif request.method == 'PUT':
        experience_to_update_dict = request.get_json()
        experience.update({'_id': ObjectId(experience_id)},
        {
            'job_title': experience_to_update_dict['job_title'],
            'job_dates': experience_to_update_dict['job_dates']
        })
        flash('Experience updated successfully!', 'success')
        response = make_response(jsonify({'message': 'success'}), 200)
    return response


@app.route('/admin/experience/delete/<experience_id>', methods=['DELETE'])
@login_required
def delete_experience(experience_id):
    """Remove a work experience document from work_experience collection based on Id"""
    if request.method == 'DELETE':
        experience = mongo.db.work_experience
        experience.remove({'_id': ObjectId(experience_id)})
        experience_to_confirm_deleted = experience.find_one({'_id': ObjectId(experience_id)})

        if not experience_to_confirm_deleted:
            flash('Experience deleted successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            flash('Failed to delete experience', 'failure')
            response = make_response(jsonify({'message': 'failure'}), 503)
    return response


@login_manager.user_loader
def load_user(email):
    """Gets information for a specific user from the database"""
    users = mongo.db.users
    user = users.find_one({'email': email})
    if not user:
        return None
    else:
        return User(email=user['email'], password=user['password'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Verifies login form information and logs a user in if valid ceredntials are provided"""
    if request.method == 'POST':
        users = mongo.db.users
        find_user = users.find_one({'email': request.form['email']})
        if find_user and bcrypt.check_password_hash(find_user['password'], request.form['password']):
            user = User(find_user['email'], find_user['password'])
            login_user(user)
            return redirect(url_for('admin'))
        flash('The login details you provided are incorrect', 'info')
    return render_template(
        'pages/login.html', 
        view='login'
    )


@app.route("/logout")
@login_required
def logout():
    """Logs a user out and destroys session data"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(e):
    """Returns a rendered template of the 404.html page"""
    return render_template(
        'pages/404.html', 
        image_height='full-screen',
        view='404'
    ), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEBUG_VALUE'))