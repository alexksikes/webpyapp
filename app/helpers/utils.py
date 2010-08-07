import config
import md5

def dict_remove(d, *keys):
    for k in keys:
        if d.has_key(k):
            del d[k]
    
def make_unique_md5():
    return md5.md5(time.ctime() + config.encryption_key).hexdigest()

def get_ip():
    return web.ctx.get('ip', '000.000.000.000')

def store(tablename, _test=False, **values):
    try:
        db.insert(tablename, **values)
    except:
        db.update(tablename, **values)
