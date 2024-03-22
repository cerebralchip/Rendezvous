// Write a function to fetch all comments for the current post (url looks like {domain}/post/post_id) from the database, and append html to div with id="comments-container"
function fetchAndAppendComments() {
    const postId = getPostIdFromUrl(); // Assuming you have a function to extract the post id from the URL
    const url = `https://example.com/post/${postId}/comments`; // Replace "example.com" with your actual domain

    fetch(url)
        .then(response => response.json())
        .then(comments => {
            const commentsContainer = document.getElementById("comments-container");
            comments.forEach(comment => {
                const commentHtml = createCommentHtml(comment); // Assuming you have a function to create HTML for a comment
                commentsContainer.innerHTML += commentHtml;
            });
        })
        .catch(error => {
            console.error("Error fetching comments:", error);
        });
}

function getPostIdFromUrl() {
    // Implement the logic to extract the post id from the URL
    
}

function createCommentHtml(comment) {
    // Implement the logic to create HTML for a comment
}