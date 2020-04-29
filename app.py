import os
if os.path.exists('env.py'):
    import env
from flask import Flask, render_template, url_for, redirect, request, session, flash, jsonify, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_mail import Mail, Message


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
    return render_template('pages/index.html', 
                            skills=skills, 
                            projects=projects,
                            qualifications=qualifications,
                            experience=experience)


@app.route('/about')
def about():
    """Return a rendered template of the ABOUT page"""
    return render_template('pages/about.html')


@app.route('/portfolio')
def portfolio():
    """Return a rendered template of the PROJECTS page with data passed to page
    
    Retrieve all projects from the PORTFOLIO collection from MongoDB Atlas.
    Return a rendered template of the PROJECTS page and pass data to it
    """
    projects = mongo.db.portfolio.find()
    return render_template('pages/portfolio.html', projects=projects)


@app.route('/project/<project_id>')
def project(project_id):
    """Return a rendered template of a specific PROJECT PAGE based on Id

    Convert the Id passed here from url_for in a PROJECT CARD into bson
    format.  Use the converted Id value to retrieve data for a specific 
    project from MongoDB Atlas.  Return a rendered remplate of a specific
    PROJECT PAGE and pass data to it 
    """
    project = mongo.db.portfolio.find_one({'_id': ObjectId(project_id)})
    return render_template('pages/project.html', project=project)


@app.route('/contact')
def contact():
    """Return a rendered template of the CONTACT page"""
    return render_template('pages/contact.html')


@app.route('/send_mail', methods=['POST'])
def send_mail():
    """Send an email to site owner using data from CONTACT page form
    
    Using data from CONTACT page, set recipient email address, 
    build email header and body and send email to site owner.
    Once completed, redirect back to the CONTACT page
    """
    if request.method == 'POST':
        recipient = os.environ.get('RECIPIENT_ADDRESS')
        msg = Message(request.form['subject'], sender = request.form['email'], recipients = [recipient])
        msg.body = request.form['query']
        mail.send(msg)
    return redirect('contact')


@app.route('/blogs')
def blogs():
    """Return a rendered template with all blog data of the BLOGS page
    
    Retrieve all blog posts from MongoDB altas blog_posts collection.
    Return a rendered template of the BLOGS page and send data to it
    """
    blog_posts = mongo.db.blog_posts.find()
    return render_template('pages/blogs.html', blog_posts=blog_posts)


@app.route('/blogs/<blog_id>')
def blog_entry(blog_id):
    """Return a rendered template of a spefic BLOG POST based on Id
    
    Convert the Id passed here from url_for in a BLOG POST CARD into bson
    format.  Use the converted Id value to retrieve data for a specific 
    blog entry from the blog_posts collection in MongoDB Atlas.  Return a 
    rendered remplate of a specific BLOG POST PAGE and pass data to it 
    """
    blog_entry = mongo.db.blog_posts.find_one({'_id': ObjectId(blog_id)})
    return render_template('pages/blog_entry.html', blog_entry=blog_entry)


@app.route('/admin')
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

    return render_template('pages/admin/admin.html', skill_count=skill_count,
                                                project_count=project_count,
                                                qualification_count=qualification_count,
                                                experience_count=experience_count,
                                                blog_posts_count=blog_posts_count)


@app.route('/admin/skills')
def manage_skills():
    """Return a rendered template of SKILLS page with all skills sent to it"""
    skills = mongo.db.skills.find()
    return render_template('pages/admin/skills.html', skills=skills)


@app.route('/admin/skills/add', methods=['POST'])
def add_skill():
    """Insert a new document into skills collection"""
    if request.method == 'POST':
        skills = mongo.db.skills
        skill_to_insert_dict = request.get_json()
        skills.insert_one(skill_to_insert_dict)
        find_inserted_skill = skills.find_one({'skill_name': skill_to_insert_dict['skill_name']})
        
        if find_inserted_skill:
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            response = make_response(jsonify({'message': 'failed'}), 500)
    return response


