document.addEventListener('DOMContentLoaded', function() {
    var map = L.map('mapid', {
        minZoom: 2,
        maxZoom: 4
    }).setView([51.505, -0.09], 2);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Your GeoJSON data path
    fetch('static/js/Globe.json')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            var geojson = L.geoJSON(data, {
                style: function (feature) {
                    return {color: feature.properties.color};
                },
                onEachFeature: function (feature, layer) {
                    layer.on('mouseover', function () {
                        // Change the style to the highlighted state on mouseover
                        layer.setStyle({
                            weight: 3,
                            color: '#666',
                            fillOpacity: 0.7
                        });
                    });
                    layer.on('mouseout', function () {
                        // Reset the layer style to its default state on mouseout
                        geojson.resetStyle(layer);
                    });
                    layer.on('click', function () {
                        // Alert with the country name
                        alert('Clicked on country: ' + feature.properties.name);
                    });
                }
            }).addTo(map);
        });
});