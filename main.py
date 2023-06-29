from ai_models.bloom_model import generate_with_bloom
from ai_models.gpt2_model import generate_with_gpt2
from game_engine.engine import GameEngine

if __name__ == "__main__":
    # AI Helpers
    ai_helpers = {
        "bloom": generate_with_bloom,
        "gpt2": generate_with_gpt2
    }

    # Initialize the game engine with AI helpers
    game_engine = GameEngine(ai_helpers)

    # Example character information
    character_info = {
        "name": "Aria",
        "class": "Wizard",
        "race": "Elf"
    }

    backstory = generate_with_bloom(f"A backstory for {character_info['name']}")

    print(backstory)

    # Create a character
    character = game_engine.create_character(character_info)
    print(character)

    # Example location information
    location_info = {
        "type": "forest",
        "features": ["trees", "river", "ancient ruins"]
    }

    # Generate a location
    location = game_engine.generate_location(location_info)
    print(location)

    # ... rest of the game initialization and logic