@app.route('/admin/skills/update/<skill_id>', methods=['GET', 'PUT'])
def update_skill(skill_id):
    """Update a skill based on its Id"""
    skills = mongo.db.skills
    if request.method == 'GET':
        skill_to_return = skills.find_one({'_id': ObjectId(skill_id)})
        del skill_to_return['_id']
        response = make_response(jsonify(skill_to_return), 200)
    elif request.method == 'PUT':
        skill_to_update_dict = request.get_json()
        skills.update({'_id': ObjectId(skill_to_update_dict['skill_id'])},
        {
            'skill_name': skill_to_update_dict['skill_name'],
            'skill_level': skill_to_update_dict['skill_level']
        })

        response = make_response(jsonify({'message': 'success'}), 200)
    return response


@app.route('/admin/skills/delete/<skill_id>', methods=['DELETE'])
def delete_skill(skill_id):
    """Remove a skill from skills collection based on Id"""
    if request.method == 'DELETE':
        skills = mongo.db.skills
        skills.remove({'_id': ObjectId(skill_id)})
        skill_to_confirm_deleted = skills.find_one({'_id': ObjectId(skill_id)})

        if not skill_to_confirm_deleted:
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            response = make_response(jsonify({'message': 'failure'}), 500)
    return response


@app.route('/admin/projects')
def manage_projects():
    """Return a rendered template of PROJECTS page with all projects sent to it"""
    projects = mongo.db.portfolio.find()
    technologies = mongo.db.technologies.find()
    technology_list = technologies[0]['technology_name']
    return render_template('pages/admin/projects.html', projects=projects, technology_list=technology_list)


@app.route('/admin/projects/add', methods=['POST'])
def add_project():
    """Insert a new document into portfolio collection"""
    if request.method == 'POST':
        projects = mongo.db.portfolio
        project_to_insert_dict = request.get_json()
        projects.insert_one(project_to_insert_dict)
        find_inserted_project = projects.find_one({'project_name': project_to_insert_dict['project_name']})
        
        if find_inserted_project:
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            response = make_response(jsonify({'message': 'failed'}), 500)
    return response 


@app.route('/admin/edit_project/<project_id>')
def edit_project(project_id):
    """Return a rendered template of EDIT PROJECT page populated with data of a specific project
    
    Using the PROJECT ID sent from MANAGE PROJECTS, retrieve the document for a specific project.
    Retrieve a list of all technologies from the technologies collection. Pass project 
    and technologies data to a rendered template of the EDIT PROJECT page.
    """
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


