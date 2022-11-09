from turncoats.bag import Bag
from turncoats.stone import Stone

def test_init():
    bag = Bag()

    assert bag.stones.count(Stone.RED) == 19
    assert bag.stones.count(Stone.BLUE) == 19
    assert bag.stones.count(Stone.BLACK) == 19