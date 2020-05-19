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

APP = Flask(__name__)
MAIL = Mail(APP)
BCRYPT = Bcrypt(APP)
LOGINMANAGER = LoginManager(APP)
LOGINMANAGER.login_view = "login"
APP.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')
APP.config['MONGO_URI'] = os.environ.get('MONGO_URI')
MONGO = PyMongo(APP)
APP.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
APP.config['MAIL_SERVER']= os.environ.get('MAIL_SERVER')
APP.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
APP.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
APP.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
APP.config['MAIL_USE_TLS'] = False
APP.config['MAIL_USE_SSL'] = True


@APP.route('/')
def home():
    """
    Retrieve data from skills, projects (limited to 3), qualifications, blog posts 
    and experience collections from MongoDB Atlas.  Return a rendered template 
    of the home page and pass the retrieved data to it, as well as a parameter to
    set the header image to full screen height.
    """
    skills = MONGO.db.skills.find()
    projects = MONGO.db.portfolio.find().limit(3)
    qualifications = MONGO.db.qualifications.find()
    experience = MONGO.db.work_experience.find()
    return render_template(
        'pages/index.html', 
        skills=skills, 
        projects=projects,
        qualifications=qualifications,
        experience=experience,
        image_height='full-screen'
    )


@APP.route('/about')
def about():
    """
    Return a rendered template of the ABOUT page and sends a
    view parameter to affect the Call To Action text and button text
    for the ABOUT page specifically.
    """
    return render_template(
        'pages/about.html', 
        view='about'
    )


@APP.route('/projects')
def projects():
    """
    Retrieve all projects from the PORTFOLIO collection from MongoDB Atlas.
    Return a rendered template of the PROJECTS page and pass data to it. Also
    send a view parameter to affect the Call To Action text and button text for
    the PROJECTS page specifically.
    """
    projects = MONGO.db.portfolio.find()
    return render_template(
        'pages/projects.html', 
        projects=projects, 
        view='projects'
    )


@APP.route('/project/<project_id>')
def project(project_id):
    """
    Convert the ID passed here from url_for in a PROJECT CARD into BSON
    format.  Use the converted ID value to retrieve data for a specific 
    project from the portfolio collection.  Return a rendered remplate of 
    a specific PROJECT PAGE and pass the retrieved data to it as well as
    a view parameter to affect the Call To Action text and button text for
    the PROJECT page specifically.
    """
    project = MONGO.db.portfolio.find_one({'_id': ObjectId(project_id)})
    return render_template(
        'pages/project.html', 
        project=project, 
        view='project'
    )


@APP.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    When receiving a GET request, return a rendered template of the CONTACT page
    and send a view parameter to affect the Call To Action text and button text for
    the CONTACT page specifically.

    When receiving a POST request, construct a message from the request form data
    and send an email. Return a redirect to the HOME page once completed.
    """
    if request.method == 'GET':
        return render_template('pages/contact.html', view='contact')
    elif request.method == 'POST':
        recipient = os.environ.get('RECIPIENT_ADDRESS')
        msg = Message(request.form['subject'], 
                      sender = request.form['email'], 
                      recipients = [recipient])
        msg.body = request.form['query']
        print(request.form)
        MAIL.send(msg)
        return redirect('home')


@APP.route('/blogs')
def blogs():
    """    
    Retrieve all blog posts from the blog_posts collection.
    Return a rendered template of the BLOGS page and send retrieved
    blog posts to it as well as a view parameter to affect the 
    Call To Action text and button text for the BLOGS page specifically.
    """
    blog_posts = MONGO.db.blog_posts.find()
    return render_template(
        'pages/blogs.html', 
        blog_posts=blog_posts, 
        view='blogs'
    )


@APP.route('/blogs/blog-post/<blog_id>')
def blog_entry(blog_id):
    """    
    Convert the ID passed here from url_for in a BLOG POST CARD into BSON
    format.  Use the converted ID value to retrieve data for a specific 
    blog entry from the blog_posts collection.  Return a rendered remplate 
    of a specific BLOG POST PAGE and pass the retrieved data to it as well 
    as a view parameter to affect the Call To Action text and button text 
    for the BLOG ENTRY page specifically.
    """
    blog_entry = MONGO.db.blog_posts.find_one({'_id': ObjectId(blog_id)})
    return render_template(
        'pages/blog-entry.html', 
        blog_entry=blog_entry, 
        view='blog post'
    )


@LOGINMANAGER.user_loader
def load_user(email):
    """
    Gets information for a specific user from the users collection
    and returns a User instance created with the specific user data.
    If the user cannot be found, return nothing.
    
    """
    users = MONGO.db.users
    user = users.find_one({'email': email})
    if not user:
        return None
    else:
        return User(email=user['email'], password=user['password'])


@APP.route('/login', methods=['GET', 'POST'])
def login():
    """
    When the request method is POST, try to find the user in the users collection
    using the email in the request form.  If the user is found, hash the password
    provided in the request form and compare it to the hashed password retrieved
    from the users collection. If the passwords match, log the user in and redirect
    to the Admin page. If the login details are incorrect, flash a message informing
    user and reload the login page. Pass a view parameter that will set the header
    image to less than 100% screen height.
    """
    if request.method == 'POST':
        users = MONGO.db.users
        find_user = users.find_one({'email': request.form['email']})
        if find_user and BCRYPT.check_password_hash(find_user['password'], request.form['password']):
            user = User(find_user['email'], find_user['password'])
            login_user(user)
            return redirect(url_for('admin'))
        flash('The login details you provided are incorrect', 'info')
    return render_template(
        'pages/login.html', 
        view='login'
    )


@APP.route("/logout")
@login_required
def logout():
    """Logs a user out and destroys session data"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


