from abc import ABCMeta, abstractmethod
from HW_02.IGameItem import IGameItem

class ItemFabric():
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_item(self):
        pass