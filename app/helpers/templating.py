# Author: Alex Ksikes

import config
import datetime
import md5
import re
import urllib
import urlparse
import web

def public(f):
    '''Exposes a function in templates. A list of functions or variables can 
    also be supplied as dictionnary.'''
    if isinstance(f, dict):
        web.template.Template.globals.update(f)
    else:
        web.template.Template.globals[f.__name__] = f

public(dict(
    # from web.http
    changequery = web.changequery,
    urlencode = web.http.urlencode,
    url = web.url,
    
    # from web.utils
    utf8 = web.utf8,
    strips = web.strips, 
    rstrips = web.rstrips,
    lstrips = web.lstrips,
    group = web.group,
    listget = web.listget,
    intget = web.intget,
    datestr = web.datestr,
    numify = web.numify,
    denumify = web.denumify,
    commify = web.commify,
    nthstr = web.nthstr,
    cond = web.utils.cond,
    to36 = web.to36,
    safemarkdown = web.safemarkdown,
    
    # from web.net
    urlquote = web.urlquote,
    httpdate = web.httpdate,
    htmlquote = web.htmlquote,
    htmlunquote = web.htmlunquote,
    websafe = web.websafe,
    
    # more from webpy
    debug = web.debug,
    input = web.input,
    
    # common utilities
    int = int,
    str = str,
    list = list,
    set = set,
    dict = dict,
    min = min,
    max = max,
    range = range,
    len = len,
    repr = repr,
    zip = zip,
    isinstance = isinstance,
    enumerate = enumerate,
    hasattr = hasattr,
    
    # here put global variables
))

@public
def include(tpl, *args, **kwargs):
    from config import view
    return view.__getattr__(tpl)(*args, **kwargs)

@public
def homedomain():
    return web.ctx.get('homedomain', '')

@public
def domain():
    return '.'.join(homedomain().split('.')[:-3:-1][::-1])

@public
def query_param(name, default=None):
    i = web.input(_m='GET')
    return i.get(name, default)

@public
def link(path, text=None):
    return '<a href="%s">%s</a>' % (web.ctx.homepath + path, text or path)

@public
def how_long(d):
    return web.datestr(d, datetime.datetime.now())

@public
def url_encode2(inputs, clean=True, doseq=True, **kw):
    inputs = web.dictadd(inputs, kw)
    if clean is True:
        for q, v in inputs.items():
            if not v:
                del inputs[q]
            if isinstance(v, unicode):
                inputs[q] = v.encode('utf-8')
    return urllib.urlencode(inputs, doseq)
    
@public
def cut_length(s, max=40):
    if len(s) > max:
        s = s[0:max] + '...'
    return s

@public
def text2html(s):
    s = re.sub('\n', '<br />', s)
    s = re.sub('\t', 4*' ', s)
    return replace_links(s)

def get_nice_url(url):
    host, path = urlparse.urlparse(url)[1:3]
    if path == '/':
        path = ''
    return cut_length(host+path)
    
@public
def replace_links(s):
    return re.sub('(http://[^\s]+)', r'<a rel="nofollow" href="\1">' + get_nice_url(r'\1') + '</a>', s, re.I)

@public
def split(pattern, str):
    return re.split(pattern, str)

@public
def get_md5_url(url):
    if not url:
        return None
    path = md5.new(url).hexdigest()
    return path[0:2] + '/' + path

@public
def wrap_tag(tag, _list):
    return ('<%s>%s</%s>' % (tag, e, tag) for e in _list)

@public
def change_params(**kwargs):
    return re.sub('/.*?\?', '', web.changequery(**kwargs))

@public
def get_inputs(**kwargs):
    inputs = web.input(**kwargs)
    return dict((i, inputs.get(i, kwargs[i])) for i in kwargs)
