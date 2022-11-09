import pytest

from turncoats.bag import Bag
from turncoats.stone import Stone

def test_init():
    bag = Bag()

    assert bag.stones.count(Stone.RED) == 19
    assert bag.stones.count(Stone.BLUE) == 19
    assert bag.stones.count(Stone.BLACK) == 19

    assert len(bag.stones) == 57

def test_get():
    """Test the random getter"""
    bag = Bag()

    stone = bag.get()

    assert isinstance(stone, Stone)

    assert len(bag.stones) == 56

    assert bag.stones.count(stone) == 18

@pytest.mark.parametrize("color", [Stone.BLACK, Stone.BLUE, Stone.RED])
def test_get_color(color):
    """Test getting each specific color stone from the bag"""
    bag = Bag()

    stone = bag.get(color)
    
    assert stone == color
    assert bag.stones.count(color) == 18

@pytest.mark.parametrize("color", [Stone.BLACK, Stone.BLUE, Stone.RED])
def test_add(color):
    """Test adding all colors to the bag"""
    
    bag = Bag()

    # override the bag stones to have only a few stones
    test_bag_contents = [Stone.BLACK] * 3 + [Stone.BLUE] * 3 + [Stone.RED] * 3

    bag.stones = test_bag_contents

    bag.add(color)

    assert len(bag.stones) == 10
    assert bag.stones.count(color) == 4

# @pytest.mark.parametrize("color", [Stone.BLACK, Stone.BLUE, Stone.RED])
# def test_add_overflow(color):
#     """Test that an error is thrown when too many stones are added to the bag"""

#     bag = Bag()

#     # need to add two more of each bag because the bag assumes that the game
#     # starts with two of each color already on the board
#     extra_stones = [Stone.BLACK] * 2 + [Stone.BLUE] * 2 + [Stone.RED] * 2
#     for stone in extra_stones:
#         bag.add(stone)

#     # now there are too many stones, adding any more should not be possible
#     with pytest.raises(RuntimeError, f"Too many {color} in the bag!"):
#         bag.add(color)