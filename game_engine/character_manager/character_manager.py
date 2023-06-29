# This file contains the CharacterManager class, which is responsible for creating characters in the game.

from ai_models.bloom_model import generate_with_bloom
from ai_models.gpt2_model import generate_with_gpt2
from game_engine.engine import GameEngine

class CharacterManager:
    def __init__(self, ai_helpers=None):
        self.ai_helpers = ai_helpers

    def create_character(self, player_character):
        """
        Creates a character in the game using BLOOM for depth and GPT-2 for balance.

        Args:
            player_character (dict): Information about the character to be created.
            relationship (dict): The relationship object between BLOOM and GPT-2.

        Returns:
            dict: The created character information.
        """
        # Use BLOOM to create a deep and culturally rich character
        player_character = self.bloom.create_character(player_character)

        # Use GPT-2 to balance the character's stats
        balanced_character = self.gpt2.balance_character(player_character)

        # Add the character to the game engine
        self.game_engine.character_manager.create_character(balanced_character)

        return balanced_character

