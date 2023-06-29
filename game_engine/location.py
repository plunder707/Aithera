    def generate_location(self, location_description, relationship):
        """
        Generates a location in the game using BLOOM for depth and GPT-2 for realism.

        Args:
            location_description (str): A basic description of the location.
            relationship (dict): The relationship object between BLOOM and GPT-2.

        Returns:
            dict: The generated location information.
        """
        # Use BLOOM to generate a description of a new location
        location_description = self.bloom.generate_location(location_description, relationship)

        # Use GPT-2 to create a more detailed and realistic version of the location
        detailed_location = self.gpt2.generate_location(location_description, relationship)

        return detailed_location