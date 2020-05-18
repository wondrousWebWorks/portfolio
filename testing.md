# Testing & Bugs

- [Testing & Bugs](#testing--bugs)
  - [Testing](#testing)
    - [Responsiveness](#responsiveness)
      - [Desired Result](#desired-result)
      - [Steps Taken to Ensure Result](#steps-taken-to-ensure-result)
      - [Verdict](#verdict)
    - [Cross-browser Compatability](#cross-browser-compatability)
      - [Desired Result](#desired-result-1)
      - [Steps Taken to Ensure Result](#steps-taken-to-ensure-result-1)
      - [Verdict](#verdict-1)
    - [Behaviour of Shared Site Components](#behaviour-of-shared-site-components)
      - [Navbar (Navigation Bar)](#navbar-navigation-bar)
      - [Page Header and Call To Action](#page-header-and-call-to-action)
    - [Behaviour of Individual Pages](#behaviour-of-individual-pages)
      - [Home Page (index.html)](#home-page-indexhtml)
        - [About Summary](#about-summary)
        - [Skills](#skills)
        - [Projects](#projects)
        - [Qualifications](#qualifications)
        - [Experience](#experience)
      - [About Page (about.html)](#about-page-abouthtml)
      - [Projects Page (projects.html)](#projects-page-projectshtml)
      - [Project Page (project.html)](#project-page-projecthtml)
      - [Blog (blogs.html)](#blog-blogshtml)
  - [Bugs](#bugs)
    - [Development Bugs](#development-bugs)
      - [Heroku Deployment Issue](#heroku-deployment-issue)

## Testing

Manual testing was performed for this project, as form validation was used to present incorrect data being sent to the backend. All other behaviour, such as navigation, responsiveness, login and CRUD operations could also be assessed manually.

### Responsiveness

#### Desired Result

The site is displayed on any screen size without compromising legibility and eliminating screen and element overflow.

#### Steps Taken to Ensure Result

Materialize was used as a library to create wondrousWebWorks(). In particular, its grid system was used extensively to ensure responsiveness on any screen size. It proved necessary to use CSS media queries for width and height, as well as orientation to display the content as intended on mobile and tablet devices in both portrait and landscape mode.

In addition to testing using responsiveness using Chrome Developer Tools, these physical devices were also used for testing:

- Sony Xperia Xa2
- Samsung J5, Galaxy S10 Lite, Galaxy S20
- Apple iPhone XR, 11, iPad Pro
- Amazon Fire HD 7 Inch tablet
- Dell Inspiron 5490 Laptop

#### Verdict

wondrousWebWorks() adapts to all tested screen sizes and devices and displays as expected. :heavy_check_mark:

### Cross-browser Compatability

#### Desired Result

Display correctly in any browser users are likely to use, except for older versions of Internet Explorer.

#### Steps Taken to Ensure Result

A a range of browsers were used to test the site, and where I did not have access to it - such as Safari - I borrowed Apple devices to test for potential bugs.

As Firefox does not support the WebKit browser rendering engine, steps were taken to ensure an approximation of the same functionailty and styling in the Firefox browser. An exmaple of this would be custom scrollbar styling, where Firefox uses the more modern CSS scrollbar styling tool. Including this not only makes the scrollbars display correctly in Firefox, but also makes the site future proof as the WebKit spec has been abandoned by W3C (World Wide Web Consortium) and will be deprecated eventually.

Browsers tested include:

- [Chrome](https://www.google.com/chrome/) - desktop and mobile
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) - desktop and mobile
- [Opera](https://www.opera.com/computer/opera) - dekstop
- [Opera Mini](https://www.opera.com/mobile/mini) - mobile
- [DuckDuckGo](https://duckduckgo.com/app) - mobile

#### Verdict

No obvious bugs were detected in any of the tested browsers. :heavy_check_mark:

### Behaviour of Shared Site Components

#### Navbar (Navigation Bar)

- Click on navigation links to confirm correct redirection to the appropriate pages :heavy_check_mark:
- Verify correct transition of navigation links on hover :heavy_check_mark:
- Verify that the so-called **'burger'** menu icon displays on smaller screens :heavy_check_mark:
- Verify that on clicking of the **'burger** icon triggers visibility of the vertical navigation menu for smaller screens :heavy_check_mark:
- Verify that the the appropriate navigation bar is displayed for the **main** and **admin** sites respectively :heavy_check_mark:

#### Page Header and Call To Action

- Verify that page header displays at full page height on the **index.html** and **404.html** pages :heavy_check_mark:
- Verify that the page header displays at less than full page height on all other pages for the main site (excludes Admin pages) :heavy_check_mark:
- Confirm that the **Call To Action** text (name jumbotron in the HTML and CSS for this project) is displayed dynamically for each page (excludes Admin pages) :heavy_check_mark:
- Confirm that the **Call To Action** button text changes dynamically for each page (excludes Admin pages) :heavy_check_mark:
- Verify that the **Call To Action** button allows for scrolling to the desired page content on all main site pages excluding **index.html** :heavy_check_mark:
- Confirm that clicking the **Call To Action** button on the **index.html** page redirects to the Contact page :heavy_check_mark:

### Behaviour of Individual Pages

#### Home Page (index.html)

##### About Summary

- Confirm that text is rendered to resemble a tablet :heavy_check_mark:
- Confirm that all colours display correctly :heavy_check_mark:
- Verify that cursor animates as expected to resemble a terminal cursor :heavy_check_mark:

##### Skills

- Confirm that all skills are displayed :heavy_check_mark:
- Confirm that 3 skill bars are present and animated for each skill :heavy_check_mark:
- Verify that each of the three skill bars per skill is a different colour as expected :heavy_check_mark:
- Verify that no skill exceeds the 100% limit :heavy_check_mark:
- Confirm that each skill's **name** and **level** is displayed correctly :heavy_check_mark:
- Confirm that each skill's housing gives a 3D effect as intended :heavy_check_mark:
- Verify that each skill's housing is circular in shape :heavy_check_mark:

##### Projects

- Confirm that a maximum of **three** projects are displayed :heavy_check_mark:
- Verify that each project card has an **image**, and that if no image is supplied, alt text it displayed :heavy_check_mark:
- Verify that each project card has the **project title** :heavy_check_mark:
- Confirm that each project card has a clickable **icon** which opens the project's **GitHub repository** in a new tab :heavy_check_mark:
- Confirn that each project card has a clickable **icon** which opens the **deployed project** in a new tab :heavy_check_mark:
- Verify that hovering over a project card **scales** that project card to be bigger, while other project cards are scaled smaller and less opaque :heavy_check_mark:

##### Qualifications

- Confirm that all qualifications are listed :heavy_check_mark:
- Verify that **hovering** over qualification name gives expected **colour transitioning effect** (lighter) :heavy_check_mark:
- Verify that **clicking** on **qualification name** triggers the visibility of a qualification body to show additional information and set the qualification name (heading) background colour to a lighter shade of grey :heavy_check_mark:
- Confirm that the qualification body contains the following components and behaviour:
  - Confirm that the **icon** and information for the **issuing Institute / Authority** is listed :heavy_check_mark:
  - Confirm that the **icon** and information for the **issue date** is listed :heavy_check_mark:
  - Confirm that **VIEW** and **MORE INFO** buttons are present :heavy_check_mark:
  - Verify that **clicking** on the **VIEW** and **MORE INFO** buttons **redirects** to the relevant information in a new browser tab :heavy_check_mark:
- Verify that **clicking** on a **qualification name** once expanded **hides** the qualification body as expected and sets the qualification name's background to the **default colour** :heavy_check_mark:

##### Experience

- Confirm that experience cards are present :heavy_check_mark:
- Verify that each experience card shows a **tag icon** for the job title and the **job title** itself :heavy_check_mark:
- Verify that each experiecne card shows a **calendar icon** for the job dates and the **job dates** themselves :heavy_check_mark:
- Confirm that the cards scale on hover :heavy_check_mark:

#### About Page (about.html)

- Confirm that **About**inforation is rendered to resemble a tablet (similar to About Summary) :heavy_check_mark:
- Confirm that all **colours** display correctly :heavy_check_mark:
- Verify that **cursor** animates as expected to resemble a **terminal cursor** :heavy_check_mark:
- Verify that the **list** and **image** display *side-by-side on bigger screens*, but *below each other on smaller screens* :heavy_check_mark:

#### Projects Page (projects.html)

- Confirm that all projects are displayed :heavy_check_mark:
- Verify that each project card has an **image**, and that if no image is supplied, alt text it displayed :heavy_check_mark:
- Verify that each project card has the **project title** :heavy_check_mark:
- Confirm that each project card has a clickable **icon** which opens the project's **GitHub repository** in a new tab :heavy_check_mark:
- Confirn that each project card has a clickable **icon** which opens the **deployed project** in a new tab :heavy_check_mark:
- Verify that hovering over a project card **scales** that project card to be bigger, while other project cards are scaled smaller and less opaque :heavy_check_mark:
- Confirm that **clicking** on a project card image or heading opens the **project.html** page with the relevant information for the specific project :heavy_check_mark:

#### Project Page (project.html)

- Verify that the correct **project image** is displayed :heavy_check_mark:
- Confirm that the full **technology list** for the project is displayed :heavy_check_mark:
- Confirm that **all paragraphs** for the project is displayed correctly :heavy_check_mark:
- Verify that the **project image** and **technology list** display *side-by-side o tablet devices* and *devices with bigger screens* :heavy_check_mark:
- Confirm that the **project image** and **technology list** display *vertically* on *mobile devices in portrait mode* :heavy_check_mark:

#### Blog (blogs.html)

- Confirm that **cards** for **all blogs** are displayed :heavy_check_mark:
- Confirm that each card has the correct **image as background** :heavy_check_mark:
- Verify that the correct **blog title** is displayed on each card :heavy_check_mark:
- Confirm that the **blog summary** is displayed on card *hover* :heavy_check_mark:
- Confirm that the correct **published date** is displayed on each blog card :heavy_check_mark:
- Verify that **clicking** on the **blog card text** opens the targeted *blog post in a new tab* :heavy_check_mark:

## Bugs

### Development Bugs

As with many a project, I encountered a few bugs during development which required squashing. These are listed below, along with their fixes.

#### Heroku Deployment Issue

- **Bug**

    Initially, there was great difficulty deploying the project to Heroku.  After viewing the project's Heroku log files, it was discovered that the **pkg-resources** package could not be located by Heroku for installation. This requirement was added to the **requirements.txt** file on running the command `pip3 freeze --local > requirements.txt` to create the file.

- **Fix**

    Modified the **requirements.txt** file by removing the **pkg-resources** dependancy before pushing to GitHub.

- **Verdict**

    Successfully deployed to Heroku with all dependancies installed.
