(function() {


function initApplication(options) {
  // Leaflet map.
  var map = L.map(options.$el.get(0)).setView([48.390834, -4.485556], 12);
  var gisDataLayer = L.tileLayer(options.tileLayer.url, {
    attribution: options.tileLayer.attribution
  });
  var osmLayer = L.tileLayer('//tile-{s}.easter-eggs.com/france/{z}/{x}/{y}.png', {
    attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a>, ' +
      '<a href="http://www.easter-eggs.com">Easter-eggs</a>'
  });
  L.control.layers(
    {'OpenStreetMap': osmLayer},
    {'GIS data': gisDataLayer},
    {collapsed: false}
  ).addTo(map);
  gisDataLayer.addTo(map);
  osmLayer.addTo(map);
}


// Exports

window.initApplication = initApplication;


}).call(this);
