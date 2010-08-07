import web
import app.helpers.templating

# connect to database
db = web.database(dbn='mysql', db='', user='', passwd='')

# in development debug error messages and reloader
web.config.debug = True

# in develpment template caching is set to false
cache = False

# the domain where to get the forms from
site_domain = 'your website domain'

# set global base template
view = web.template.render('app/views', cache=cache)

# show output of mysql statements
db.printing = True

# used as a salt
encryption_key = 'a random string'

# if specified email errors to this address
email_errors = ''