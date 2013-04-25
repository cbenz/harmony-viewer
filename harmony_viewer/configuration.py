# -*- coding: utf-8 -*-


"""Paste INI configuration"""


import logging
import os
import urlparse

from biryani1 import strings
from biryani1.baseconv import (check, cleanup_line, default, function, guess_bool, noop, not_none, pipe, struct)


def load_configuration(global_conf, app_conf):
    """Build the application configuration dict."""
    app_dir = os.path.dirname(os.path.abspath(__file__))
    conf = {}
    conf.update(strings.deep_decode(global_conf))
    conf.update(strings.deep_decode(app_conf))
    conf.update(check(struct(
        {
            'app_conf': default(app_conf),
            'app_dir': default(app_dir),
            'app_name': default('Harmony Viewer'),
            'cache_dir': default(os.path.join(os.path.dirname(app_dir), 'cache')),
            'cdn.url': pipe(cleanup_line, not_none),
            'custom_templates_dir': default(None),
            'debug': pipe(guess_bool, default(False)),
            'global_conf': default(global_conf),
            'log_level': pipe(
                default('WARNING'),
                function(lambda log_level: getattr(logging, log_level.upper())),
                ),
            'package_name': default('harmony-viewer'),
            'projects_base_dir': pipe(cleanup_line, not_none),
            'static_files': pipe(guess_bool, default(False)),
            'static_files_dir': default(os.path.join(app_dir, 'static')),
        },
        default='drop',
        drop_none_values=False,
    ))(conf))

    # Assets
    conf.update(check(struct(
        {
            'cdn.bootstrap.css': default(
                urlparse.urljoin(conf['cdn.url'], '/bootstrap/2.2.2/css/bootstrap.min.css')
                ),
            'cdn.bootstrap.js': default(urlparse.urljoin(conf['cdn.url'], '/bootstrap/2.2.2/js/bootstrap.js')),
            'cdn.html5shiv.js': default(urlparse.urljoin(conf['cdn.url'], '/html5shiv/html5shiv.js')),
            'cdn.jquery.js': default(urlparse.urljoin(conf['cdn.url'], '/jquery/jquery-1.9.1.min.js')),
            'cdn.leaflet.css': default(urlparse.urljoin(conf['cdn.url'], '/leaflet/0.5.1/leaflet.css')),
            'cdn.leaflet.ie.css': default(urlparse.urljoin(conf['cdn.url'], '/leaflet/0.5.1/leaflet.ie.css')),
            'cdn.leaflet.js': default(urlparse.urljoin(conf['cdn.url'], '/leaflet/0.5.1/leaflet.js')),
            'cdn.plupload.js': default(urlparse.urljoin(conf['cdn.url'], '/plupload/plupload.full.js')),
            'cdn.underscore.js': default(urlparse.urljoin(conf['cdn.url'], '/underscore/underscore.js')),
        },
        default=noop,
    ))(conf))
    return conf
