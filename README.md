# wondrousWebWorks()

Thank you for viewing my project. wondrousWebWorks() is a profile for me as a full stack developer, including some information about me, skills, experience, acontact section and a portfolio. It also includes an admin page, where the site owner can manage the site and perform CRUD (Create, Read, Update and Delete) operations.

## Contents

- [wondrousWebWorks()](#wondrouswebworks)
  - [Contents](#contents)
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
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries, Frameworks & Tools](#libraries-frameworks--tools)
  - [Wireframes](#wireframes)
    - [Differences Between Wireframes and Final Product](#differences-between-wireframes-and-final-product)
      - [Landing Page (Skills section)](#landing-page-skills-section)
  - [Bugs](#bugs)
    - [Deployment Bugs](#deployment-bugs)
  - [Credits](#credits)

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

#### Landing Page (Skills section)

- On mobile devices in portrait orientation, two skills are displayed per row as opposed to a single skill as illustrated in the wireframe

## Bugs

### Deployment Bugs

Initially, there was great difficulty deploying the project to Heroku.  After viewing the project's Heroku log files, it was discovered that the **pkg-resources** package could not be located by Heroku for installation. Modifying the **requirements.txt** file by removing the **pkg-resources** dependancy before pushing to GitHub and subsequently Heroku fixed the bug and allowed succesfull installion of all dependancies.

## Credits

- Hero Shot image on in header was taken from [PNGTREE](https://pngtree.com/)
- Blog images were taken from [Pexels](https://www.pexels.com/)
