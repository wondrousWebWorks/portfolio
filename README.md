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
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries, Frameworks & Tools](#libraries-frameworks--tools)
  - [Wireframes](#wireframes)
    - [Differences Between Wireframes and Final Product](#differences-between-wireframes-and-final-product)
      - [Landing Page (Skills section)](#landing-page-skills-section)
  - [Bugs](#bugs)
    - [Development Bugs](#development-bugs)
    - [Deployment Bugs](#deployment-bugs)
  - [Local Installation](#local-installation)
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

## Local Installation

If you want to download the project to view or modify the code locally on your machine, follow the following instructions. Please note that your local changes can't be pushed to the GitHub repository, and that the values of environment variables are not provided as they contain sensitive information.

1. Ensure Git is installed on your local machine (installation instructions can be found [here](https://git-scm.com/downloads))
2. Using your browser of choice, navigate to the [wondrousWebWorks repository](https://github.com/wondrousWebWorks/wondrousWebWorks) in GitHub
3. Click on the green **Clone or download** button on the right of the screen (on personal computers) which will trigger a dropdown menu
4. Copy the URL provided
5. Using your terminal of choice, create or navigate to the directory or folder where you'd like to install the wondrousWebWorks project directory
6. Enter the following command and paste the URL copied, or just copy the command from here, paste it in the terminal enter press Enter
    1. `git clone https://github.com/wondrousWebWorks/wondrousWebWorks.git`
7. Wait for the the repository to be cloned
8. Open the newly cloned wondrousWebWorks folder in your favourite IDE or text editor

Note that in step 4 above, a ZIP file can be downloaded instead of copying the provided URL. Should you choose to download the ZIP file, use whatever software is available on your computer to unzip the file and proceed to step 8 above.

## Credits

- Image for README.md responsive layouts taken from [Am I Responsive?](http://ami.responsivedesign.is/)
- Hero Shot image on in header was taken from [PNGTREE](https://pngtree.com/)
- Blog images were taken from [Pexels](https://www.pexels.com/)
- Project images were generated using [mockDrop](https://mockdrop.io/)

## Disclaimer

This site is intended for **educational purposes** only, and is not intended for use in any other capacity.
