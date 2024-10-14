from urllib.parse import quote as url_quote
import werkzeug.urls

# Monkey-patch werkzeug's url_quote
werkzeug.urls.url_quote = url_quote

from sgd import app
