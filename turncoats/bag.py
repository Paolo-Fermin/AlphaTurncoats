from turncoats.stone import Stone
from typing import List, Optional
import random

class Bag:
    """The bag stores all the stones in a list. """
    
    def __init__(self):
        """Initialize the bag with 19 of each color. There are 21 of each color total, but each game starts
        with two of each color already on the board
        """
        self.stones: List[Stone] = [Stone.BLACK] * 19 + [Stone.RED] * 19 + [Stone.BLUE] * 19

    def get(self, color: Optional[Stone] = None) -> Stone:
        """Get a stone from the bag. By default it is a random stone

        Args:
            color (Optional[Stone], optional): Return a specific color from the bag, if it exists. 
                Might be useful for debugging purposes. Defaults to None.

        Raises:
            ValueError: A color was requested but no more stones of this color are left in the bag

        Returns:
            Stone: The stone returned from the bag
        """
        if color is None:
            return random.choice(self.stones)
        try:
            idx = self.stones.index(color)
            return self.stones[idx]
        except ValueError as e:
            raise ValueError("There is no stone of this color left in the bag!") from e

    def add(self, color: Stone):
        """Add stone to the bag

        Args:
            color (Stone): The color of the stone being added

        Raises: 
            AssertionError: There are too many stones of that color already in the bag
        """
        assert self.stones.count(Stone.RED) < 21, "Too many red stones in the bag!"
        assert self.stones.count(Stone.BLUE) < 21, "Too many blue stones in the bag!"
        assert self.stones.count(Stone.BLACK) < 21, "Too many black stones in the bag!"
        
        self.stones.append(color)