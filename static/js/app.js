/*jshint esversion: 6 */
/* PORTFOLIO HOME PAGE */
const cursorRectangle = document.querySelectorAll('.cursor-rectangle');
const skillBarsWrappers = document.querySelectorAll('.skill-bars-wrapper');
const skillBars = document.querySelectorAll('.skill-bar');
const projects = document.querySelectorAll('.project-col');

/* NAVBAR */
const toggleMenuIcon = document.querySelector('.menu-toggle-icon');
const sideNav = document.querySelector('.nav-display-col');

/* ADMIN SHARED */
const buttons = document.querySelectorAll('button');

/* ADMIN SKILLS */
const skillUpdateButtons = document.querySelectorAll('.update-skill-btn');
const skillDeleteButtons = document.querySelectorAll('.delete-skill-btn');
const skillModal = document.getElementById('skills-form-modal');
const skillForm = document.getElementById('skills-form');
const skillFormLabels = document.querySelectorAll('.skills-form-label');
const skillFormSubmitButton = document.getElementById('skills-form-submit-btn');
const skillFormSubmitButtonText = document.getElementById('skills-form-submit-btn-text');
const skillFormDocId = document.getElementById('skill-form-doc-id');
const skillsAlert = document.getElementById('skills-alert');
const skillFormInputs = document.querySelectorAll('#skills-form input');
const skillName = document.getElementById('skill-name');
const skillLevel = document.getElementById('skill-level');

/* ADMIN PROJECTS */
const projectUpdateButtons = document.querySelectorAll('.update-project-btn');
const projectDeleteButtons = document.querySelectorAll('.delete-project-btn');
const projectModal = document.getElementById('projects-form-modal');
const projectForm = document.getElementById('projects-form');
const projectFormLabels = document.querySelectorAll('.projects-form-label');
const projectFormSubmitButton = document.getElementById('projects-form-btn');
const projectFormSubmitButtonText = document.getElementById('projects-form-submit-btn-text');
const projectFormDocId = document.getElementById('project-form-doc-id');
const projectsAlert = document.getElementById('projects-alert');
const projectFormInputs = document.querySelectorAll('#projects-form input');
const projectName = document.getElementById('project-name');
const projectImgUrl = document.getElementById('project-img-url');
const projectGithubUrl = document.getElementById('project-github-url');
const projectDeployedUrl = document.getElementById('project-deployed-url');
const projectTechnologies = document.getElementById('project-technologies');
const projectDescriptionParagraphs = document.querySelectorAll('.project-description-paragraph');

/* ADMIN QUALIFICATIONS */
const qualificationUpdateButtons = document.querySelectorAll('.update-qualification-btn');
const qualificationDeleteButtons = document.querySelectorAll('.delete-qualification-btn');
const qualificationModal = document.getElementById('qualifications-form-modal');
const qualificationForm = document.getElementById('qualifications-form');
const qualificationFormLabels = document.querySelectorAll('.qualifications-form-label');
const qualificationFormSubmitButton = document.getElementById('qualifications-form-submit-btn');
const qualificationFormSubmitButtonText = document.getElementById('qualifications-form-submit-btn-text');
const qualificationFormDocId = document.getElementById('qualification-form-doc-id');
const qualificationsAlert = document.getElementById('qualifications-alert');
const qualificationFormInputs = document.querySelectorAll('#qualifications-form input');
const qualificationName = document.getElementById('qualification-name');
const qualificationFrom = document.getElementById('qualification-from');
const qualificationIssueDate = document.getElementById('qualification-issue-date');
const qualificationViewUrl = document.getElementById('qualification-view-url');
const qualificationInfoUrl = document.getElementById('qualification-info-url');

