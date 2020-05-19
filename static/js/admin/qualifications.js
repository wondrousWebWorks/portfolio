/*jshint esversion: 6 */
const qualificationAddModalTrigger = document.querySelector('#add-qualification-btn');
const qualificationUpdateButtons = document.querySelectorAll('.update-qualification-btn');
const qualificationDeleteButtons = document.querySelectorAll('.delete-qualification-btn');
const qualificationModal = document.querySelector('#qualifications-form-modal');
const qualificationForm = document.querySelector('#qualifications-form');
const qualificationFormLabels = document.querySelectorAll('.qualifications-form-label');
const qualificationFormSubmitButton = document.querySelector('#qualifications-form-submit-btn');
const qualificationFormSubmitButtonText = document.querySelector('#qualifications-form-submit-btn-text');
const qualificationFormDocId = document.querySelector('#qualification-form-doc-id');
const qualificationsAlert = document.querySelector('#qualifications-alert');
const qualificationFormInputs = document.querySelectorAll('#qualifications-form input');
const qualificationName = document.querySelector('#qualification-name');
const qualificationFrom = document.querySelector('#qualification-from');
const qualificationIssueDate = document.querySelector('#qualification-issue-date');
const qualificationViewUrl = document.querySelector('#qualification-view-url');
const qualificationInfoUrl = document.querySelector('#qualification-info-url');
const qualificationModalInstance = M.Modal.init(qualificationModal);

document.addEventListener('DOMContentLoaded', function () {
    qualificationAddModalTrigger.addEventListener('click', () => toggleAddModal('qualifications'));

    qualificationFormSubmitButton.addEventListener('click', () => addOrUpdateFormData(qualificationFormSubmitButton));

    Array.from(qualificationUpdateButtons).forEach(updateButton => {
        updateButton.addEventListener('click', () => getQualificationData(updateButton));
    });

    Array.from(qualificationDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', () => deleteDocument(deleteButton));
    });
});