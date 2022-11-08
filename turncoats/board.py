"""The Turncoats board can be represented as a graph where each node contains information about what stones are within it."""

from dataclasses import dataclass
from globals import Stone
from typing import List, Dict, Optional, Tuple
import random

@dataclass
class Tile:
    adj: List[int]
    stones: List[Stone]

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

class Board:

    def __init__(self, bag: Bag):
        """Encode the board as an adjacency list of tiles"""
        self.graph: Dict[int, List[List[int], Tile]] = {
            0: Tile([1, 2],[]), 
            1: Tile([0, 3, 4], []), 
            2: Tile([0, 4], [Stone.BLACK, Stone.BLACK]),
            3: Tile([1, 5], [Stone.RED, Stone.RED]),
            4: Tile([0, 1, 2, 6], []),
            5: Tile([3, 7, 8], []),
            6: Tile([4, 7, 9], []),
            7: Tile([5, 6, 8, 9], []),
            8: Tile([5, 7, 10], []),
            9: Tile([6, 7, 10], [Stone.BLUE, Stone.BLUE]),
            10: Tile([7, 8, 9], []),
            
            # note that 11 (axe) and 12 (flag) are essentially tiles without any connected nodes
            11: Tile([], []),
            12: Tile([], []),
        }

        
