# Description: Unit tests for the Aitheria Game Engine
import unittest
from unittest.mock import MagicMock
from game_engine.engine import GameEngine

class TestAitheriaGame(unittest.TestCase):
    def setUp(self):
        self.bloom = MagicMock()
        self.gpt2 = MagicMock()
        self.ai_helpers = {"bloom": self.bloom, "gpt2": self.gpt2}
        self.game_engine = GameEngine(self.ai_helpers)

    def test_create_character_with_ai(self):
        player_character = {"name": "Test Character", "race": "Elf", "class": "Wizard"}
        character = self.game_engine.create_character(player_character)
        self.assertEqual(character["name"], "Test Character")
        self.assertEqual(character["race"], "Elf")
        self.assertEqual(character["class"], "Wizard")

    def test_generate_location_with_ai(self):
        location_description = "A spooky forest"
        location = self.game_engine.generate_location(location_description)
        self.assertEqual(location["description"], "A spooky forest")

    def test_bloom_is_called_when_creating_character(self):
        player_character = {"name": "Test Character", "race": "Elf", "class": "Wizard"}
        self.game_engine.create_character(player_character)
        self.bloom.create_character.assert_called_once()

    def test_gpt2_is_called_when_creating_character(self):
        player_character = {"name": "Test Character", "race": "Elf", "class": "Wizard"}
        self.game_engine.create_character(player_character)
        self.gpt2.balance_character.assert_called_once()


if __name__ == '__main__':
    unittest.main()
