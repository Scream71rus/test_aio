
import handlers.ws
import handlers.main
import handlers.auth

urls = []
urls.extend(handlers.ws.urls)
urls.extend(handlers.main.urls)
urls.extend(handlers.auth.urls)

