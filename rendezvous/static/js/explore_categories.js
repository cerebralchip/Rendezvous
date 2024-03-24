function explore_cards_search(query) {
    // This function is called on click by a div in index.html
    // make a get request to search ({% url 'search' %}) with query
    window.location.href=`/search?query=${query}`;
};