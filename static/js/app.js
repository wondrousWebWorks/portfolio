const cursorRectangle = document.querySelectorAll(".cursor-rectangle");
const skillBarsWrappers = document.querySelectorAll(".skill-bars-wrapper");
const skillBars = document.querySelectorAll(".skill-bar");
const projects = document.querySelectorAll(".project-col");

document.addEventListener('DOMContentLoaded', function () {

    const navElems = document.querySelectorAll('.sidenav');
    const navInstances = M.Sidenav.init(navElems, {});

    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

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

    function scaleProject() {
        projects.forEach(project => {
            project.classList.add('project-scale-smaller-and-opage');
        });
        this.classList.remove('project-scale-smaller-and-opage');
        this.classList.add('project-scale-bigger');
    }

    function shrinkProjects() {
        projects.forEach(project => {
            project.classList.remove('project-scale-smaller-and-opage');
            project.classList.remove('project-scale-bigger');
        });
    }

    Array.from(projects).forEach(project => {
        project.addEventListener("mouseover", scaleProject);
        project.addEventListener("mouseout", shrinkProjects);
      });

    animateCursor();
    randomizeInitialSkillBarHeight();
    animateSkillBars();
});