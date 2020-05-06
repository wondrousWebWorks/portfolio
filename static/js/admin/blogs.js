/*jshint esversion: 6 */
const blogAddModalTrigger = document.querySelector('#add-blog-post-btn');
const blogPostUpdateButtons = document.querySelectorAll('.update-blog-post-btn');
const blogPostDeleteButtons = document.querySelectorAll('.delete-blog-post-btn');
const blogModal = document.querySelector('#blogs-form-modal');
const blogForm = document.querySelector('#blogs-form');
const blogFormLabels = document.querySelectorAll('.blogs-form-label');
const blogFormSubmitButton = document.querySelector('#blogs-form-submit-btn');
const blogFormSubmitButtonText = document.querySelector('#blogs-form-submit-btn-text');
const blogFormDocId = document.querySelector('#blogs-form-doc-id');
const blogAlert = document.querySelector('#blogs-alert');
const blogFormInputs = document.querySelectorAll('#blogs-form input');
const blogTitle = document.querySelector('#blog-title');
const blogImgUrl = document.querySelector('#blog-img-url');
const blogSummary = document.querySelector('#blog-summary');
const blogDate = document.querySelector('#blog-date');
const blogParagraphs = document.querySelectorAll('.blog-paragraph');
const blogModalInstance = M.Modal.init(blogModal);

document.addEventListener('DOMContentLoaded', function () {
    blogAddModalTrigger.addEventListener('click', () => {
        toggleAddModal('blogs');
    });

    blogFormSubmitButton.addEventListener('click', function() {
        addOrUpdateFormData(this);
    });

    Array.from(blogPostUpdateButtons).forEach(updateButton => {
        updateButton.addEventListener('click', getBlogEntryData);
    });

    Array.from(blogPostDeleteButtons).forEach(deleteButton => {
        deleteButton.addEventListener('click', function() {
            deleteDocument(this);
        });
    });
});