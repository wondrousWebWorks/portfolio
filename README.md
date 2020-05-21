# wondrousWebWorks()

[Live Site](https://wondrouswebworks.herokuapp.com/)

Information on using the Admin site can be found [here](#using-the-admin-site)

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1589826600/wondrousWebWorks/wondrouswebworks-responsive-layout.png "wondrousWebWorks() responsive layout for landing page")

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
        - [#E03C31 (sa-flag-red)](#e03c31-sa-flag-red)
        - [#007749 (sa-flag-green)](#007749-sa-flag-green)
        - [#0080ff (sa-flag-blue)](#0080ff-sa-flag-blue)
        - [#FFB81C (sa-flag-gold)](#ffb81c-sa-flag-gold)
        - [#F7F7F7 (off-white)](#f7f7f7-off-white)
  - [Features](#features)
    - [Animated Headings](#animated-headings)
    - [Tablet-style Container](#tablet-style-container)
    - [Animated Skills Listings](#animated-skills-listings)
    - [Project Card Animation and Tooltips](#project-card-animation-and-tooltips)
    - [Collapsible Qualifications](#collapsible-qualifications)
    - [Animated Experience Section](#animated-experience-section)
  - [Using the Admin Site](#using-the-admin-site)
    - [Login Procedure](#login-procedure)
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
    - [Changes for Both Landscape and Portrait Orientation](#changes-for-both-landscape-and-portrait-orientation)
      - [Landing Page (Projects section) - landscape and portrait](#landing-page-projects-section---landscape-and-portrait)
      - [Landing Page (Experience section) - landscape and portrait](#landing-page-experience-section---landscape-and-portrait)
      - [Admin Management Changes - landscape and portrait](#admin-management-changes---landscape-and-portrait)
      - [Admin Skills - landscape and portrait](#admin-skills---landscape-and-portrait)
      - [Admin Projects - landscape and portrait](#admin-projects---landscape-and-portrait)
    - [Devices in Landscape Orientation](#devices-in-landscape-orientation)
      - [About Page - landscape](#about-page---landscape)
      - [Portfolio Page - landscape](#portfolio-page---landscape)
      - [Contact Page - landscape](#contact-page---landscape)
      - [Blogs Page - landscape](#blogs-page---landscape)
      - [Blog Post Page - landscape](#blog-post-page---landscape)
      - [Login Page - landscape](#login-page---landscape)
      - [Admin Dashboard - landscape](#admin-dashboard---landscape)
    - [Devices in Portrait Orientation](#devices-in-portrait-orientation)
      - [Landing Page (Skills Section) - portrait](#landing-page-skills-section---portrait)
        - [Tablet Devices - portrait](#tablet-devices---portrait)
        - [Mobile Devices - portrait](#mobile-devices---portrait)
      - [About Page - portrait](#about-page---portrait)
      - [Portfolio Page - portrait](#portfolio-page---portrait)
      - [Project Page - portrait](#project-page---portrait)
      - [Contact Page - portrait](#contact-page---portrait)
      - [Blogs Page - portrait](#blogs-page---portrait)
        - [Tablet Devices - portrait](#tablet-devices---portrait-1)
      - [Blog Post Page - portrait](#blog-post-page---portrait)
        - [Tablet Devices - portrait](#tablet-devices---portrait-2)
        - [Mobile Devices - portrait](#mobile-devices---portrait-1)
      - [Login Page - portrait](#login-page---portrait)
      - [Admin Dashboard - portrait](#admin-dashboard---portrait)
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
- Create a site that is future proof and allows for the addition of additional skills, projects, blog posts, education and work experience

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

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1589668312/wondrousWebWorks/wondrousWebWorks-color-palette.png "wondrousWebWorks() colour palette")

 **Eerie black** (*#1c1c1c* in hex) was chosen as background colour for the site body as the site was designed to be displayed in "dark mode". In order to make text legible, **#f7f7f7** was chosen as text colour. All other colours were taken from the South African flag and named by me; a subtle homage to my origin. See below for more details.  All colours complement each other very well, and provide a good level of contrast to increase legibility and highlight various areas of the page.

##### #1C1C1C (Eerie Black)

- Background colour for main site body and admin body

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

##### #0080ff (sa-flag-blue)

- Background colour of the *more info* buttons in the **Education** section
- Background-colour of all modal *close* buttons
- Background colour of all **Manage** buttons on the Admin dashboard

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

##### #F7F7F7 (off-white)

- Used for all text, except blog post dates

## Features

Some features of the site can be viewed below.  It is by no means a list of all features, but only those I deem noteworthy.

### Animated Headings

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1590047223/wondrousWebWorks/gifs/wondrouswebworks-heading_ehcnvn.gif "gif of animated heading")

### Tablet-style Container

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1590047223/wondrousWebWorks/gifs/wondrouswebworks-tablet-style-animation_aa3a1c.gif "gif of tablet-style container with flashing cursor")

### Animated Skills Listings

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1590047223/wondrousWebWorks/gifs/wondrouswebworks-skills-animation_ve6pxr.gif "gif of animated skill listing")

### Project Card Animation and Tooltips

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1590047223/wondrousWebWorks/gifs/wondrouswebworks-projects-animation_h9m8mi.gif "gif of project card animation and tooltips")

### Collapsible Qualifications

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1590047223/wondrousWebWorks/gifs/wondrouswebworks-qualifications-animation_tzuf5u.gif "gif of collapsible qualifications")

### Animated Experience Section

![alt text](https://res.cloudinary.com/wondrouswebworks/image/upload/v1590047223/wondrousWebWorks/gifs/wondrouswebworks-experience-animation_thjtsf.gif "gif of animated work experience")

## Using the Admin Site

For the sake of testing, users can test the functionality of the Admin page by logging in with a guest account.  As the site does not require users to register or create accounts, the login details for trhe deployed testing site are provided here instead.

**NOTE Should you wish to deploy the site with your own data, use your login details instead.**

**NOTE** Trying to access any Admin page by typing the URL into the browser's search bar will redirect the user to the **Login** page automatically and inform them of the need to be logged in to access that particular resource.

### Login Procedure

1. Navigate to either the **admin** or **login** page. 
    - On the example deployed site they can be found [**here for Admin**](https://wondrouswebworks.herokuapp.com/admin) and [**here for Login**](https://wondrouswebworks.herokuapp.com/login) page
    - If you wish to access it locally or where you have deployed the site, navigate to the **Home** page by clicking **Home** link in the navbar at the top of the page. Add either of the following to the end of the URL in the browser `/admin` or `/login`
2. Enter the following login details in the form input fields:
   - Email: guest@test.com
   - Password: M@ryH@d@L1ttl3L@mb
3. Click on the **login** button

If the above steps are followed, the user should be logged in and redirected to the Admin Dashboard. A new link will appear in the navbar, **Log out**. Clicking on this will log the user out and login will be required if access to the Admin page is required again.

## Information Architecture

Information on using the Admin site can be found [here](#using-the-admin-site)

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

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
- [Python](https://www.python.org/about/)

### Libraries, Frameworks & Tools

- [Flask](https://palletsprojects.com/p/flask/)
- [MongoDB (Atlas Cloud)](https://www.mongodb.com/cloud/atlas)
- [Git](https://git-scm.com/about)
- [Materialize](https://materializecss.com/about.html)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Cloudinary](https://cloudinary.com/about)

## Wireframes

[Balsamiq Mockups 3](https://balsamiq.com/) was used to design all mockups. Wireframes for desktop, mobile and tablet can be viewed [here](https://github.com/wondrousWebWorks/wondrousWebWorks/tree/master/wireframes). There are some differences between the wireframes and the end product due to user feedback during testing to improve the UX (User Experience).  These changes are highlighted below.

The text in the **page header** and the **page header button** changes dynamically depending on which page is loaded. Other changes are listed below.

### Changes for Both Landscape and Portrait Orientation

#### Landing Page (Projects section) - landscape and portrait

- Instead of using square buttons with text for the links to project **GitHub reposities** and **Deployed Sites**, the icons only were used without any text. A tooltip does provide more information on hover of the icons, though.

#### Landing Page (Experience section) - landscape and portrait

- A timeline was used to display work experience instead of the card system.  This makes it easier to read while reflecting more modern design convention.

#### Admin Management Changes - landscape and portrait

- An **Add* button is displayed below the page heading
- Documents are not listed in a collapsible structure, but simply with the **Edit** and **Delete** buttons listed on the same row as each document
- Instead of loading separate pages for **adding** or **updating** documents, a form modal is triggered when clicking on either the **Add** or **Edit** buttons
- The submit button text is **Update** instead of **Confirm Edit** in forms for **editing** documents

#### Admin Skills - landscape and portrait

- The **Add Skill** form no longer has an input field for *Skill Image URL* as it was too difficult to find consitent images for all skills used
- The **Edit Skill** form no longer has an input field for *Skill Image URL*

#### Admin Projects - landscape and portrait

- **Five** textarea inputs are provided for **Project Description** paragraphs **instead of seven**

### Devices in Landscape Orientation

#### About Page - landscape

- The image is displayed below the opening paragraph text and to the right of the screen
- On the left of the image is a list with the developer's main qualities and characteristics

#### Portfolio Page - landscape

- The same changes as were made for the **Project** cards in the **Projects** section on the **Landing Page**

#### Contact Page - landscape

- The **Name** and **Last Name** fields were removed
- A **Subject** input field was added

#### Blogs Page - landscape

- The **Blog Title**, **Blog Date** and **Blog Summary** are now displayed on the Blog Post's background image
- The **Read** button was removed while clicking on the **card text** will now direct the user to the appropriate blog post

#### Blog Post Page - landscape

- The **image** for the **Blog Post** is now on the right of the screen

#### Login Page - landscape

- The **navbar** for the portfolio site **is displayed** at the top at the screen
- The *page heading* is **Log In** instead of **Sign In**
- The **footer** contains the same links as other pages for the **portfolio** site

#### Admin Dashboard - landscape

- **Horizontal navbar** used at the top of the page *instead of a side navigation bar*
- The new **navbar** does not have links to **Add** or **Manage** any of the collections
- Instead of displaying the **collections** in a 2 x 1 x 2 arrangement, three collections (Skills, Projects, Qualifications) are listed in one row, while two collections (Blogs, Experience) are listed on another row
- Instead of having an **Add** button below each collection count, a **Manage** button is displayed which will direct the the user to the appropriate management page

### Devices in Portrait Orientation

#### Landing Page (Skills Section) - portrait

##### Tablet Devices - portrait

- **Four** Skills are listed per row **instead of three**

##### Mobile Devices - portrait

- **Two** Skills are listed per row **instead of three**

#### About Page - portrait

- Below the opening paragraph text is a list with the developer's main qualities and characteristics
- The image is displayed below the list with the developer's main qualities and characteristics

#### Portfolio Page - portrait

- The same changes as were made for the **Project** cards in the **Projects** section on the **Landing Page**

#### Project Page - portrait

- The **project image** and **technology list** are not displayed side-by-side
- The **project image** is displayed first
- The **technology list** is displayed below the **project image**

#### Contact Page - portrait

- The same changes as were made for the **Contact** page in devices in *landscape orientation*

#### Blogs Page - portrait

- The same changes as for **Blog Post** cards on devices with a landscape orientation

##### Tablet Devices - portrait

- **Two** Blog Post cards are displayed per row instead of **one**

#### Blog Post Page - portrait

##### Tablet Devices - portrait

- The same layout as for devices in landscape orientation

##### Mobile Devices - portrait

- The **blog image** is displayed below the **blog title** and **blog date**

#### Login Page - portrait

- The same as for devices in landscape orientation

#### Admin Dashboard - portrait

- The same as for devices in landscape orientation with the following exception:
  - The navbar is vertical and animates the same as the **Portfolio** site's

## Deployment

The project can be run either locally or deployed on Heroku.  Instructions for either option can be viewed below.

Information on using the Admin site can be found [here](#using-the-admin-site)

### Local Installation

#### Requirements

**NOTE: The instructions provided are for installing on a Debian-based Linux operating system. Should your operating system be different, please note that some of the commands might be different.**

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

   It considered good practice to contain each product in each own virtual environment as any dependancies for each project can be installed locally in each project's virtual environment. Several virtual environments exist and since Python 3.3, a subset of the popular [virtualenv](https://virtualenv.pypa.io/en/latest/) comes as standard with all Python 3 installations. This subset does not offer the full fetaure set of the full **virtualenv** package, and as such is recommended to install **virtualenv** using **pip**.

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

    NOTE: Wherever text is surrounded by <> (angle brackets), you will need to provide your own values without the angle brackets as determined by your **MongoDB account**, **mail server** and **secret key**.

    NOTE: Remember to change the **username**, **password** and **cluster_name** in your MongoDB Atlas connection string. Information on getting your **MongoDB Atlas connection string** can be found [here](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/).

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

    NOTE: If you wish to use a mail service other than Gmail, use the appropriate values for **MAIL_SERVER** and **MAIL_PORT** instead.

    NOTE: Information on generating a good secret key can be found [here](https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python).

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

      NOTE: Wherever text is surrounded by <> (angle brackets), you will need to provide your own values without the angle brackets as determined by your MongoDB account, mail server and secret key. Remember to change the **username**, **password** and **cluster_name** in your MongoDB Atlas connection string. Information on getting your**MongoDB Atlas connection string** can be found [here](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/).

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

      NOTE: If you wish to use a mail service other than Gmail, use the appropriate values for **MAIL_SERVER** and **MAIL_PORT** instead. Please not that that the default Gmail settings do not allow third party apps to connect.  You will need to generate a unique password which will be the password for your **MAIL_PASSWORD** Convig Var in the table above. Information on getting the unique app password can be found [here](https://support.google.com/accounts/answer/185833?hl=en).

      NOTE: Information on generating a good secret key can be found [here](https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python).

7. Click on **Deploy** in the navigation bar
8. In **Deployment method**, click on GitHub
9. Search for the **wondrousWebWorks** repository and confirm that it has been found. The search result should look similar to this:

        wondrousWebWorks/wondrousWebWorks

10. Click **Connect** and confirm a successful connection
11. Scroll down to the **Manual deploy** section and click on **Deploy Branch**
12. Provided that every step has been followed correctly, the app should be deployed and can be viewed by clicking on the **View** or **Open app** buttons

Information on using the Admin site can be found [here](#using-the-admin-site)

## Credits

- Image for README.md responsive layouts taken from [Am I Responsive?](http://ami.responsivedesign.is/)
- Hero Shot image on in header was taken from [PNGTREE](https://pngtree.com/)
- Blog images were taken from [Pexels](https://www.pexels.com/)
- Project images were generated using [mockDrop](https://mockdrop.io/)
- README.md tables in Information Architecture were created using [Tables Generator](https://www.tablesgenerator.com/)

## Disclaimer

This site is intended for **educational purposes** only, and is not intended for use in any other capacity.
