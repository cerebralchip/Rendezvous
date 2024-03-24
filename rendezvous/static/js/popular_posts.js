$(document).ready(function() {
    $.ajax({
        url: '/api/popular-posts/', // Adjust this URL to the one you've set up for popular posts
        dataType: 'json',
        success: function(data) {
            data.forEach(function(post) {
                var fields = post.fields;
                // Construct the URL for the post image
                var pictureUrl = fields.Picture ? '/media/' + fields.Picture : '/media/default_pic.jpeg'; // Adjust with your default image path
                // Format the published date in a more readable format if necessary
                var publishedDate = new Date(fields.published_date).toLocaleDateString("en-GB", {
                    year: 'numeric', month: 'long', day: 'numeric'
                });
                
                var postHtml = 
                    '<div class="col-md-4">' +
                        '<div class="card bg-dark text-white">' +
                        '<a href="/post/'+ post.pk +'">' +
                            '<img src="' + pictureUrl + '" class="card-img" alt="Post Image">' +
                            '<div class="card-img-overlay d-flex flex-column justify-content-end">' +
                                '<h5 class="card-title">' + fields.Title + '</h5>' + 
                                '<p class="card-text">' + fields.Text.substring(0, 100) + '...</p>' + 
                                '<hr class="card-inside-separator">' +
                                '<p class="card-meta">' +
                                    '<small>'+ fields.username +'</small><br />' +
                                    '<small>' + publishedDate + '</small><br />' +
                                    // Show fields.Upvotes and fields.Downvotes but formatted nicely
                                    '<small>Upvotes: ' + fields.Upvotes + '</small>' + ' | ' +
                                    '<small>Downvotes: ' + fields.Downvotes + '</small>' +
                                '</p>' +
                            '</div>' +
                        '</a>' +
                        '</div>' +
                    '</div>';

                // Append the constructed HTML to a container, e.g., one with class 'row', id 'popular-posts-container'
                $('#popular-posts-container').append(postHtml);});
        }
    });
});