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

/* ADMIN SKILLS */
const skillUpdateButtons = document.querySelectorAll('.update-skill-btn');
const skillDeleteButtons = document.querySelectorAll('.delete-skill-btn');
const skillName = document.getElementById('skill-name');
const skillLevel = document.getElementById('skill-level');
const skillModal = document.getElementById('skills-form');
const skillFormLabels = document.querySelectorAll('.skills-form-label');
const skillFormButton = document.getElementById('skills-form-btn');
const skillFormButtonText = document.getElementById('skills-form-submit-btn-text');
const skillDocId = document.getElementById('skill-doc-id');
const buttons = document.querySelectorAll('button');
const skillsAlert = document.getElementById('skills-alert');


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
     * Upon click of ADMIN nav dropdown element,
     * toggle vibility and chevron animation
     */
    function toggleDropdown() {
        this.nextElementSibling.classList.toggle('admin-nav-dropdown-animation');
        this.children[0].classList.toggle('admin-nav-dropdown-trigger-selected');
        this.querySelector('.admin-nav-chevron').classList.toggle('admin-nav-chevron-flip');
    }

    function toggleSideNav() {
        this.classList.toggle('menu-toggle-icon-expand');
        sideNav.classList.toggle('nav-slide');
    }

    function reloadTargetURL(redirect) {
        window.location.replace(`${window.origin}/admin/${redirect}`);
    }

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

    function resetSkill() {
        changeFormButton('add', 'skills');
        skillName.value = null;
        skillLevel.value = null;
        skillName.classList.remove('valid');
        skillLevel.classList.remove('valid');

        Array.from(skillFormLabels).forEach(label => {
            label.classList.remove('active');
        });
    }

    function changeFormButton(type, formTarget) {
        let formTargetButton;
        switch (formTarget) {
            case 'skills': 
                formTarget = skillFormButton;
                formTargetButton = skillFormButtonText;
                break;
            default: formTarget = formTarget; 
        }

        if (type === 'add') {
            formTarget.classList.remove('skills-form-btn-update');
            formTarget.classList.add('skills-form-btn-add');
            formTargetButton.innerText = 'Add';
        } else if (type === 'update') {
            formTarget.classList.remove('skills-form-btn-add');
            formTarget.classList.add('skills-form-btn-update');
            formTargetButton.innerText = 'Update';
        }
    }

    function addSkillData() {
        const skill_entry = {
            skill_name: skillName.value,
            skill_level: skillLevel.value
        };

        fetch(`${window.origin}/admin/skills/add`, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(skill_entry),
            cache: 'no-cache',
            headers: new Headers({
                'content-type': 'application/json'
            })
        }).then(response => {
            if (response.status !== 200) {
                console.log(`Response status not 200: ${response.status}`);
                flashAlert(skillsAlert, 'failure', 'skill', 'added', 'skills');
                return;
            }
            response.json().then(data => {
                console.log(data);
                flashAlert(skillsAlert, 'success', 'skill', 'added', 'skills');
            });
        });   
    }

    function fetchSkillData() {
        dataTarget = this.getAttribute('data-id');
        skillDocId.setAttribute('data-id', dataTarget);
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

    function updateSkillData() {
        dataTarget = skillDocId.getAttribute('data-id');
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

    function deleteDocument(type, event) {
        const dataTarget = event.target.getAttribute('data-id');

        fetch(`${window.origin}/admin/${type}/delete/${dataTarget}`, {
            method: 'DELETE',
            credentials: 'include',
            headers: new Headers()
        })
        .then(response => {
            if (response.status !== 200) {
                console.log(`Response status not 200: ${response.status}`);
                flashAlert(skillsAlert, 'failure', 'skill', 'deleted', 'skills');
                return;
            }

            response.json().then(data => {
                console.log(data);
                flashAlert(skillsAlert, 'success', 'skill', 'deleted', 'skills');
            });
        });
    }

    function handleElementsNotLoadedGlobally(event) {
        event = event || window.event;
        event.target = event.target || event.srcElement;

        let element = event.target;
        
        while (element) {
            if (/add-btn/.test(element.className)) {
                changeFormButton('add', 'skills');
                resetSkill();
                setTimeout(function() {
                    skillModalInstance.open();               
                }, 400);
                break; 
            } else if (/skills-form-btn-add/.test(element.className)) {
                addSkillData();
                break; 
            } else if (/skills-form-btn-update/.test(element.className)) {
                updateSkillData();
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
            deleteDocument('skills', event);
        });
    });

    Array.from(buttons).forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
        });
    });

    toggleMenuIcon.addEventListener('click', toggleSideNav);

    document.addEventListener( "click", handleElementsNotLoadedGlobally);
    /* END OF EVENT LISTENERS */

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
    /* END OF INITIALIZE MATERIALIZE COMPONENTS */

    animateCursor();
    randomizeInitialSkillBarHeight();
    animateSkillBars();
});