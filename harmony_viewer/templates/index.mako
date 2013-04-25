## -*- coding: utf-8 -*-


<%inherit file="/site.mako"/>


<%block name="container_content">
<div class="map"></div>
</%block>


<%block name="page_scripts">
<script src="${ctx.conf['cdn.leaflet.js']}"></script>
<script src="/application.js"></script>
<script>
$(function() {
  initApplication({
    $el: $('.map'),
    tileLayer: {
      attribution: 'TODO Brest métropole',
      url: '//localhost:8000/{z}/{x}/{y}.png'
    }
  });
});
</script>
</%block>


<%block name="page_stylesheets">
<link href="${ctx.conf['cdn.leaflet.css']}" rel="stylesheet">
<!--[if lte IE 8]>
    <link href="ctx.conf['cdn.leaflet.ie.css']" rel="stylesheet">
<![endif]-->
<link href="/style.css" rel="stylesheet">
</%block>
