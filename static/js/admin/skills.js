/*jshint esversion: 6 */
const skillAddModalTrigger = document.querySelector('#add-skill-btn');
const skillUpdateButtons = document.querySelectorAll('.update-skill-btn');
const skillDeleteButtons = document.querySelectorAll('.delete-skill-btn');
const skillModal = document.querySelector('#skills-form-modal');
const skillForm = document.querySelector('#skills-form');
const skillFormLabels = document.querySelectorAll('.skills-form-label');
const skillFormSubmitButton = document.querySelector('#skills-form-submit-btn');
const skillFormSubmitButtonText = document.querySelector('#skills-form-submit-btn-text');
const skillFormDocId = document.querySelector('#skill-form-doc-id');
const skillsAlert = document.querySelector('#skills-alert');
const skillFormInputs = document.querySelectorAll('#skills-form input');
const skillName = document.querySelector('#skill-name');
const skillLevel = document.querySelector('#skill-level');
const skillModalInstance = M.Modal.init(skillModal);

document.addEventListener('DOMContentLoaded', function () {
    skillAddModalTrigger.addEventListener('click', () => {
        toggleAddModal('skills');
    });

    skillFormSubmitButton.addEventListener('click', function() {
        addOrUpdateFormData(this);
    });

    Array.from(skillUpdateButtons).forEach(updateButton => {
        updateButton.addEventListener('click', getSkillData);
    });

    Array.from(skillDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function() {
            deleteDocument(this);
        });
    });
});