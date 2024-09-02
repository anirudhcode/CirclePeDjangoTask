wsgi_app = "nebulon.wsgi:application"
loglevel = "info"
workers = 3
bind = "0.0.0.0:8000"
reload = True
accesslog = errorlog = "/var/log/gunicorn/access.log"
capture_output = True
pidfile = "/var/run/gunicorn.pid"

daemon = True
