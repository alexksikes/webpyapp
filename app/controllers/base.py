import web
import config

from config import view

class index:    
    def GET(self):
        i = web.input(q='')

        return view.layout(view.index(i.q))