@APP.route('/admin')
@login_required
def admin():
    """    
    Retrieve all documents from the skills, portfolio, qualifications,
    work_experience and blog_posts collections and count them separately. 
    Return a rendered template of the ADMIN page and pass all counts to it
    """
    skill_count = MONGO.db.skills.count()
    project_count = MONGO.db.portfolio.count()
    qualification_count = MONGO.db.qualifications.count()
    experience_count = MONGO.db.work_experience.count()
    blog_posts_count = MONGO.db.blog_posts.count()

    return render_template(
        'pages/admin/admin.html', 
        skill_count=skill_count,
        project_count=project_count,
        qualification_count=qualification_count,
        experience_count=experience_count,
        blog_posts_count=blog_posts_count
    )


@APP.route('/admin/skills')
@login_required
def manage_skills():
    """
    Retrieve all skills from the skills collection. Return a rendered 
    template of 'pages/admin/skills.html' and send retrieved skills to it 
    as well as a view parameter to set the top margin of the page heading.
    """
    skills = MONGO.db.skills.find()
    return render_template(
        'pages/admin/skills.html', 
        skills=skills, 
        view='admin'
    )


@APP.route('/admin/skills/add', methods=['POST'])
@login_required
def add_skill():
    """
    When receiving a POST request, try to construct a dictionary
    from the POST request and insert it into the skills collection.
    Try to verify that the skill has been inserted into the skills
    collection and flash a SUCCESS or FAILURE message as well as
    creating a reponse with a message and an appropriate HTTP status
    code. 

    If the above fails, flash a message informing the user that an error
    occured on the server side and create a response to send to the front
    end with the correct HTTPS status code.

    Return the created response.
    """
    if request.method == 'POST':
        try:
            skills = MONGO.db.skills
            skill_to_insert_dict = request.get_json()
            skills.insert_one(skill_to_insert_dict)
            find_inserted_skill = skills.find_one({'skill_name': skill_to_insert_dict['skill_name']})
            
            if find_inserted_skill:
                flash('Skill added successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to add skill.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    return response


@APP.route('/admin/skills/update/<skill_id>', methods=['GET', 'PUT'])
@login_required
def update_skill(skill_id):
    """
    When receiving a GET request, try to convert the skill ID to BSON format
    and find the skill in the skills collection. If the skill is found, create a
    response containing the skill as JSON (minus its ID), otherwise flash a FAILURE message
    and create a reponse with an HTTP status code of 503. Should this attempt fail,
    flash a FAILURE message and return a response with an HTTP status code of 500.

    When receiving a PUT request, try to construct a dictionary from the request body
    and update the skill in the skills collection based on its ID (converted to BSON).
    Flash a SUCCESS message and create a response with an HTTP status code of 200. Should
    the update fail, flash a FAILURE message and create a response with an HTTP status code
    of 500.

    Return the created response.
    """
    skills = MONGO.db.skills

    if request.method == 'GET':
        try:
            skill_to_return = skills.find_one({'_id': ObjectId(skill_id)})

            if skill_to_return:
                del skill_to_return['_id']
                response = make_response(jsonify(skill_to_return), 200)
            else:
                flash('Failed to get skill data.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    elif request.method == 'PUT':
        try:
            skill_to_update_dict = request.get_json()
            skills.update({'_id': ObjectId(skill_id)},
            {
                'skill_name': skill_to_update_dict['skill_name'],
                'skill_level': skill_to_update_dict['skill_level']
            })

            flash('Skill updated successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    return response


@APP.route('/admin/skills/delete/<skill_id>', methods=['DELETE'])
@login_required
def delete_skill(skill_id):
    """
    When the request method is DELETE, try to remove the particular skill
    from the skills collection using its ID (converted to BSON). Following the
    deletion attempt, attempt to locate the skill in the skills collection.
    If the skill cannot be found, flash a SUCCESS message and create a response
    with an HTTPS status code of 200, otherwise flash a FAILURE message and create
    a response with an HTTP status code of 503.

    Should the above attempt fail, flash a FAILURE message and create a response
    with a status code of 500.

    Return the response.
    """
    if request.method == 'DELETE':
        try:
            skills = MONGO.db.skills
            skills.remove({'_id': ObjectId(skill_id)})
            skill_to_confirm_deleted = skills.find_one({'_id': ObjectId(skill_id)})

            if not skill_to_confirm_deleted:
                flash('Skill deleted successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to delete skill.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    return response


@APP.route('/admin/projects')
@login_required
def manage_projects():
    """
    Retrieve all projects from the portfolio collection. Return a rendered 
    template of 'pages/admin/projects.html' and send retrieved skills to it 
    as well as a view parameter to set the top margin of the page heading.
    """
    projects = MONGO.db.portfolio.find()
    technologies = MONGO.db.technologies.find()
    technology_list = technologies[0]['technology_name']
    return render_template(
        'pages/admin/projects.html', 
        projects=projects, 
        technology_list=technology_list,
        view='admin'
    )


@APP.route('/admin/projects/add', methods=['POST'])
@login_required
def add_project():
    """
    When receiving a POST request, try to construct a dictionary
    from the POST request and insert it into the portfolio collection.
    Try to verify that the project has been inserted into the portfolio
    collection and flash a SUCCESS or FAILURE message as well as
    creating a reponse with a message and an appropriate HTTP status
    code. 

    If the above fails, flash a message informing the user that an error
    occured on the server side and create a response to send to the front
    end with the correct HTTPS status code.

    Return the created response.
    """
    if request.method == 'POST':
        try:
            projects = MONGO.db.portfolio
            project_to_insert_dict = request.get_json()
            projects.insert_one(project_to_insert_dict)
            find_inserted_project = projects.find_one({'project_name': project_to_insert_dict['project_name']})
            
            if find_inserted_project:
                flash('Project added successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to add project.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    return response


@APP.route('/admin/projects/update/<project_id>', methods=['GET', 'PUT'])
@login_required
def update_project(project_id):
    """
    When receiving a GET request, try to convert the project ID to BSON format
    and find the project in the portfolio collection. If the project is found, create a
    response containing the project as JSON (minus its ID), otherwise flash a FAILURE message
    and create a reponse with an HTTP status code of 503. Should this attempt fail,
    flash a FAILURE message and return a response with an HTTP status code of 500.

    When receiving a PUT request, try to construct a dictionary from the request body
    and update the project in the portfolio collection based on its ID (converted to BSON).
    Flash a SUCCESS message and create a response with an HTTP status code of 200. Should
    the update fail, flash a FAILURE message and create a response with an HTTP status code
    of 500.

    Return the created response.
    """
    portfolio = MONGO.db.portfolio

    if request.method == 'GET':
        try:
            project_to_return = portfolio.find_one({'_id': ObjectId(project_id)})
            
            if project_to_return:
                del project_to_return['_id']
                response = make_response(jsonify(project_to_return), 200)
            else:
                flash('Failed to get project data.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    elif request.method == 'PUT':
        try:
            project_to_update_dict = request.get_json()
            portfolio.update({'_id': ObjectId(project_id)}, project_to_update_dict)
            flash('Project updated successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)            
    return response


@APP.route('/admin/projects/delete/<project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id):
    """
    When the request method is DELETE, try to remove the particular project
    from the portfolio collection using its ID (converted to BSON). Following the
    deletion attempt, attempt to locate the project in the portfolio collection.
    If the project cannot be found, flash a SUCCESS message and create a response
    with an HTTPS status code of 200, otherwise flash a FAILURE message and create
    a response with an HTTP status code of 503.

    Should the above attempt fail, flash a FAILURE message and create a response
    with a status code of 500.

    Return the response.
    """
    if request.method == 'DELETE':
        try:
            projects = MONGO.db.portfolio
            projects.remove({'_id': ObjectId(project_id)})
            project_to_confirm_deleted = projects.find_one({'_id': ObjectId(project_id)})

            if not project_to_confirm_deleted:
                flash('Project deleted successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to delete project.', 'failure')
                response = make_response(jsonify({'message': 'failure'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)       
    return response


@APP.route('/admin/qualifications')
@login_required
def manage_qualifications():
    """
    Retrieve all qualifications from the qualifications collection. Return a rendered 
    template of 'pages/admin/qualifications.html' and send retrieved qualifications to it 
    as well as a view parameter to set the top margin of the page heading.
    """
    qualifications = MONGO.db.qualifications.find()
    return render_template(
        'pages/admin/qualifications.html', 
        qualifications=qualifications,
        view='admin'
    )


@APP.route('/admin/qualifications/add', methods=['POST'])
@login_required
def add_qualification():
    """
    When receiving a POST request, try to construct a dictionary
    from the POST request and insert it into the qualifications collection.
    Try to verify that the qualification has been inserted into the qualifications
    collection and flash a SUCCESS or FAILURE message as well as
    creating a reponse with a message and an appropriate HTTP status
    code. 

    If the above fails, flash a message informing the user that an error
    occured on the server side and create a response to send to the front
    end with the correct HTTPS status code.

    Return the created response.
    """
    if request.method == 'POST':
        try:
            qualifications = MONGO.db.qualifications
            qualification_to_insert = request.get_json()
            qualifications.insert_one(qualification_to_insert)
            find_inserted_qualification = qualifications.find_one({'qualification_name': qualification_to_insert['qualification_name']})
            
            if find_inserted_qualification:
                flash('Qualification added successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to delete qualification.', 'failure')
                response = make_response(jsonify({'message': 'failed'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    return response


@APP.route('/admin/qualifications/update/<qualification_id>', methods=['GET', 'PUT'])
@login_required
def update_qualification(qualification_id):
    """
    When receiving a GET request, try to convert the qualification ID to BSON format
    and find the qualification in the qualifications collection. If the qualification is found, create a
    response containing the skill as JSON (minus its ID), otherwise flash a FAILURE message
    and create a reponse with an HTTP status code of 503. Should this attempt fail,
    flash a FAILURE message and return a response with an HTTP status code of 500.

    When receiving a PUT request, try to construct a dictionary from the request body
    and update the qualification in the qualifications collection based on its ID (converted to BSON).
    Flash a SUCCESS message and create a response with an HTTP status code of 200. Should
    the update fail, flash a FAILURE message and create a response with an HTTP status code
    of 500.

    Return the created response.
    """
    qualifications = MONGO.db.qualifications

    if request.method == 'GET':
        try:
            qualification_to_return = qualifications.find_one({'_id': ObjectId(qualification_id)})
            
            if qualification_to_return:
                del qualification_to_return['_id']
                response = make_response(jsonify(qualification_to_return), 200)
            else:
                flash('Failed to get qualification data.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)            
    elif request.method == 'PUT':
        try:
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
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500) 
    return response


@APP.route('/admin/qualifications/delete/<qualification_id>', methods=['DELETE'])
@login_required
def delete_qualification(qualification_id):
    """
    When the request method is DELETE, try to remove the particular qualification
    from the qualifications collection using its ID (converted to BSON). Following the
    deletion attempt, attempt to locate the qualification in the qualifications collection.
    If the qualification cannot be found, flash a SUCCESS message and create a response
    with an HTTPS status code of 200, otherwise flash a FAILURE message and create
    a response with an HTTP status code of 503.

    Should the above attempt fail, flash a FAILURE message and create a response
    with a status code of 500.

    Return the response.
    """
    if request.method == 'DELETE':
        try:
            qualifications = MONGO.db.qualifications
            qualifications.remove({'_id': ObjectId(qualification_id)})
            qualification_to_confirm_deleted = qualifications.find_one({'_id': ObjectId(qualification_id)})

            if not qualification_to_confirm_deleted:
                flash('Qualification deleted successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to delete qualification.', 'failure')
                response = make_response(jsonify({'message': 'failure'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)     
    return response


@APP.route('/admin/blogs')
@login_required
def manage_blogs():
    """
    Retrieve all blog posts from the blog_posts collection. Return a rendered 
    template of 'pages/admin/blogs.html' and send retrieved blog posts to it 
    as well as a view parameter to set the top margin of the page heading.
    """
    blog_posts = MONGO.db.blog_posts.find()
    return render_template(
        'pages/admin/blogs.html', 
        blog_posts=blog_posts,
        view='admin'
    )


@APP.route('/admin/blogs/add', methods=['POST'])
@login_required
def add_blog_post():
    """
    When receiving a POST request, try to construct a dictionary
    from the POST request and insert it into the blog_posts collection.
    Try to verify that the blog post has been inserted into the blog_post
    collection and flash a SUCCESS or FAILURE message as well as
    creating a reponse with a message and an appropriate HTTP status
    code. 

    If the above fails, flash a message informing the user that an error
    occured on the server side and create a response to send to the front
    end with the correct HTTPS status code.

    Return the created response.
    """
    if request.method == 'POST':
        try:
            blog_posts = MONGO.db.blog_posts
            blog_post_to_insert_dict = request.get_json()
            blog_posts.insert_one(blog_post_to_insert_dict)
            find_inserted_blog_post = blog_posts.find_one({'blog_title': blog_post_to_insert_dict['blog_title']})
            
            if find_inserted_blog_post:
                flash('Blog post added successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to add blog post', 'failure')
                response = make_response(jsonify({'message': 'failed'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    return response


@APP.route('/admin/blogs/update/<blog_post_id>', methods=['GET','PUT'])
@login_required
def update_blog_post(blog_post_id):
    """
    When receiving a GET request, try to convert the blog post ID to BSON format
    and find the blog post in the blog_posts collection. If the blog post is found, create a
    response containing the blog post as JSON (minus its ID), otherwise flash a FAILURE message
    and create a reponse with an HTTP status code of 503. Should this attempt fail,
    flash a FAILURE message and return a response with an HTTP status code of 500.

    When receiving a PUT request, try to construct a dictionary from the request body
    and update the blog post in the blog_posts collection based on its ID (converted to BSON).
    Flash a SUCCESS message and create a response with an HTTP status code of 200. Should
    the update fail, flash a FAILURE message and create a response with an HTTP status code
    of 500.

    Return the created response.
    """
    blog_posts = MONGO.db.blog_posts

    if request.method == 'GET':
        try:
            blog_post_to_return = blog_posts.find_one({'_id': ObjectId(blog_post_id)})

            if blog_post_to_return:
                del blog_post_to_return['_id']
                response = make_response(jsonify(blog_post_to_return), 200)
            else:
                flash('Failed to get blog post data.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)   
    elif request.method == 'PUT':
        try:
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
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)              
    return response


@APP.route('/admin/blogs/delete/<blog_post_id>', methods=['DELETE'])
@login_required
def delete_blog_post(blog_post_id):
    """
    When the request method is DELETE, try to remove the particular blog post
    from the blog_posts collection using its ID (converted to BSON). Following the
    deletion attempt, attempt to locate the blog post in the blog_posts collection.
    If the blog post cannot be found, flash a SUCCESS message and create a response
    with an HTTPS status code of 200, otherwise flash a FAILURE message and create
    a response with an HTTP status code of 503.

    Should the above attempt fail, flash a FAILURE message and create a response
    with a status code of 500.

    Return the response.
    """
    if request.method == 'DELETE':
        try:
            blog_posts = MONGO.db.blog_posts
            blog_posts.remove({'_id': ObjectId(blog_post_id)})
            blog_post_to_confirm_deleted = blog_posts.find_one({'_id': ObjectId(blog_post_id)})

            if not blog_post_to_confirm_deleted:
                flash('Blog post deleted successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to delete blog post', 'failure')
                response = make_response(jsonify({'message': 'failure'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)     
    return response

@APP.route('/admin/experience')
@login_required
def manage_experience():
    """
    Retrieve all work experience from the work_experience collection. Return a rendered 
    template of 'pages/admin/experience.html' and send retrieved work experience to it 
    as well as a view parameter to set the top margin of the page heading.
    """
    experience = MONGO.db.work_experience.find()
    return render_template(
        'pages/admin/experience.html', 
        experience=experience,
        view='admin'
    )


@APP.route('/admin/experience/add', methods=['POST'])
@login_required
def add_experience():
    """
    When receiving a POST request, try to construct a dictionary
    from the POST request and insert it into the work_experience collection.
    Try to verify that the work experience has been inserted into the work_experience
    collection and flash a SUCCESS or FAILURE message as well as
    creating a reponse with a message and an appropriate HTTP status
    code.

    If the above fails, flash a message informing the user that an error
    occured on the server side and create a response to send to the front
    end with the correct HTTPS status code.

    Return the created response.
    """
    if request.method == 'POST':
        try:
            experience = MONGO.db.work_experience
            experience_to_insert_dict = request.get_json()
            experience.insert_one(experience_to_insert_dict)
            find_inserted_experience = experience.find_one({'job_title': experience_to_insert_dict['job_title']})
            
            if find_inserted_experience:
                flash('Experience added successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to add experience.', 'failure')
                response = make_response(jsonify({'message': 'failed'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)
    return response


@APP.route('/admin/experience/update/<experience_id>', methods=['GET','PUT'])
@login_required
def update_experience(experience_id):
    """
    When receiving a GET request, try to convert the experience ID to BSON format
    and find the experience in the work_experience collection. If the experience is found, create a
    response containing the experience as JSON (minus its ID), otherwise flash a FAILURE message
    and create a reponse with an HTTP status code of 503. Should this attempt fail,
    flash a FAILURE message and return a response with an HTTP status code of 500.

    When receiving a PUT request, try to construct a dictionary from the request body
    and update the experience in the work_experience collection based on its ID (converted to BSON).
    Flash a SUCCESS message and create a response with an HTTP status code of 200. Should
    the update fail, flash a FAILURE message and create a response with an HTTP status code
    of 500.

    Return the created response.
    """
    experience = MONGO.db.work_experience

    if request.method == 'GET':
        try:
            experience_to_return = experience.find_one({'_id': ObjectId(experience_id)})
            if experience_to_return:
                del experience_to_return['_id']
                response = make_response(jsonify(experience_to_return), 200)
            else:
                flash('Failed to get experience data.', 'failure')
                response = make_response(jsonify({'message': 'The requested service is not available at present. Please try again later.'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)           
    elif request.method == 'PUT':
        try:
            experience_to_update_dict = request.get_json()
            experience.update({'_id': ObjectId(experience_id)},
            {
                'job_title': experience_to_update_dict['job_title'],
                'job_dates': experience_to_update_dict['job_dates']
            })
            flash('Experience updated successfully!', 'success')
            response = make_response(jsonify({'message': 'success'}), 200)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)   
    return response


@APP.route('/admin/experience/delete/<experience_id>', methods=['DELETE'])
@login_required
def delete_experience(experience_id):
    """
    When the request method is DELETE, try to remove the particular experience
    from the work_experience collection using its ID (converted to BSON). Following the
    deletion attempt, attempt to locate the experience in the work_experience collection.
    If the experience cannot be found, flash a SUCCESS message and create a response
    with an HTTPS status code of 200, otherwise flash a FAILURE message and create
    a response with an HTTP status code of 503.

    Should the above attempt fail, flash a FAILURE message and create a response
    with a status code of 500.

    Return the response.
    """
    if request.method == 'DELETE':
        try:
            experience = MONGO.db.work_experience
            experience.remove({'_id': ObjectId(experience_id)})
            experience_to_confirm_deleted = experience.find_one({'_id': ObjectId(experience_id)})

            if not experience_to_confirm_deleted:
                flash('Experience deleted successfully!', 'success')
                response = make_response(jsonify({'message': 'success'}), 200)
            else:
                flash('Failed to delete experience', 'failure')
                response = make_response(jsonify({'message': 'failure'}), 503)
        except:
            flash('Oops, something seems to have gone wrong server side...', 'failure')
            response = make_response(jsonify({'message': 'Something seems to have gone wrong server side. Please try again later.'}), 500)     
    return response


@APP.errorhandler(404)
def page_not_found(e):
    """Returns a rendered template of the 404.html page"""
    return render_template(
        'pages/404.html', 
        image_height='full-screen',
        view='404'
    ), 404


if __name__ == '__main__':
    APP.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEBUG_VALUE'))