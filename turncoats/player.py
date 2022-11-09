"""The player takes actions on the board"""
from typing import List
from turncoats.stone import Stone

class Player:

    def __init__(self, id: str, starting_hand: List[Stone]):
        """Each player must be initialized with a unique string and a list of 8 stones to start with

        Args:
            id (str): player id
        """
        self.id: str = id

        assert len(starting_hand) == 8, "Must provide 8 stones to start!"
        self.hand = starting_hand

