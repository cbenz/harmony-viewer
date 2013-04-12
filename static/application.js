function initApplication() {
  // Leaflet map.
  var map = L.map('map').setView([48.390834, -4.485556], 12);
  var gisDataLayer = L.tileLayer('//localhost:8000/{z}/{x}/{y}.png', {
    attribution: 'TODO'
    });
  var osmLayer = L.tileLayer('//tile-{s}.easter-eggs.com/france/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    });
  L.control.layers(
    {'OpenStreetMap': osmLayer},
    {'GIS data': gisDataLayer},
    {collapsed: false}
    ).addTo(map);
  gisDataLayer.addTo(map);
  osmLayer.addTo(map);

  // Dat GUI controller.
  var gui = new dat.GUI();
  var opacityController = gui.add(gisDataLayer.options, 'opacity', 0, 1);
  opacityController.onChange(function(value) {
    gisDataLayer.setOpacity(value);
  });
}
