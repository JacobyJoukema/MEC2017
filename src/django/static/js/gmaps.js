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
  url: 'static/img/ok_medium.png',
  size: new google.maps.Size(32, 32),
  origin: new google.maps.Point(0, 0),
  anchor: new google.maps.Point(16, 16),
}

var bad_img = {
  url: 'static/img/bad_medium.png',
  size: new google.maps.Size(32, 32),
  origin: new google.maps.Point(0, 0),
  anchor: new google.maps.Point(16, 16),
}

window.addp = function() {
marker = new google.maps.Marker({
  position: new google.maps.LatLng(-33.890542, 151.274856),
  map: map,
  icon: ok_img,
  animation: google.maps.Animation.DROP,
});
}

var markers = {};
function get_data() {
    console.log('fetching')
    $.ajax('/api/points', {
        success: function(data) {
            console.log(data);
            roll_points(data);
        }
    })
}
function roll_points(data) {
    if (data.add) {
        for (var i=0; i<data.add.length; i++) {
            var am = data.add[i];
            var id = am.ID
            var lat = am.lat;
            var long = am.long;
            var type = Math.random()<=0.2 ? 0 : 1//am.type;
            var icon_img;
            if (type == 1) { icon_img = ok_img; }
            else { icon_img = bad_img; }
            markers[id] = new google.maps.Marker({
                position: new google.maps.LatLng(lat, long),
                map: map,
                icon: icon_img,
                //animation: google.maps.Animation.DROP,
            })
        }
    }
    if (data.remove) {
        for (var i=0; i<data.remove.length; i++) {
            var am = data.remove[i];
            var id = am.ID;
            if (markers[id]) {
                markers[id].setMap(null);
            }
        }
    }
}
setInterval(get_data, 1000);
//
//for (i = 0; i < locations.length; i++) {
//  marker = new google.maps.Marker({
//    position: new google.maps.LatLng(locations[i][1], locations[i][2]),
//    map: map,
//    icon: ok_img,
//  });
//
//  google.maps.event.addListener(marker, 'click', (function(marker, i) {
//    return function() {
//      infowindow.setContent(locations[i][0]);
//      infowindow.open(map, marker);
//    }
//  })(marker, i));
//}