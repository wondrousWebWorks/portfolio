/*jshint esversion: 6 */
const projectAddModalTrigger = document.querySelector('#add-project-btn');
const projectUpdateButtons = document.querySelectorAll('.update-project-btn');
const projectDeleteButtons = document.querySelectorAll('.delete-project-btn');
const projectModal = document.querySelector('#projects-form-modal');
const projectForm = document.querySelector('#projects-form');
const projectFormLabels = document.querySelectorAll('.projects-form-label');
const projectFormSubmitButton = document.querySelector('#projects-form-btn');
const projectFormSubmitButtonText = document.querySelector('#projects-form-submit-btn-text');
const projectFormDocId = document.querySelector('#project-form-doc-id');
const projectsAlert = document.querySelector('#projects-alert');
const projectFormInputs = document.querySelectorAll('#projects-form input');
const projectName = document.querySelector('#project-name');
const projectImgUrl = document.querySelector('#project-img-url');
const projectGithubUrl = document.querySelector('#project-github-url');
const projectDeployedUrl = document.querySelector('#project-deployed-url');
const projectTechnologies = document.querySelector('#project-technologies');
const projectTechnologiesSelectOptions = document.querySelectorAll('.project-technology');
const projectDescriptionParagraphs = document.querySelectorAll('.project-description-paragraph');
const projectModalInstance = M.Modal.init(projectModal);

document.addEventListener('DOMContentLoaded', function () {
    projectAddModalTrigger.addEventListener('click', () => {
        toggleAddModal('projects');
    });

    projectFormSubmitButton.addEventListener('click', function() {
        addOrUpdateFormData(this);
    });

    Array.from(projectUpdateButtons).forEach(updateButton => {
        updateButton.addEventListener('click', getProjectData);
    });

    Array.from(projectDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function() {
            deleteDocument(this);
        });
    });
});