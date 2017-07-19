# coding=utf-8
__author__ = 'lxn3032'


from poco.rpc import RpcInterface

from hrpc.client import RpcClient
from hrpc.transport.http import HttpTransport


__all__ = ['AndroidRpcClient']


class Client(RpcClient):
    def __init__(self, endpoint):
        self.endpoint = endpoint
        super(Client, self).__init__(HttpTransport)

    def initialize_transport(self):
        return HttpTransport(self.endpoint, self)


class AndroidRpcClient(RpcInterface):
    def __init__(self, endpoint):
        super(AndroidRpcClient, self).__init__()
        self.endpoint = endpoint
        self.client = Client(endpoint)
        self.remote_poco = self.client.remote('poco-uiautomation-framework')
        self.inputer = self.remote_poco.inputer

    # screen interface
    def get_screen_size(self):
        return self.remote_poco.get_screen_size()

    # node/hierarchy interface
    def getattr(self, nodes, name):
        return self.remote_poco.attributor.getAttr(nodes, name)

    def setattr(self, nodes, name, val):
        self.remote_poco.attributor.setAttr(nodes, name, val)

    def select(self, query, multiple=False):
        return self.remote_poco.selector.select(query, multiple)

    def dump(self):
        return self.remote_poco.dumper.dumpHierarchy()

    # input interface
    def click(self, x, y):
        return self.inputer.click(int(x), int(y))

    def long_click(self, x, y, duration=3):
        # 目标设备duration以毫秒为单位
        return self.inputer.longClick(int(x), int(y), int(duration * 1000))

    def swipe(self, x1, y1, x2, y2, duration):
        return self.inputer.swipe(int(x1), int(y1), int(x2), int(y2), int(duration * 1000))

    def get_input_panel_size(self):
        return self.inputer.getPortSize()
