from twisted.internet.protocol import Factory

from twisted_share.protocols import WebsocketShare


class ShareFactory(Factory):
    protocol = WebsocketShare
    clients = []
    messages = {}
