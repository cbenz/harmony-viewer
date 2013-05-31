## -*- coding: utf-8 -*-


<%!
import collections
%>


<%def name="topbar()">
<div class="navbar navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container">
      <a class="brand" href="/">${ctx.conf['app_name']}</a>
    </div>
  </div>
</div>
</%def>


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><%block name="title_content">${ctx.conf['app_name']}</%block></title>
    <%block name="stylesheets">
    <link rel="stylesheet" href="${ctx.conf['cdn.bootstrap.css']}">
    <%block name="page_stylesheets"/>
    <link rel="stylesheet" href="/style.css">
    </%block>
  </head>
  <body>
    <%self:topbar/>
    <div class="container content">
      <%block name="container_content"/>
    </div>
    <%block name="scripts">
    <!--[if lt IE 9]>
    <script src="${ctx.conf['cdn.html5shiv.js']}"></script>
    <![endif]-->
    <script src="${ctx.conf['cdn.jquery.js']}"></script>
    <script src="${ctx.conf['cdn.bootstrap.js']}"></script>
    <%block name="page_scripts"/>
    </%block>
  </body>
</html>
