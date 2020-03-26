# wondrousWebWorks()

Thank you for viewing my project. wondrousWebWorks() is a profile for me as a full stack developer, including some information about me, skills, experience, acontact section and a portfolio. It also includes an admin page, where the site owner can manage the site and perform CRUD (Create, Read, Update and Delete) operations.

## Contents

- [wondrousWebWorks()](#wondrouswebworks)
  - [Contents](#contents)
  - [User Experience](#user-experience)
    - [Project Goals](#project-goals)
      - [User Goals](#user-goals)
  - [Bugs](#bugs)
    - [Deployment Bugs](#deployment-bugs)

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

## Bugs

### Deployment Bugs

Initially, there was great difficulty deploying the project to Heroku.  After viewing the project's Heroku log files, it was discovered that the **pkg-resources** package could not be located by Heroku for installation. Modifying the **requirements.txt** file by removing the **pkg-resources** dependancy before pushing to GitHub and subsequently Heroku fixed the bug and allowed succesfull installion of all dependancies.
