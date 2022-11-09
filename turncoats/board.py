"""The Turncoats board can be represented as a graph where each node contains information about what stones are within it."""

from dataclasses import dataclass
from turncoats.stone import Stone
from typing import List, Dict
from bag import Bag

@dataclass
class Tile:
    adj: List[int]
    stones: List[Stone]


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

        # do not populate these tiles with any more stones
        home_tiles: List = [2, 3, 9]

        # randomly draw pairs of stones and place them in every other area
        for id, tile in self.graph.items():
            if id not in home_tiles:
                tile.stones.extend([bag.get(), bag.get()])

        