/* ADMIN BLOGS */
const blogPostUpdateButtons = document.querySelectorAll('.update-blog-post-btn');
const blogPostDeleteButtons = document.querySelectorAll('.delete-blog-post-btn');
const blogModal = document.getElementById('blogs-form-modal');
const blogForm = document.getElementById('blogs-form');
const blogFormLabels = document.querySelectorAll('.blogs-form-label');
const blogFormSubmitButton = document.getElementById('blogs-form-submit-btn');
const blogFormSubmitButtonText = document.getElementById('blogs-form-submit-btn-text');
const blogFormDocId = document.getElementById('blogs-form-doc-id');
const blogAlert = document.getElementById('blogs-alert');
const blogFormInputs = document.querySelectorAll('#blogs-form input');
const blogTitle = document.getElementById('blog-title');
const blogImgUrl = document.getElementById('blog-img-url');
const blogSummary = document.getElementById('blog-summary');
const blogDate = document.getElementById('blog-date');
const blogParagraphs = document.querySelectorAll('.blog-paragraph');

/* ADMIN EXPERIENCE */
const experienceUpdateButtons = document.querySelectorAll('.update-experience-btn');
const experienceDeleteButtons = document.querySelectorAll('.delete-experience-btn');
const experienceModal = document.getElementById('experience-form-modal');
const experienceForm = document.getElementById('experience-form');
const experienceFormLabels = document.querySelectorAll('.experience-form-label');
const experienceFormSubmitButton = document.getElementById('experience-form-submit-btn');
const experienceFormSubmitButtonText = document.getElementById('experience-form-submit-btn-text');
const experienceFormDocId = document.getElementById('experience-form-doc-id');
const experienceAlert = document.getElementById('experience-alert');
const experienceFormInputs = document.querySelectorAll('#experience-form input');
const experienceJobTitle = document.getElementById('job-title');
const experienceJobDates = document.getElementById('job-dates');



