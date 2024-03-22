$(document).ready(function() {
    $.ajax({
        url: '/api/featured-posts/',
        dataType: 'json',
        success: function(data) {
            data.forEach(function(post) {
                // Access the 'fields' property of each post object
                var fields = post.fields;
                var pictureUrl = fields.Picture ? '/media/' + fields.Picture : '/media/default_pic.jpeg'; // Adjust the default image path
                var postHtml = '<div class="carousel-item">' +
                                '<img src="' + pictureUrl + '" class="d-block w-100" alt="Post Image"/>' +
                                    '<div class="carousel-caption d-none d-md-block">' +
                                        '<div class="caption-background">' +
                                        '<h5>'+ fields.Title +'</h5>' + 
                                        '<p>' + fields.Text.substring(0, 100) + '...</p>' +
                                        '</div>' +
                                    '</div>' +
                                '</div>';

                // Append the new post HTML to the container
                $('#featured_posts_container').append(postHtml);
            });
        }
    });
});


