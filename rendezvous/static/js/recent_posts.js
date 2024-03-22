$(document).ready(function() {
    $.ajax({
        url: '/api/recent-posts/',
        dataType: 'json',
        success: function(data) {
            data.forEach(function(post) {
                // Access the 'fields' property of each post object
                var fields = post.fields;
                var pictureUrl = fields.Picture ? '/media/' + fields.Picture : '/media/default_pic.jpeg'; // Adjust the default image path
                var postHtml = '<div class="discover-feed-card">' +
                                '<img src="' + pictureUrl + '" class="discover-feed-img" alt="Post Image">' +
                                '<div>' +
                                    '<h5 class="discover-feed-title">' + fields.Title + '</h5>' + 
                                    '<div class="discover-feed-separator"></div>' +
                                    '<p class="discover-feed-text">' + fields.Text.substring(0, 100) + '...</p>' +
                                '</div>' +
                               '</div>';

                // Append the new post HTML to the container
                $('#discover-feed-container').append(postHtml);
            });
        }
    });
});