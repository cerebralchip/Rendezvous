$(document).ready(function() {
    $.ajax({
        url: '/api/recent-posts/',
        dataType: 'json',
        success: function(data) {
            data.forEach(function(post) {
                // Access the 'fields' property of each post object
                var fields = post.fields;
                var pictureUrl = fields.Picture ? '/media/' + fields.Picture : '/media/default_pic.jpeg'; // Adjust the default image path
                // Format the published date in a more readable format if necessary
                var publishedDate = new Date(fields.published_date).toLocaleDateString("en-GB", {
                    year: 'numeric', month: 'long', day: 'numeric'
                });
                var postHtml = '<div class="col-md-4">' +
                                    '<div class="card bg-dark text-white">' +
                                    '<img src="'+ pictureUrl +'" class="card-img" alt="Post Image" />' +
                                        '<div class="card-img-overlay d-flex flex-column justify-content-end">' +
                                            '<h5 class="card-title">'+ fields.Title +'</h5>' + 
                                            '<p class="card-text">' + fields.Text.substring(0, 100) + '...</p>' +
                                            '<hr class="card-inside-separator" />' +
                                            '<p class="card-meta"> <small>'+ fields.username +'</small><br/><small>'+ publishedDate +'</small> </p>'+
                                        '</div>' +
                                    '</div>' +
                               '</div>';

                // Append the new post HTML to the container
                $('#recent-posts-container').append(postHtml);
            });
        }
    });
});