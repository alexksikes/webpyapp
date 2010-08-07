# Author: Alex Ksikes 

import os
import mimetypes
import web

class public:
    def GET(self): 
        public_dir = 'public'
        try:
            file_name = web.ctx.path.split('/')[-1]
            web.header('Content-type', mime_type(file_name))
            path = (public_dir + web.ctx.path).replace('..', '')
            
            return open(path, 'rb').read()
        except IOError:
            raise web.notfound()
            
def mime_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream' 
