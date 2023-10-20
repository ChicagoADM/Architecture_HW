from HW_02.ItemFabric import ItemFabric
from HW_02.SilverReward import SilverReward


class SilverGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (серебро)")
        return SilverReward()
