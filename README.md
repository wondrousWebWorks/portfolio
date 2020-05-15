# wondrousWebWorks()

Thank you for viewing my project. wondrousWebWorks() is a portfolio for me as a full stack developer, including some information about me, my skills, experience, a contact section, a blog and project information. It also includes an admin page, where the site owner can manage the site and perform CRUD (Create, Read, Update and Delete) operations.

## Content

- [wondrousWebWorks()](#wondrouswebworks)
  - [Content](#content)
  - [User Experience](#user-experience)
    - [Project Goals](#project-goals)
      - [User Goals](#user-goals)
      - [User Stories](#user-stories)
        - [User Story A](#user-story-a)
        - [User Story B](#user-story-b)
        - [User Story C](#user-story-c)
        - [User Story D](#user-story-d)
        - [User Story E](#user-story-e)
      - [Site Owner Goals](#site-owner-goals)
    - [Design Choices](#design-choices)
      - [Fonts](#fonts)
      - [Icons](#icons)
      - [Images](#images)
      - [Colours](#colours)
        - [#1C1C1C (Eerie Black)](#1c1c1c-eerie-black)
        - [#F7F7F7 (off-white)](#f7f7f7-off-white)
        - [#007749 (sa-flag-green)](#007749-sa-flag-green)
        - [#E03C31 (sa-flag-red)](#e03c31-sa-flag-red)
        - [#FFB81C (sa-flag-gold)](#ffb81c-sa-flag-gold)
        - [#0080ff (sa-flag-blue)](#0080ff-sa-flag-blue)
  - [Information Architecture](#information-architecture)
    - [Collection name:  blog_posts](#collection-name-blogposts)
    - [Collection name:  portfolio](#collection-name-portfolio)
    - [Collection name: qualifications](#collection-name-qualifications)
    - [Collection name: skills](#collection-name-skills)
    - [Collection name: technologies](#collection-name-technologies)
    - [Collection name: users](#collection-name-users)
    - [Collection name:  work_experience](#collection-name-workexperience)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries, Frameworks & Tools](#libraries-frameworks--tools)
  - [Wireframes](#wireframes)
    - [Differences Between Wireframes and Final Product](#differences-between-wireframes-and-final-product)
      - [Landing Page (Skills section)](#landing-page-skills-section)
  - [Bugs](#bugs)
    - [Development Bugs](#development-bugs)
    - [Deployment Bugs](#deployment-bugs)
  - [Deployment](#deployment)
    - [Local Installation](#local-installation)
      - [Requirements](#requirements)
      - [Installation Instructions](#installation-instructions)
    - [Deploy to Heroku](#deploy-to-heroku)
      - [Requirements](#requirements-1)
      - [Deployment Instructions](#deployment-instructions)
  - [Credits](#credits)
  - [Disclaimer](#disclaimer)

## User Experience

### Project Goals

wondrousWebWorks() is created to be a profile for me as a developer.  It serves to showcase my skills as a developer while allowing visitors to view my ever-expanding portfolio. The site provides some information about me and allows visitors to contact me for any queries or to request work should they so desire. wondrousWebworks() is created to be future proof, and as such featues an admin panel which allows the site admin to manipulate the site by performing CRUD (Create, Read, Update and Delete) operations to change the MongoDB collection and subsequebtly the site as desired. The site showcases current design trends in 2020, and is designed to be visually appealing and intuitive to use.

#### User Goals

- A multi-page site which allows the user view information about the developer with ease
- Information about the developer
- An indication of the developer's skill set and estimated proficiency at each skill
- A portfolio showcasing the developer's projects with project information and links to repositories and live sites
- The ability to contact the developer for queries or for work
- Easy navigation between all pages of the site

#### User Stories

##### User Story A

*"As a first-time user of the site, I want the UX to be well designed so that I can navigate the site with ease."*

##### User Story B

*"As someone wishing to see the developer's ability, I want to see good design practices so that I can assess their skill level."*

##### User Story C

*"As an interest party, I want to be able to naviagte to the developer's GitHub repositories and LinkedIn profile so I can get more detailed information about them."*

##### User Story D

*"As a prospective employer, I want to be able to see a portfolio of projects so that I can assess the developer's experience and ability."*

##### User Story E

*"As a prospective customer, I want to be able to contact the developer so that I can discuss them working on a project for me."*

#### Site Owner Goals

- Deliver on User Stories as far as possible
- Gain the interest of prospective employers or customers
- Create an ADMIN page which allows carrying out CRUD (Create, Read, Update, Delete) operations)
- Create a site that is future proof and allows for the addition of additional skills, projects, blog posts and education

### Design Choices

I decided on using a dark theme with a selection of bright colours to provide good contrast and reduce eye strain for users and the site admin. The design is simple with good spacing so that the various sections of the portfolio would stand out and be visualy striking in itself where required.

#### Fonts

In order to fit the fantasy nature of the game, unconventional fonts were selected from **Google Fonts**.  The selected fonts have to be slighty quirky and more cartoony in design, while still being legible. Sample phrases featured in the game were entered in **Google Fonts** to see how they were displayed. Ultimately, the fonts below were selected to be used in clearly defined areas in the game.

- [Baloo 2](https://fonts.google.com/specimen/Baloo+2?query=Baloo+2) - used for all headings as well as links in the navbar
- [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab?query=roboto+slab) - used for all text which is not a heading or a link in the navbar

#### Icons

At first an effort was made to use Materialize icons only, but it soon became apparent that they were too limited to meet design expectations. As such, all icons were taken from either [Materialize](https://materializecss.com/) or [Font Awesome](https://fontawesome.com/).

#### Images

The image for the **Hero** shot in the site header was taken from [PNGTREE](https://pngtree.com/) and chosen because it complements the site's chosen colour scheme.  Images for **Blog** entries were taken from [Pexels](https://www.pexels.com/) and selected to portray the general topic of each blog. Project images were taken from [Am I Responsive?](http://ami.responsivedesign.is/) to show a responsive layout for each project. The **wondrousWebWorks()** logo was created by me.

#### Colours

 **Eerie black** (*#1c1c1c* in hex) was chosen as background colour for the site body as the site was designed to be displayed in "dark mode". In order to make text legible, **#f7f7f7** was chosen as text colour. All other colours were taken from the South African flag and named by me; a subtle homage to my origin. See below for more details.  All colours complement each other very well, and provide a good level of contrast to increase legibility and highlight various areas of the page.

##### #1C1C1C (Eerie Black)

- Background colour for main site body and admin body

##### #F7F7F7 (off-white)

- Used for all text

##### #007749 (sa-flag-green)

- Background colour of **navbar**
- Colour of the *LinkedIn* icon in the fixed navigation shortcuts on the left of the screen
- Background colour of the 'user and host' name in the **About** and **About Summary** sections
- Colour of the bottom border below section headings
- One of three background colours of bars in **Skills** displays
- Colour of the *deployed site* icon in **Project cards**
- Background colour of the *view* buttons in the **Education** section
- Colour of the *calendar* icons in **Experience cards**
- Colour of even-numbered *technologies* of the **Project** page
- Background colour of the *blog summary* on **Blog cards**
- Background colour of the **Add** buttons on Admin management pages
- Background colour of the form *submit* buttons in form modals

##### #E03C31 (sa-flag-red)

- Background colour of the *call-to-action* button in the page header
- Colour of the *Contact* icon in the fixed navigation shortcuts on the left of the screen
- Colour of the $ symbol in the **About** and **About Summary** sections
- One of three background colours of bars in **Skills** displays
- Background colour of the **All Projects** button on the home page
- Colour of the *university* and *calendar* icons in the **Education** section
- Colour of the left text border on the **Project** page
- Colour of the left text border on the **Blog Post** page
- Background colour of the *Delete* buttons on Admin management pages

##### #FFB81C (sa-flag-gold)

- Colour of the *GitHub* icon in the fixed navigation shortcuts on the left of the screen
- Colour of the ;present working directory' in the **About** and **About Summary** sections
- Colour of the flashing rectangular icon in the **About** and **About Summary** sections
- One of three background colours of bars in **Skills** displays
- Colour of the *GitHub* icon in **Project cards**
- Colour of *down* caret icons in collapsible items
- Colour of the *tag* icons in **Experience cards**
- Colour of odd-numbered *technologies* of the **Project** page
- Colour of the *blog date* on the **Blog Post** page

##### #0080ff (sa-flag-blue)

- Background colour of the *more info* buttons in the **Education** section
- Background-colour of all modal *close* buttons
- Background colour of all **Manage** buttons on the Admin dashboard

## Information Architecture

For this project, it was required to use a NoSQL database. MongoDB Atlas was chosen as it provides free datbase hosting in the cloud for minimal traffic and has hardly any downtime at all.

The **collections** required with information on each key:value pair's **title**, **key** and value **data type** is listed below. Please ensure that you use the **collection** and **key** names *exactly* as outlined.

NOTE: MongoDB automatically generates a unique ID for each document.  It is part of every document and **not** something you have to create yourself.

### Collection name:  blog_posts

A JSON representation of the **blog_posts** collection can be found [here](https://github.com/wondrousWebWorks/wondrousWebWorks/blob/master/schemas/blog_posts.json)

<table>
<thead>
  <tr>
    <th>Description</th>
    <th>Key</th>
    <th>Data Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>The unique document ID generated by MongoDB</td>
    <td>_id</td>
    <td>ObjectId</td>
  </tr>
  <tr>
    <td>The title for the blog post</td>
    <td>blog_title</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The URL for the image used in the blog</td>
    <td>blog_img_url</td>
    <td>string</td>
  </tr>
  <tr>
    <td>A short summary of the blog post (one sentence)</td>
    <td>blog_summary</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The date the blog is/was published e.g. 23 Jun 2020</td>
    <td>blog_date</td>
    <td>string</td>
  </tr>
  <tr>
    <td>A collection of all the paragraphs in the blog post (maximum 10)</td>
    <td>blog_body</td>
    <td>Array</td>
  </tr>
</tbody>
</table>

### Collection name:  portfolio

A JSON representation of the **portfolio** collection can be found [here](https://github.com/wondrousWebWorks/wondrousWebWorks/blob/master/schemas/portfolio.json)

<table>
<thead>
  <tr>
    <th>Description</th>
    <th>Key</th>
    <th>Data Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>The unique document ID as generated by MongoDB</td>
    <td>_id</td>
    <td>ObjectId</td>
  </tr>
  <tr>
    <td>The name of the project</td>
    <td>project_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The URL of where the project is hosted or located</td>
    <td>project_img_url</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The GitHub URL of the project's repository</td>
    <td>project_github_url</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The URL of where the project is deployed</td>
    <td>project_deployed_url</td>
    <td>string</td>
  </tr>
  <tr>
    <td>A list of all the technologies used in the project</td>
    <td>project_technologies</td>
    <td>Array</td>
  </tr>
  <tr>
    <td>A list of all the paragraphs describing the project</td>
    <td>project_description</td>
    <td>Array</td>
  </tr>
</tbody>
</table>

### Collection name: qualifications

A JSON representation of the **qualifications** collection can be found [here](https://github.com/wondrousWebWorks/wondrousWebWorks/blob/master/schemas/qualifications.json)

<table>
<thead>
  <tr>
    <th>Description</th>
    <th>Key</th>
    <th>Data Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>The unique document ID as generated by MongoDB</td>
    <td>_id</td>
    <td>ObjectId</td>
  </tr>
  <tr>
    <td>The name of the qualification</td>
    <td>qualification_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The name of the institute which issued the qualification</td>
    <td>qualification_from</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The date the qualification was obtained / issued e.g 2017 or Feb 2017</td>
    <td>qualification_issue_date</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The URL where the qualification can be viewed</td>
    <td>qualification_view_url</td>
    <td>string</td>
  </tr>
  <tr>
    <td>A URL where more information about the qualification can be found </td>
    <td>qualification_info_url</td>
    <td>string</td>
  </tr>
</tbody>
</table>

### Collection name: skills

A JSON representation of the **skills** collection can be found [here](https://github.com/wondrousWebWorks/wondrousWebWorks/blob/master/schemas/skills.json)

<table>
<thead>
  <tr>
    <th>Description</th>
    <th>Key</th>
    <th>Data Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>The unique document ID as generated by MongoDB</td>
    <td>_id</td>
    <td>ObjectId</td>
  </tr>
  <tr>
    <td>The name of the skill</td>
    <td>skill_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The developer's skill level expressed as a percentage (maximum 100)</td>
    <td>skill_level</td>
    <td>string</td>
  </tr>
</tbody>
</table>

### Collection name: technologies

A JSON representation of the **technologies** collection can be found [here](https://github.com/wondrousWebWorks/wondrousWebWorks/blob/master/schemas/technologies.json)

<table>
<thead>
  <tr>
    <th>Description</th>
    <th>Key</th>
    <th>Data Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>The unique document ID as generated by MongoDB</td>
    <td>_id</td>
    <td>ObjectId</td>
  </tr>
  <tr>
    <td>A list of technologies in the developer's arsenal. As more are mastered, the can be added to this list</td>
    <td>technology_name</td>
    <td>Array</td>
  </tr>
</tbody>
</table>

### Collection name: users

A JSON representation of the **users** collection can be found [here](https://github.com/wondrousWebWorks/wondrousWebWorks/blob/master/schemas/users.json)

<table>
<thead>
  <tr>
    <th>Description</th>
    <th>Key</th>
    <th>Data Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>The unique document ID as generated by MongoDB</td>
    <td>_id</td>
    <td>ObjectId</td>
  </tr>
  <tr>
    <td>The email address for a particular user</td>
    <td>email</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The hashed password for a particular user</td>
    <td>password</td>
    <td>string</td>
  </tr>
</tbody>
</table>

### Collection name:  work_experience

A JSON representation of the **work_experience** collection can be found [here](https://github.com/wondrousWebWorks/wondrousWebWorks/blob/master/schemas/work_experience.json)

<table>
<thead>
  <tr>
    <th>Description</th>
    <th>Key</th>
    <th>Data Type</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>The unique document ID as generated by MongoDB</td>
    <td>_id</td>
    <td>ObjectId</td>
  </tr>
  <tr>
    <td>The job title e.g. Frontend Developer</td>
    <td>job_title</td>
    <td>string</td>
  </tr>
  <tr>
    <td>The dates worked in particular job e.g. 25 Oct 2018 - 27 Sep 2019</td>
    <td>job_dates</td>
    <td>string</td>
  </tr>
</tbody>
</table>

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Libraries, Frameworks & Tools

- Flask
- MongoDB (Atlas Cloud)
- Git
- Materializecss
- Font Awesome
- Google Fonts
- Cloudinary

## Wireframes

[Balsamiq Mockups 3](https://balsamiq.com/) was used to design all mockups. Wireframes for desktop, mobile and tablet can be viewed [here](https://github.com/wondrousWebWorks/wondrousWebWorks/tree/master/wireframes). There were some minor differences between the wireframes and the end product due to user feedback following testing.  These changes are highlighted below.

### Differences Between Wireframes and Final Product

Some changes had to be made based on tester feedback to improve User Experience (UX).  These changes are listed below.

#### Landing Page (Skills section)

- On mobile devices in portrait orientation, two skills are displayed per row as opposed to a single skill as illustrated in the wireframe

## Bugs

### Development Bugs

At one stage, I couldn't get flashed messages to display on my Admin page, and decided to replicate the same functionality in Javascript as best I could only to realise that I'd forgotten to add the flash messages functionality to both the base.html **and** admin-base.html files.  Upon discovery of this oversight, I implemented Flask's messaging system and removed the unnecessary JavaScript function which mimicked the same functionality.

Another niggle was when I prevented the default behaviour of all buttons, only to realise that it affected my contact and login forms where the default behaviour was required.  Unfortunately, it took quite a bit of time to discover the issue.

### Deployment Bugs

Initially, there was great difficulty deploying the project to Heroku.  After viewing the project's Heroku log files, it was discovered that the **pkg-resources** package could not be located by Heroku for installation. Modifying the **requirements.txt** file by removing the **pkg-resources** dependancy before pushing to GitHub and subsequently Heroku fixed the bug and allowed succesfull installion of all dependancies.

## Deployment

The project can be run either locally or deployed on Heroku.  Instructions for either option can be viewed below. The instructions provided are for installing on a Linux-based machine. Should your operating system be different, please note that some of the commands might be different.

### Local Installation

#### Requirements

- An integrated development environment (IDE) - [VSCode](https://code.visualstudio.com/Download) is free and was used to create this site
- An account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - follow the instructions to create an account
- [Git](https://git-scm.com/downloads) - includes installation instructions
- [Python 3](https://www.python.org/downloads/) - installation instructions can be found [here](https://docs.python-guide.org/starting/install3/linux/)
- [pip](https://pypi.org/project/pip/) - includes installation instructions
- An email acount for which you can find server details - [Gmail](https://www.google.com/gmail/about/#) works very well for this

#### Installation Instructions

It is assumed that the required database and collections have been created in your MongoDB Atlas account. If not, please refer to the [Information Architecture](#information-architecture) section and set up your database and collections as stipulated there.

1. Using your browser of choice, navigate to the [wondrousWebWorks repository](https://github.com/wondrousWebWorks/wondrousWebWorks) in GitHub
2. Click on the green **Clone or download** button on the right of the screen (on personal computers) which will trigger a dropdown menu
3. Copy the URL provided
4. Using your terminal of choice, create or navigate to the directory or folder where you'd like to install the wondrousWebWorks project directory
5. Enter the command `git clone` followed by the URL copied in step 3, or just copy the command from here, paste it in the terminal enter press Enter

        git clone https://github.com/wondrousWebWorks/wondrousWebWorks.git

6. Wait for the the repository to be cloned

   It considered good practice to contain each product in each own virtual environment as any dependancies for each project can be installed locally in each project's virtual environment. Several virtual environments exist and since Python 3.3, a subset of the popular [virtualenv](https://virtualenv.pypa.io/en/latest/) comes as standard with all Python 3 installations. This subset does not offer the full fetaure set of the full **virtualenv** package, and as such is recommended to install it using **pip**.

7. Install the virtualenv package using pip by using the following command

        pip3 install virtualenv

8. Once **virtualenv** is successfully installed, ensure that you are in the project's root directory and create a virtual environment named *venv* using the following command

        virtualenv venv

9. Ensure you are in the project directory and activate the *venv* environment with the folowing command. This will allow you to install project-dependant requirements in the next step

        source venv/bin/activate

10. Install the necessary requirements in your virtual environment with *pip* using the following command

        pip3 install -r requirements.txt

11. Open your IDE and open the project folder in it
12. Create a file called *env.py* in the project's root directory
13. In your *env.py* file, import the *os* module and set the following environment variables as follows.

        import os
        os.environ["IP"] = "0.0.0.0"
        os.environ["PORT"] = "5000"
        os.environ["DEBUG_VALUE"] = "True"
        os.environ["MONGO_URI"] = "<your MongoDB Atlas connection string>"
        os.environ["MONGO_DBNAME"] = "<your db name>"
        os.environ["SECRET_KEY"] = "<your secret key>"
        os.environ["MAIL_SERVER"] = "smtp.gmail.com"
        os.environ["MAIL_PORT"] = "465"
        os.environ["MAIL_USERNAME"] = "<your gmail address>"
        os.environ["MAIL_PASSWORD"] = "<your gmail password>"
        os.environ["RECIPIENT_ADDRESS"] = "<the email address where you would like the contact mail to be sent - it can be the same as your MAIL_USERNAME>"
        os.environ["SECRET_KEY"] = "<your secret key>"

    NOTE: Wherever text is surrounded by <> (angle brackets), you will need to provide your own values without the angle brackets as determined by your MonogoDB account, mail server and secret key. Remember to change the *username*, *password* and *cluster_name* in your MongoDB Atlas connection string. This assumes you are using a Gmail account to send emails. If you wish to use a different mail server, use the appropriate values for MAIL_SERVER and MAIL_PORT instead. Information on generating a good secret key can be found [here](https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python). Information on getting your **MongoDB Atlas connection string** can be found [here](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/).

14. If all the steps above have been completed successfully, you can launch the application with the following command and view the site at ```http://127.0.0.1:5000```

        python3 app.py

### Deploy to Heroku

#### Requirements

- An account on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - follow the instructions to create an account
- An email acount for which you can find server details - [Gmail](https://www.google.com/gmail/about/#) works very well for this

#### Deployment Instructions

NOTE: In order to deploy successfully to Heroku, both a *requirements.txt* file and *Procfile* are required. Both of these files are already included in the GitHub repository for this project for your convenience.

1. On the [Heroku](https://www.heroku.com/) website, create a new account if you do not have one already
2. Once logged in and on your Heroku dashboard, create a new app by clicking on the **New** button, followed by **Create new app** in the dropdown menu
3. Enter a name for your app (it must be unique) and a region, such as Europe if you are located in Europe and click on **Create app**
4. On your app page, click on **Settings** in the navigation bar
5. Click on **Reveal Config Vars** in the *Convig Vars* section
6. Set the following Config Vars as key:value pairs

    <table>
    <thead>
      <tr>
        <th>KEY</th>
        <th>VALUE</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>IP</td>
        <td>0.0.0.0</td>
      </tr>
      <tr>
        <td>PORT</td>
        <td>5000</td>
      </tr>
      <tr>
        <td>DEBUG_VALUE</td>
        <td>LEAVE THIS FIELD EMPTY!!!</td>
      </tr>
      <tr>
        <td>MONGO_URI</td>
        <td>&lt;your MongoDB Atlas connection string&gt;</td>
      </tr>
      <tr>
        <td>MONGO_DBNAME</td>
        <td>&lt;your MongoDB Atlas database name&gt;</td>
      </tr>
      <tr>
        <td>MAIL_SERVER</td>
        <td>&lt;smtp.gmail.com&gt;</td>
      </tr>
      <tr>
        <td>MAIL_PORT</td>
        <td>465</td>
      </tr>
      <tr>
        <td>MAIL_USERNAME</td>
        <td>&lt;your Gmail email address&gt;</td>
      </tr>
      <tr>
        <td>MAIL_PASSWORD</td>
        <td>&lt;your Gmail account's app-specific password&gt;</td>
      </tr>
      <tr>
        <td>RECIPIENT_ADDRESS</td>
        <td>&lt;the email address to which you would like emails to be sent&gt;</td>
      </tr>
      <tr>
        <td>SECRET_KEY</td>
        <td>&lt;your secret key&gt;</td>
      </tr>
    </tbody>
    </table>

      NOTE: Wherever text is surrounded by <> (angle brackets), you will need to provide your own values without the angle brackets as determined by your MonogoDB account, mail server and secret key. Remember to change the *username*, *password* and *cluster_name* in your MongoDB Atlas connection string. This assumes you are using a Gmail account to send emails. If you wish to use a different mail server, use the appropriate values for MAIL_SERVER and MAIL_PORT instead. Please not that that the default Gmail settings do not allow third party apps to connect.  You will need to generate a unique password which will be the password for your MAIL_PASSWORD Convig Var in the table above. Information on getting the unique app password can be found [here](https://support.google.com/accounts/answer/185833?hl=en). Information on generating a good secret key can be found [here](https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python). Information on getting your**MongoDB Atlas connection string** can be found [here](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/).

7. Click on **Deploy** in the navigation bar
8. In **Deployment method**, click on GitHub
9. Search for the **wondrousWebWorks** repository and confirm that it has been found. The search result should look similar to this:

        wondrousWebWorks/wondrousWebWorks

10. Click **Connect** and confirm a successful connection
11. Scroll down to the **Manual deploy** section and click on **Deploy Branch**
12. Provided that every step has been followed correctly, the app should be deployed and can be viewed by clicking on the **View** or **Open app** buttons

## Credits

- Image for README.md responsive layouts taken from [Am I Responsive?](http://ami.responsivedesign.is/)
- Hero Shot image on in header was taken from [PNGTREE](https://pngtree.com/)
- Blog images were taken from [Pexels](https://www.pexels.com/)
- Project images were generated using [mockDrop](https://mockdrop.io/)
- README.md tables were created using [Tables Generator](https://www.tablesgenerator.com/)

## Disclaimer

This site is intended for **educational purposes** only, and is not intended for use in any other capacity.
