# Testing & Bugs

- [Testing & Bugs](#testing--bugs)
  - [Bugs](#bugs)
    - [Development Bugs](#development-bugs)
      - [Heroku Deployment Issue](#heroku-deployment-issue)

## Bugs

### Development Bugs

As with many a project, I encountered a few bugs during development which required squashing. These are listed below, along with their fixes.

#### Heroku Deployment Issue

- Bug
  Initially, there was great difficulty deploying the project to Heroku.  After viewing the project's Heroku log files, it was discovered that the **pkg-resources** package could not be located by Heroku for installation. This requirement was added to the **requirements.txt** file on running the command `pip3 freeze --local > requirements.txt` to create the file.
- Fix
  Modified the **requirements.txt** file by removing the **pkg-resources** dependancy before pushing to GitHub.
- Verdict
  Successfully deployed to Heroku with all dependancies installed.
  At one stage, I couldn't get flashed messages to display on my Admin page, and decided to replicate the same functionality in Javascript as best I could only to realise that I'd forgotten to add the flash messages functionality to both the base.html **and** admin-base.html files.  Upon discovery of this oversight, I implemented Flask's messaging system and removed the unnecessary JavaScript function which mimicked the same functionality.