@app.route('/admin/projects/delete/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Remove a project from portfolio collection based on Id"""
    if request.method == 'DELETE':
        projects = mongo.db.portfolio
        projects.remove({'_id': ObjectId(project_id)})
        project_to_confirm_deleted = projects.find_one({'_id': ObjectId(project_id)})

        if not project_to_confirm_deleted:
            response = make_response(jsonify({'message': 'success'}), 200)
        else:
            response = make_response(jsonify({'message': 'failure'}), 500)
    return response


@app.route('/admin/add_qualification')
def add_qualification():
    """Return a rendered template of the ADD QUALIFICATION page"""
    return render_template('pages/add_qualification.html')


@app.route('/admin/insert_qualification', methods=['POST'])
def insert_qualification():
    """Using data from form on ADD QUALIFICATION page, insert document into qualifications collection
    
    Retrieve documents from qualifications collection. Convert form data from add_qualification
    page's form to dictionary. Insert it into qualifications collection. Try to find 
    newly inserted document in qualifications collection and flash either a success or
    failure message on screen. Finally, redirect to MANAGE QUALIFICATIONS page
    """
    if request.method == 'POST':
        qualifications = mongo.db.qualifications
        qualification_to_insert = request.form.to_dict()
        qualifications.insert_one(qualification_to_insert)
        find_inserted_qualification = qualifications.find_one({'qualification_name': qualification_to_insert['qualification_name']})
    
        if find_inserted_qualification:
            flash(f'Successfully inserted \"{qualification_to_insert["qualification_name"]}\" into \"qualifications\" collection', 'success')
        else:
            flash('Failed to insert project into portfolio collection', 'failed')
        return redirect(url_for('manage_qualifications'))


@app.route('/admin/qualifications')
def manage_qualifications():
    """Return a rendered template of MANAGE QUALIFICATIONS page
    
    Retrieve all qualification documents from the qualifications collection.  
    Pass retrieved data to a rendered template of the MANMAGE QUALIFICATIONS page.
    """
    qualifications = mongo.db.qualifications.find()
    return render_template('pages/admin/qualifications.html', qualifications=qualifications)


@app.route('/admin/edit_qualification/<qualification_id>')
def edit_qualification(qualification_id):
    """Return a rendered template of EDIT QUALIFICATION page populated with data of a specific qualification
    
    Using the QUALIFICATION ID sent from MANAGE QUALIFICATIONS, retrieve the document for a specific qualification.
    Pass project data to a rendered template of the EDIT QUALIFICATION page.
    """
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
    """Remove a qualification from qualifications collection based on Id
    
    Retrieve qualifications collection from DB, then retrieve and store entry to be deleted using its 
    Id from MANAGE QUALIFICATIONS page. Remove qualification from qualifications collection using Id. Try to find
    qualification in qualifications collection to confirm removal and flash success or failure message based on 
    result. Finally, redirect to MANAGE QUALIFICATIONS page
    """
    qualifications = mongo.db.qualifications
    qualification_to_delete = qualifications.find_one({'_id': ObjectId(qualification_id)})
    qualifications.remove({'_id': ObjectId(qualification_id)})
    qualification_to_confirm_deleted = qualifications.find_one({'_id': ObjectId(qualification_id)})

    if not qualification_to_confirm_deleted:
        flash(f'Successfully deleted \"{qualification_to_delete["qualification_name"]}\" from \"qualifications\" collection', 'success')
    else:
        flash('Failed to delete qualification from qualifications collection', 'failed')
    return redirect(url_for('manage_qualifications'))


@app.route('/admin/add_blog_post')
def add_blog_post():
    """Return rendered template of ADD BLOG POST page"""
    return render_template('pages/add_blog_post.html')


@app.route('/admin/insert_blog_post', methods=['POST'])
def insert_blog_post():
    """Using data from form on ADD BLOG POST page, insert document into blog_posts collection
    
    Retrieve documents from blog_posts collection. Convert form data from add_blog_post
    page's form to dictionary. Set blog_body field as list instead of single value. Insert dictionary 
    into blog_posts collection. Try to find newly inserted document in blog_posts collection and flash 
    either a success or failure message on screen. Finally, redirect to MANAGE BLOGS page
    """
    if request.method == 'POST':
        blog_posts = mongo.db.blog_posts
        form_body = request.form.to_dict()
        form_body['blog_body'] = request.form.getlist('blog_body')
        blog_posts.insert_one(form_body)
        find_inserted_blog_post = blog_posts.find_one({'blog_title': form_body['blog_title']})

        if find_inserted_blog_post:
            flash(f'Successfully inserted \"{form_body["blog_title"]}\" into \"blog_posts\" collection', 'success')
        else:
            flash('Failed to insert blog post into blog_posts collection', 'failed')
        return redirect(url_for('manage_blogs'))


@app.route('/admin/blogs')
def manage_blogs():
    """Return a rendered template of MANAGE BLOGS page
    
    Retrieve all BLOG POST documents from the blog_posts collection.  Pass retrieved data 
    to a rendered template of the MANAGE BLOGS page.
    """
    blog_posts = mongo.db.blog_posts.find()
    return render_template('pages/admin/blogs.html', blog_posts=blog_posts)


@app.route('/admin/edit_blog_post/<blog_post_id>')
def edit_blog_post(blog_post_id):
    """Return a rendered template of EDIT BLOG POST page populated with data of a specific blog post
    
    Using the BLOG POST ID sent from MANAGE BLOGS, retrieve the document for a specific blog post.
    Pass blog post data to a rendered template of the EDIT BLOG POST page.
    """
    blog_post = mongo.db.blog_posts.find_one({'_id': ObjectId(blog_post_id)})
    return render_template('pages/edit_blog_post.html', blog_post=blog_post)


@app.route('/admin/update_blog_post/<blog_post_id>', methods=['POST'])
def update_blog_post(blog_post_id):
    if request.method == 'POST':
        blog_posts = mongo.db.blog_posts
        blog_posts.update({'_id': ObjectId(blog_post_id)},
        {
            'blog_title': request.form.get('blog_title'),
            'blog_img_url': request.form.get('blog_img_url'),
            'blog_summary': request.form.get('blog_summary'),
            'blog_date': request.form.get('blog_date'),
            'blog_body': request.form.getlist('blog_body')
        })

        return redirect(url_for('admin'))
    else:
        return redirect(url_for('edit_blog_post'))


@app.route('/admin/delete_blog_post/<blog_post_id>')
def delete_blog_post(blog_post_id):
    """Remove a blog post from blog_posts collection based on Id
    
    Retrieve blog_posts collection from DB, then retrieve and store entry to be deleted using its 
    Id from MANAGE BLOGS page. Remove blog post from blog_posts collection using Id. Try to find
    blog_posts in blog_posts collection to confirm removal and flash success or failure message based on 
    result. Finally, redirect to MANAGE BLOGS page
    """
    blog_posts = mongo.db.blog_posts
    blog_post_to_delete = blog_posts.find_one({'_id': ObjectId(blog_post_id)})
    blog_posts.remove({'_id': ObjectId(blog_post_id)})
    blog_post_to_confirm_deleted = blog_posts.find_one({'_id': ObjectId(blog_post_id)})

    if not blog_post_to_confirm_deleted:
        flash(f'Successfully deleted \"{blog_post_to_delete["blog_title"]}\" from \"blog_posts\" collection', 'success')
    else:
        flash('Failed to delete blog post from blog_posts collection', 'failed')
    return redirect(url_for('manage_blogs'))


@app.route('/admin/add_experience')
def add_experience():
    """Return a rendered template of the ADD EXPERIENCE page"""
    return render_template('pages/add_experience.html')


@app.route('/admin/insert_experience', methods=['POST'])
def insert_experience():
    """Using data from form on ADD EXPERIENCE page, insert document into work_experience collection
    
    Retrieve documents from work_experience collection. Convert form data from add_experience
    page's form to dictionary. Insert dictionary into work_experience collection. Try to find 
    newly inserted document in work_experience collection and flash either a success or 
    failure message on screen. Finally, redirect to MANAGE EXPERIENCE page
    """
    if request.method == 'POST':
        experience = mongo.db.work_experience
        form_body = request.form.to_dict()
        experience.insert_one(form_body)
        find_inserted_experience = experience.find_one({'job_title': form_body['job_title']})

        if find_inserted_experience:
            flash(f'Successfully inserted \"{form_body["job_title"]}\" into \"work_experience\" collection', 'success')
        else:
            flash('Failed to insert experience into work_experience collection', 'failed')
        return redirect(url_for('manage_experience'))


@app.route('/admin/experience')
def manage_experience():
    """Return a rendered template of MANAGE EXPERIENCE page
    
    Retrieve all WORK EXPERIENCE documents from the work_experience collection.  Pass retrieved data 
    to a rendered template of the MANAGE WORK EXPERIENCE page.
    """
    experience = mongo.db.work_experience.find()
    return render_template('pages/admin/experience.html', experience=experience)


@app.route('/admin/edit_experience/<experience_id>')
def edit_experience(experience_id):
    """Return a rendered template of EDIT EXPERIENCE page populated with data of specific work experience
    
    Using the WORK EXPERIENCE ID sent from MANAGE WORK EXPERIENCE, retrieve the document for a specific work experience.
    Pass work experience data to a rendered template of the EDIT EXPERIENCE page.
    """
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
    """Remove a work experience from work_experience collection based on Id
    
    Retrieve work_experience collection from DB, then retrieve and store entry to be deleted using its 
    Id from MANAGE EXPERIENCE page. Remove work experience from work_experience collection using Id. Try to find
    work_experience in work_experience collection to confirm removal and flash success or failure message based on 
    result. Finally, redirect to MANAGE EXPERIENCE page
    """
    experience = mongo.db.work_experience
    experience_to_delete = experience.find_one({'_id': ObjectId(experience_id)})
    experience.remove({'_id': ObjectId(experience_id)})
    experience_to_confirm_deleted = experience.find_one({'_id': ObjectId(experience_id)})

    if not experience_to_confirm_deleted:
        flash(f'Successfully deleted \"{experience_to_delete["job_title"]}\" from \"work_experience\" collection', 'success')
    else:
        flash('Failed to delete experience from work_experience collection', 'failed')
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