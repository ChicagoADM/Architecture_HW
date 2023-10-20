from HW_02.ItemFabric import ItemFabric
from HW_02.GoldReward import GoldReward


class GoldGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (золото)")
        return GoldReward()
