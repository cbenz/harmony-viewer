# -*- coding: utf-8 -*-


"""Middleware initialization"""


import logging
import sys

from weberror.errormiddleware import ErrorMiddleware
from paste.cascade import Cascade
from paste.urlparser import StaticURLParser

from . import configuration, context, controllers, templates


def make_app(global_conf, **app_conf):
    """Create a WSGI application and return it

    ``global_conf``
        The inherited configuration for this application. Normally from
        the [DEFAULT] section of the Paste ini file.

    ``app_conf``
        The application's local configuration. Normally specified in
        the [app:<name>] section of the Paste ini file (where <name>
        defaults to main).
    """
    app_ctx = context.Context()
    app_ctx.conf = configuration.load_configuration(global_conf, app_conf)
    app_ctx.templates = templates.load_templates(app_ctx)
    logging.basicConfig(level=app_ctx.conf['log_level'], stream=sys.stdout)
    app = controllers.make_router()
    app = context.make_add_context_to_request(app, app_ctx)
    if not app_ctx.conf['debug']:
        app = ErrorMiddleware(
            app,
            error_email=app_ctx.conf['email_to'],
            error_log=app_ctx.conf.get('error_log', None),
            error_message=app_ctx.conf.get('error_message', 'An internal server error occurred'),
            error_subject_prefix=app_ctx.conf.get('error_subject_prefix', 'Web application error: '),
            from_address=app_ctx.conf['from_address'],
            smtp_server=app_ctx.conf.get('smtp_server', 'localhost'),
        )
    if app_ctx.conf['static_files']:
        # Serve static files.
        app = Cascade([StaticURLParser(app_ctx.conf['static_files_dir']), app])
    app.ctx = app_ctx
    return app
