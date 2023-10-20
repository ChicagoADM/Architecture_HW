from HW_02.ItemFabric import ItemFabric
from HW_02.CupperReward import CupperReward


class CupperGenerator(ItemFabric):

    def create_item(self):
        print("Создали сундук (медь)")
        return CupperReward()
