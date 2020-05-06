/*jshint esversion: 6 */
const experienceAddModalTrigger = document.querySelector('#add-experience-btn');
const experienceUpdateButtons = document.querySelectorAll('.update-experience-btn');
const experienceDeleteButtons = document.querySelectorAll('.delete-experience-btn');
const experienceModal = document.querySelector('#experience-form-modal');
const experienceForm = document.querySelector('#experience-form');
const experienceFormLabels = document.querySelectorAll('.experience-form-label');
const experienceFormSubmitButton = document.querySelector('#experience-form-submit-btn');
const experienceFormSubmitButtonText = document.querySelector('#experience-form-submit-btn-text');
const experienceFormDocId = document.querySelector('#experience-form-doc-id');
const experienceAlert = document.querySelector('#experience-alert');
const experienceFormInputs = document.querySelectorAll('#experience-form input');
const experienceJobTitle = document.querySelector('#job-title');
const experienceJobDates = document.querySelector('#job-dates');
const experienceModalInstance = M.Modal.init(experienceModal);

document.addEventListener('DOMContentLoaded', function () {
    experienceAddModalTrigger.addEventListener('click', () => {
        toggleAddModal('experience');
    });

    experienceFormSubmitButton.addEventListener('click', function() {
        addOrUpdateFormData(this);
    });

    Array.from(experienceUpdateButtons).forEach(updateButton => {
        updateButton.addEventListener('click', getExperienceData);
    });

    Array.from(experienceDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function() {
            deleteDocument(this);
        });
    });
});