import os
import sys
from twisted.application import service, internet
from twisted.internet import reactor

from twisted.web import server, resource, wsgi, static
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.web.websockets import WebSocketsResource, lookupProtocolForFactory

from twisted_share.factories import ShareFactory
from twisted_share.resources import HttpShare, StaticFileScanner
from twisted_share.wsgi import WsgiRoot
from twisted.python.threadpool import ThreadPool

from django.core.handlers.wsgi import WSGIHandler


# Environment setup for your Django project files:
#sys.path.append("cib_simulator")
sys.path.append("gameMT")
os.environ['DJANGO_SETTINGS_MODULE'] = 'gameMT.settings'

shared_messages = {}

resource = HttpShare(shared_messages)
factory = Site(resource)
ws_resource = WebSocketsResource(lookupProtocolForFactory(resource.wsFactory))

#Create a resource which will correspond to the root of the URL hierarchy: all URLs are children of this resource.
root = Resource()
root.putChild("",resource) #the http protocol is up at /
root.putChild("ws",ws_resource) #the websocket protocol is at /ws

# Twisted Application Framework setup:
application = service.Application("shareserver")

#This is the port for pass messages
internet.TCPServer(1035, Site(root)).setServiceParent(application)

#serving django over wsgi
# Create and start a thread pool,
wsgiThreadPool = ThreadPool()
wsgiThreadPool.start()

django_application = WSGIHandler()
django_resource = wsgi.WSGIResource(reactor, wsgiThreadPool, django_application)

#Serve it up:
#staticsrc = static.File(os.path.join(os.path.abspath("."), "cib_simulator/static"))
django_root = WsgiRoot(django_resource)
project_dir = os.getcwd()
#django_root.putChild('static', StaticFileScanner("CIB-system-master/cib_simulator/static"))
#staticsrc = static.File("CIB-system-master/cib_simulator/static")
#root.putChild("static", staticsrc)
#django_root.putChild('static', staticsrc)
django_root.putChild('static', StaticFileScanner(project_dir + "/gameMT/static"))

#Replace port 8000 with 80,try,failed,still listen to 8000
internet.TCPServer(8000, Site(django_root)).setServiceParent(application)
