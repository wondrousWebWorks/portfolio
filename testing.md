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
    - [Behaviour of site components](#behaviour-of-site-components)
      - [Navbar (Navigation Bar)](#navbar-navigation-bar)
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

- Chrome - desktop and mobile
- Firefox - desktop and mobile
- Opera - dekstop
- Opera Mini - mobile
- DuckDuckGo - mobile

#### Verdict

No obvious bugs were detected in any of the tested browsers. :heavy_check_mark:

### Behaviour of site components

#### Navbar (Navigation Bar)

- Click on navigation links to confirm correct redirection to the appropriate pages :heavy_check_mark:
- Verify correct transition of navigation links on hover :heavy_check_mark:
- Verify that the so-called **'burger'** menu icon displays on smaller screens :heavy_check_mark:
- Verify that on clicking of the **'burger** icon triggers visibility of the vertical navigation menu for smaller screens :heavy_check_mark:
- Verify that the the appropriate navigation bar is displayed for the **main** and **admin** sites respectively :heavy_check_mark:

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
