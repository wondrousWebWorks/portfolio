const cursorRectangle = document.querySelectorAll(".cursor-rectangle");
const skillBarInfoElements = document.querySelectorAll(".skill-info-bars");
const skillBars = document.querySelectorAll(".skill-bar");

document.addEventListener('DOMContentLoaded', function () {

    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});

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
        skillBarInfoElements.forEach(skillBarInfoElement => {
            const skillLevel = parseInt(skillBarInfoElement.getAttribute('data-skill-level'));
            const skillBarInfoElementChildren = skillBarInfoElement.children;

            for (let i = 0; i < skillBarInfoElementChildren.length; i++) {
                if (skillLevel == 0) {
                    continue;
                } else {
                    const skillBarRandomHeight = Math.floor(Math.random() * (skillLevel - 3) + 3);
                    skillBarInfoElementChildren[i].style.height = `${skillBarRandomHeight}%`;
                    const skillBarRisingOrFalling = Math.random();
                    if (skillBarRisingOrFalling < 0.5) {
                        skillBarInfoElementChildren[i].setAttribute('data-rising-falling', 'falling');
                    } else {
                        skillBarInfoElementChildren[i].setAttribute('data-rising-falling', 'rising');
                    }
                }
            }
        });
    }

    function animateSkillBars() {
        let skillBarRising = true;
        setInterval(function () {
            skillBarInfoElements.forEach(skillBarInfoElement => {
                
                const skillLevel = parseInt(skillBarInfoElement.getAttribute('data-skill-level'));
                const skillBarInfoElementChildren = skillBarInfoElement.children;

                for (let i = 0; i < skillBarInfoElementChildren.length; i++) {
                    let currentSkillBarHeight = parseInt(skillBarInfoElementChildren[i].style.height.replace("%", ""));
                    let risingOrFalling = skillBarInfoElementChildren[i].getAttribute('data-rising-falling');
                    
                    if (risingOrFalling == 'rising') {
                        if (currentSkillBarHeight + 3 <= skillLevel) {
                            skillBarInfoElementChildren[i].style.height = `${currentSkillBarHeight + 3}%`;
                        } else {
                            skillBarInfoElementChildren[i].setAttribute('data-rising-falling', 'falling');
                        }
                    } else if (risingOrFalling == 'falling') {
                        if (currentSkillBarHeight - 3 >= 0) {
                            skillBarInfoElementChildren[i].style.height = `${currentSkillBarHeight - 3}%`;
                        } else {
                            skillBarInfoElementChildren[i].setAttribute('data-rising-falling', 'rising');
                        }
                    }
                }
            });
        }, 60);
    }

    animateCursor();
    randomizeInitialSkillBarHeight();
    animateSkillBars();
});