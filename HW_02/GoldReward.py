from HW_02.IGameItem import IGameItem

class GoldReward(IGameItem):
    def open(self):
        print("Открыли сундук с золотом")