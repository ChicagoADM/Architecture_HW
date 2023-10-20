import random

from HW_02.GemGenerator import GemGenerator
from HW_02.GoldGenerator import GoldGenerator
from HW_02.SilverGenerator import SilverGenerator
from HW_02.CupperGenerator import CupperGenerator

if __name__ == '__main__':
    fabricList = [GemGenerator(), GoldGenerator(), SilverGenerator(), CupperGenerator()]
    for i in range(20):
        rnd = random.choice(fabricList).create_item().open()