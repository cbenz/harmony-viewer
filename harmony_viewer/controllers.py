# -*- coding: utf-8 -*-


import os
from webob.dec import wsgify

from . import router, templates, wsgi_helpers


N_ = lambda message: message


@wsgify
def index(req):
    ctx = req.ctx
    conf = ctx.conf
    project_slug = req.urlvars['project_slug']
    project_dir_name = os.path.join(conf['projects_base_dir'], project_slug)
    if not os.path.isdir(project_dir_name):
        return wsgi_helpers.not_found(ctx, comment=N_(u'Invalid project'))
    return templates.render(
        req.ctx,
        '/index.mako',
        )


def make_router():
    """Return a WSGI application that dispatches requests to controllers """
    return router.make_router(
        ('GET', '^/(?P<project_slug>[a-z0-9-]+)/?', index),
        )
