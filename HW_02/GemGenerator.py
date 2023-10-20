from HW_02.ItemFabric import ItemFabric
from HW_02.GemReward import GemReward


class GemGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (др. камень)")
        return GemReward()
