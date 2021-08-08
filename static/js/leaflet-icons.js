/*******************************************
    Leaflet Icons for Color Filtering
    icons taken from repository 
    	https://github.com/pointhi/leaflet-color-markers
*******************************************/

var createIcon = L.Icon.extend({
    options: {
        shadowUrl: '/static/img/map/marker-shadow.png',
        
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    }
});

var blackIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-black.png'}),
	blueIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-blue.png'}),
	goldIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-gold.png'}),
	greenIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-green.png'}),
	grayIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-grey.png'}),
	orangeIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-orange.png'}),
	redIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-red.png'}),
	violetIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-violet.png'}),
	yellowIcon = new createIcon({iconUrl: '/static/img/map/marker-icon-yellow.png'});