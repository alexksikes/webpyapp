#!/usr/bin/env python

import web
import config
import app.controllers

urls = (
    '/',                                         'app.controllers.base.index',
    
    # in production should be overriden by lighttpd
    '/(?:img|js|css)/.*',                        'app.controllers.public.public',
)

app = web.application(urls, globals())

if config.email_errors:
    setup_error_emaling(app)

if __name__ == "__main__":
    app.run()

def setup_error_emaling(app):
    app.internalerror = web.emailerrors(config.email_errors, app.internalerror) # was web.webapi._InternalError
    
def setup_sessions(app):
    from app.helpers import session
    session.add_sessions_to_app(app)