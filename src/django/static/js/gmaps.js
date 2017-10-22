var locations = [
  //['Bondi Beach', -33.890542, 151.274856, 4],
  ['Coogee Beach', -33.923036, 151.259052, 5],
  ['Cronulla Beach', -34.028249, 151.157507, 3],
  ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
  ['Maroubra Beach', -33.950198, 151.259302, 1]
];

var map = new google.maps.Map(document.getElementById('map'), {
  zoom: 10,
  center: new google.maps.LatLng((43.076149+43.168864)/2, (-80.125481 + -79.930081)/2),
  mapTypeId: google.maps.MapTypeId.SATELLITE
});
map.fitBounds(new google.maps.LatLngBounds(
  new google.maps.LatLng(43.076149, -80.125481),
  new google.maps.LatLng(43.168864, -79.930081)
));

var infowindow = new google.maps.InfoWindow();

var marker, i;

var ok_img = {
  url: '{% static "img/ok_medium.png" %}',
  size: new google.maps.Size(32, 32),
  origin: new google.maps.Point(0, 0),
  anchor: new google.maps.Point(16, 16),
}
  var image = {
url: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png',
// This marker is 20 pixels wide by 32 pixels high.
size: new google.maps.Size(20, 32),
// The origin for this image is (0, 0).
origin: new google.maps.Point(0, 0),
// The anchor for this image is the base of the flagpole at (0, 32).
anchor: new google.maps.Point(0, 32)
};

window.addp = function() {
marker = new google.maps.Marker({
  position: new google.maps.LatLng(-33.890542, 151.274856),
  map: map,
  icon: ok_img,
  animation: google.maps.Animation.DROP,
});
}

for (i = 0; i < locations.length; i++) {
  marker = new google.maps.Marker({
    position: new google.maps.LatLng(locations[i][1], locations[i][2]),
    map: map,
    icon: ok_img,
  });

  google.maps.event.addListener(marker, 'click', (function(marker, i) {
    return function() {
      infowindow.setContent(locations[i][0]);
      infowindow.open(map, marker);
    }
  })(marker, i));
}