document.addEventListener('DOMContentLoaded', function () {
    /**
     * Animates the terminal-like cursor in the
     * About summary section in index.html
     */
    function animateCursor() {
        setInterval(function () {
            cursorRectangle.forEach(cursor => {
                cursor.classList.toggle('cursor-hide');
            });

        }, 800);
    }

    /**
     * Sets a random height in percentage for
     * each skill bar and also sets an attribute
     * as either rising or falling
     */
    function randomizeInitialSkillBarHeight() {
        skillBarsWrappers.forEach(skillBarsWrapper => {
            const skillLevel = parseInt(skillBarsWrapper.getAttribute('data-skill-level'));
            const skillBars = skillBarsWrapper.children;

            for (let i = 0; i < skillBars.length; i++) {
                if (skillLevel == 0) {
                    continue;
                } else {
                    const skillBarRandomHeight = Math.floor(Math.random() * (skillLevel - 3) + 3);
                    skillBars[i].style.height = `${skillBarRandomHeight}%`;
                    const skillBarRisingOrFalling = Math.random();
                    if (skillBarRisingOrFalling < 0.5) {
                        skillBars[i].setAttribute('data-rising-falling', 'falling');
                    } else {
                        skillBars[i].setAttribute('data-rising-falling', 'rising');
                    }
                }
            }
        });
    }

    /**
     * Loops through Skills and animates each skill bar
     * so that it does not exceed the set skill level
     */
    function animateSkillBars() {
        let skillBarRising = true;
        setInterval(function () {
            skillBarsWrappers.forEach(skillBarsWrapper => {
                
                const skillLevel = parseInt(skillBarsWrapper.getAttribute('data-skill-level'));
                const skillBarsWrapperChildren = skillBarsWrapper.children;

                for (let i = 0; i < skillBarsWrapperChildren.length; i++) {
                    let currentSkillBarHeight = parseInt(skillBarsWrapperChildren[i].style.height.replace("%", ""));
                    let risingOrFalling = skillBarsWrapperChildren[i].getAttribute('data-rising-falling');
                    
                    if (risingOrFalling == 'rising') {
                        if (currentSkillBarHeight + 3 <= skillLevel) {
                            skillBarsWrapperChildren[i].style.height = `${currentSkillBarHeight + 3}%`;
                        } else {
                            skillBarsWrapperChildren[i].setAttribute('data-rising-falling', 'falling');
                        }
                    } else if (risingOrFalling == 'falling') {
                        if ((currentSkillBarHeight - 3) >= (skillLevel / 1.5)) {
                            skillBarsWrapperChildren[i].style.height = `${currentSkillBarHeight - 3}%`;
                        } else {
                            skillBarsWrapperChildren[i].setAttribute('data-rising-falling', 'rising');
                        }
                    }
                }
            });
        }, 40);
    }

    /**
     * Upon hovering over a project,
     * enlarge the project card whilst
     * shrinking and increasing the opacity
     * of other projects
     */
    function scaleProject() {
        projects.forEach(project => {
            project.classList.add('project-scale-smaller-and-opage');
        });
        this.classList.remove('project-scale-smaller-and-opage');
        this.classList.add('project-scale-bigger');
    }

    /**
     * Upon the mouse leaving a project,
     * restore project card to normal size
     * and opacity
     */
    function shrinkProjects() {
        projects.forEach(project => {
            project.classList.remove('project-scale-smaller-and-opage');
            project.classList.remove('project-scale-bigger');
        });
    }

    /**
     * Toggles the side nav visibility on smaller screens
     */
    function toggleSideNav() {
        this.classList.toggle('menu-toggle-icon-expand');
        sideNav.classList.toggle('nav-slide');
    }

    /**
     * Redirects to a given URL based on redirect parameter
     * @param {string} redirect 
     */
    function reloadTargetURL(redirect) {
        window.location.replace(`${window.origin}/admin/${redirect}`);
    }

    /**
     * Briefly displays a success or failure message on screen following
     * a Create, Update or Delete operation
     * @param {Node} targetElement - DOM element to target
     * @param {string} successOrFailure - success or failure string
     * @param {string} type - skill, project, qualification, blog or experience
     * @param {string} action - added, updated or deleted
     * @param {string} redirect - skills, projects, qualifications, blogs or experience
     */
    function flashAlert(targetElement, successOrFailure, type, action, redirect) {
        targetElement.style.display = 'block';
        if (successOrFailure == "success") {
            targetElement.classList.add('alert-success');
            targetElement.children[0].innerText = `${type} successfully ${action} `;
        } else {
            targetElement.classList.add('alert-failure');
            targetElement.children[0].innerText = `${type} failed to be ${action}`;
        }
        
        setTimeout(function() {
            targetElement.style.display = 'none';
            reloadTargetURL(redirect); 
        }, 2500);
    }

    /**
     * Reset any form to its original empty state
     * @param {string} formTarget 
     */
    function resetForm(formTarget) {
        let formInputElements;
        let formLabels;
        changeFormButton('add', formTarget);

        if (formTarget === 'skills') {
           formInputElements = skillFormInputs;
           formLabels = skillFormLabels;
           formInputElements.forEach(input => {
               input.value = null;
               input.classList.remove('valid');
           }); 
        } else if (formTarget === 'projects') {
            formInputElements = projectFormInputs;
            formLabels = projectFormLabels;
            formInputElements.forEach(input => {
                input.value = null;
                input.classList.remove('valid');
            }); 
        } else if (formTarget === 'qualifications') {
            formInputElements = qualificationFormInputs;
            formLabels = qualificationFormLabels;
            formInputElements.forEach(input => {
                input.value = null;
                input.classList.remove('valid');
            }); 
        } else if (formTarget === 'blogs') {
            formInputElements = blogFormInputs;
            formLabels = blogFormLabels;
            formInputElements.forEach(input => {
                input.value = null;
                input.classList.remove('valid');
            }); 
        } else if (formTarget === 'experience') {
            formInputElements = experienceFormInputs;
            formLabels = experienceFormLabels;
            formInputElements.forEach(input => {
                input.value = null;
                input.classList.remove('valid');
            }); 
        }

        Array.from(formLabels).forEach(label => {
            label.classList.remove('active');
        });
    }

    /**
     * Changes the button classes and text for any admin form
     * @param {string} type - add or update
     * @param {string} formTarget - which form to target
     */
    function changeFormButton(type, formTarget) {
        let formTargetButton;
        let formTargetClass = formTarget;
        switch (formTarget) {
            case 'skills': 
                formTarget = skillFormSubmitButton;
                formTargetButton = skillFormSubmitButtonText;
                break;
            case 'projects':
                formTarget = projectFormSubmitButton;
                formTargetButton = projectFormSubmitButtonText;
                break;
            case 'qualifications':
                formTarget = qualificationFormSubmitButton;
                formTargetButton = qualificationFormSubmitButtonText;
                break;
            case 'blogs':
                formTarget = blogFormSubmitButton;
                formTargetButton = blogFormSubmitButtonText;
                break;
            case 'experience':
                formTarget = experienceFormSubmitButton;
                formTargetButton = experienceFormSubmitButtonText;
                break;
            default: formTarget = formTarget; 
        }

        if (type === 'add') {
            formTarget.classList.remove(`${formTargetClass}-form-btn-update`);
            formTarget.classList.add(`${formTargetClass}-form-btn-add`);
            formTargetButton.innerText = 'Add';
        } else if (type === 'update') {
            formTarget.classList.remove(`${formTargetClass}-form-btn-add`);
            formTarget.classList.add(`${formTargetClass}-form-btn-update`);
            formTargetButton.innerText = 'Update';
        }
    }

    /**
     * POSTS data to a specific URL and handles the response
     * @param {string} urlTarget - which admin page to target
     * @param {Object} POST body - key:value pairs
     * @param {Node} alertTargetElement - alert element for specific page
     * @param {string} typeOfDocument - lets the user know what kind of document was added
     */
    function addData(urlTarget, body, alertTargetElement, typeOfDocument) {
        fetch(`${window.origin}/admin/${urlTarget}/add`, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(body),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })
        }).then(response => {
            if (response.status !== 200) {
                console.log(`Response status not 200: ${response.status}`);
                flashAlert(alertTargetElement, 'failure', typeOfDocument, 'added', urlTarget);
                return;
            }
            response.json().then(data => {
                console.log(data);
                flashAlert(alertTargetElement, 'success', typeOfDocument, 'added', urlTarget);
            });
        });   
    }

    /**
     * POSTs a skill to backend and flashes a success
     * or failure alert message
     */
    function addSkillData() {
        const skillEntry = {
            skill_name: skillName.value,
            skill_level: skillLevel.value
        };

        addData('skills', skillEntry, skillsAlert, 'skill');
    }

    /**
     * POSTs a project to backend and flashes a success
     * or failure alert message
     */
    function addProjectData() {
        const projectTechnologiesValues = M.FormSelect.getInstance(projectTechnologies);
        const projectDescription = [];
        projectDescriptionParagraphs.forEach(paragraph => {
            projectDescription.push(paragraph.value);
        });

        const projectEntry = {
            project_name: projectName.value,
            project_img_url: projectImgUrl.value,
            project_github_url: projectGithubUrl.value,
            project_deployed_url: projectDeployedUrl.value,
            project_technologies: projectTechnologiesValues.getSelectedValues(),
            project_description: projectDescription
        };

        console.log(projectEntry);

        addData('projects', projectEntry, projectsAlert, 'project');
    }

    /**
     * POSTs a qualification to backend and flashes a success
     * or failure alert message
     */
    function addQualificationData() {
        const qualificationEntry = {
            qualification_name: qualificationName.value,
            qualification_from: qualificationFrom.value,
            qualification_issue_date: qualificationIssueDate.value,
            qualification_view_url: qualificationViewUrl.value,
            qualification_info_url: qualificationInfoUrl.value
        };

        addData('qualifications', qualificationEntry, qualificationsAlert, 'qualification');
    }

    /**
     * POSTs a blog post to backend and flashes a success
     * or failure alert message
     */
    function addBlogPostData() {
        const blogPostParagraphs = []
        blogParagraphs.forEach(paragraph => {
            blogPostParagraphs.push(paragraph.value);
        });

        const blogPost = {
            blog_title: blogTitle.value,
            blog_img_url: blogImgUrl.value,
            blog_summary: blogSummary.value,
            blog_date: blogDate.value,
            blog_body: blogPostParagraphs
        };

        addData('blogs', blogPost, blogAlert, 'blog post');
    }

        /**
     * POSTs a blog post to backend and flashes a success
     * or failure alert message
     */
    function addExperienceData() {
        const experienceEntry = {
            job_title: experienceJobTitle.value,
            job_dates: experienceJobDates.value
        };

        addData('experience', experienceEntry, experienceAlert, 'experience');
    }

    /**
     * Fetches skill data and populates the skills form
     * fields with it
     */
    function fetchSkillData() {
        dataTarget = this.getAttribute('data-id');
        skillFormDocId.setAttribute('data-id', dataTarget);
        changeFormButton('update', 'skills');
        
        fetch(`${window.origin}/admin/skills/update/${dataTarget}`)
        .then(response => {
            response.json()
            .then(data => {
                skillName.value = data.skill_name;
                skillLevel.value = data.skill_level;
            });
            skillModalInstance.open();
            Array.from(skillFormLabels).forEach(label => {
                label.classList.add('active');
            });
        });
    }

    /**
     * Gets Skills form data and PUTs it to the
     * backend. Flash a success or failure alert
     * depending on response
     */
    function updateSkillData() {
        dataTarget = skillFormDocId.getAttribute('data-id');
        const skill_entry = {
            skill_id: dataTarget,
            skill_name: skillName.value,
            skill_level: skillLevel.value
        };

        fetch(`${window.origin}/admin/skills/update/${dataTarget}`, {
            method: 'PUT',
            credentials: 'include',
            body: JSON.stringify(skill_entry),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })
        }).then(response => {
            if (response.status !== 200) {
                console.log(`Response status not 200: ${response.status}`);
                flashAlert(skillsAlert, 'failure', 'skill', 'updated', 'skills');
                return;
            }

            response.json().then(data => {
                console.log(data);
                flashAlert(skillsAlert, 'success', 'skill', 'updated', 'skills');
            });
        });
    }

    /**
     * Deletes a document by sending a DELETE request to the backend
     * @param {string} type - skills, projects, qualifications, blogs or experience
     * @param {event} event - the button click event
     */
    function deleteDocument(type, event) {
        const dataTarget = event.target.getAttribute('data-id');
        let alertTarget;
        let redirect;

        if (type === 'skill') {
            alertTarget = skillsAlert;
            redirect = 'skills';
        } else if (type === 'project') {
            alertTarget = projectsAlert;
            redirect = 'projects';
        } else if (type === 'qualification') {
            alertTarget = qualificationsAlert;
            redirect = 'qualifications';
        } else if (type === 'blog') {
            alertTarget = blogAlert;
            redirect = 'blogs';
        } else if (type === 'experience') {
            alertTarget = experienceAlert;
            redirect = 'experience';
        }

        fetch(`${window.origin}/admin/${redirect}/delete/${dataTarget}`, {
            method: 'DELETE',
            credentials: 'include',
            headers: new Headers()
        })
        .then(response => {
            if (response.status !== 200) {
                console.log(`Response status not 200: ${response.status}`);
                flashAlert(alertTarget, 'failure', type, 'deleted', redirect);
                return;
            }

            response.json().then(data => {
                console.log(data);
                flashAlert(alertTarget, 'success', type, 'deleted', redirect);
            });
        });
    }

    /**
     * Handles a document click event and traverses up the
     * DOM tree until a condition is met upon which an 
     * appropriate function is called
     * @param {event} event 
     */
    function handleElementsNotLoadedGlobally(event) {
        event = event || window.event;
        event.target = event.target || event.srcElement;

        let element = event.target;
        
        while (element) {
            if (/add-skill-btn/.test(element.className)) {
                changeFormButton('add', 'skills');
                resetForm('skills');
                setTimeout(function() {
                    skillModalInstance.open();               
                }, 400);
                break; 
            } else if (/skills-form-btn-add/.test(element.className)) {
                addSkillData();
                break; 
            } else if (/projects-form-btn-add/.test(element.className)) {
                addProjectData();
                break;
            } else if (/blogs-form-btn-add/.test(element.className)) {
                addBlogPostData();
                break; 
            } else if(/qualifications-form-btn-add/.test(element.className)) {
                addQualificationData();
                break;
            } else if(/experience-form-btn-add/.test(element.className)) {
                addExperienceData();
                break;
            } else if (/skills-form-btn-update/.test(element.className)) {
                updateSkillData();
                break; 
            } else if (/add-project-btn/.test(element.className)) {
                resetForm('projects');
                setTimeout(function() {
                    projectModalInstance.open();               
                }, 400);
                break;
            } else if (/add-qualification-btn/.test(element.className)) {
                resetForm('qualifications');
                setTimeout(function() {
                    qualificationModalInstance.open();               
                }, 400);
                break;
            } else if (/add-blog-post-btn/.test(element.className)) {
                resetForm('blogs');
                setTimeout(function() {
                    blogModalInstance.open();               
                }, 400);
                break;
            } else if (/add-experience-btn/.test(element.className)) {
                resetForm('experience');
                setTimeout(function() {
                    experienceModalInstance.open();               
                }, 400);
                break;
            } 
    
            element = element.parentNode;
        }
    }


    /* EVENT LISTENERS */
    Array.from(projects).forEach(project => {
        project.addEventListener("mouseover", scaleProject);
        project.addEventListener("mouseout", shrinkProjects);
      });

    Array.from(skillUpdateButtons).forEach(updateButton => {
        updateButton.addEventListener('click', fetchSkillData);
    });

    Array.from(skillDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function(event) {
            deleteDocument('skill', event);
        });
    });

    Array.from(projectDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function(event) {
            deleteDocument('project', event);
        });
    });

    Array.from(qualificationDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function(event) {
            deleteDocument('qualification', event);
        });
    });

    Array.from(blogPostDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function(event) {
            deleteDocument('blog', event);
        });
    });

    Array.from(experienceDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function(event) {
            deleteDocument('experience', event);
        });
    });

    Array.from(buttons).forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
        });
    });

    toggleMenuIcon.addEventListener('click', toggleSideNav);
    document.addEventListener( "click", handleElementsNotLoadedGlobally);

    /* INITIALIZE MATERIALIZE COMPONENTS */
    const selectElems = document.querySelectorAll('select');
    const selectInstances = M.FormSelect.init(selectElems);

    const collapsibleElems = document.querySelectorAll('.collapsible');
    const collapsibleInstances = M.Collapsible.init(collapsibleElems, {
        onOpenStart: function(el) {
            el.querySelector('.custom-collapsible-header').style.backgroundColor = '#333';
            el.querySelector('.custom-collapsible-body').style.backgroundColor = '#222';
            el.querySelector('.custom-collapsible-header i').style.transform = 'scaleY(-1)';
        },
        onCloseStart: function(el) {
            el.querySelector('.custom-collapsible-header').style.backgroundColor = '#1f1f1f';
            el.querySelector('.custom-collapsible-body').style.backgroundColor = '#1f1f1f';
            el.querySelector('.custom-collapsible-header i').style.transform = 'scaleY(1)';
        }
    });

    const modalElems = document.querySelectorAll('.modal');
    const modalInstances = M.Modal.init(modalElems);
    const skillModalInstance = M.Modal.init(skillModal);
    const projectModalInstance = M.Modal.init(projectModal);
    const qualificationModalInstance = M.Modal.init(qualificationModal);
    const blogModalInstance = M.Modal.init(blogModal);
    const experienceModalInstance = M.Modal.init(experienceModal);

    /* FUNCTIONS CALLED ON PAGE LOAD */
    animateCursor();
    randomizeInitialSkillBarHeight();
    animateSkillBars();
});