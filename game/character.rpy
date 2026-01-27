init python:
    class VisualNovelCharacter:
        """
        A class to manage visual novel characters with their names, images, and dialogue properties.
        """
        
        def __init__(self, name, image_prefix, color="#c8ffc8"):
            """
            Initialize a character with all essential properties.
            
            Args:
                name (str): Character's display name shown in dialogue
                image_prefix (str): Prefix for image files (e.g., "eileen" for "eileen_happy.png")
                color (str): Hex color code for the character's name in dialogue boxes
            """
            self.name = name
            self.image_prefix = image_prefix
            self.color = color

            #D&D Stats
            self.charisma = renpy.random.randint(1, 20)
            self.constitution = renpy.random.randint(1, 20)
            self.wisdom = renpy.random.randint(1, 20)
            self.intelligence = renpy.random.randint(1, 20)
            self.dexterity = renpy.random.randint(1, 20)
            self.strength = renpy.random.randint(1, 20)

            self.emotions = {}
            
            # Create the Ren'Py Character object for dialogue
            self.character = Character(self.name, color=self.color)
        
        def add_emotion(self, emotion_name, image_path):
            """
            Add an emotional state/pose with its corresponding image.
            
            Args:
                emotion_name (str): Name of the emotion (e.g., "happy", "sad", "neutral")
                image_path (str): Path to the image file relative to the game directory
            """
            self.emotions[emotion_name] = {'path': image_path}
            
            # Register the image with Ren'Py's image system
            image_tag = f"{self.image_prefix} {emotion_name}"
            renpy.image(image_tag, image_path)
        
        def show(self, emotion="neutral", position="center"):
            """
            Display the character with a specific emotion.
            
            Args:
                emotion (str): The emotion to display
                position (str): Screen position ("left", "center", "right")
            
            Returns:
                tuple: (image_tag, position) or (None, None) if emotion not found
            """
            if emotion not in self.emotions:
                return None, None
            
            image_tag = f"{self.image_prefix} {emotion}"
            return image_tag, position
        
        def say(self, dialogue):
            """
            Make the character speak dialogue.
            
            Args:
                dialogue (str): The text the character will say
            """
            self.character(dialogue)
        
        def get_emotions_list(self):
            """
            Get a list of all registered emotions for this character.
            
            Returns:
                list: List of emotion names
            """
            return list(self.emotions.keys())
        
        def has_emotion(self, emotion_name):
            """
            Check if a specific emotion is registered for this character.
            
            Args:
                emotion_name (str): Name of the emotion to check
            
            Returns:
                bool: True if emotion exists, False otherwise
            """
            return emotion_name in self.emotions
        
        def get_info(self):
            """
            Get a dictionary with all character information.
            
            Returns:
                dict: Character properties including name, image_prefix, color, and emotions
            """
            return {
                'name': self.name,
                'image_prefix': self.image_prefix,
                'color': self.color,
                'emotions': self.get_emotions_list()
            }
        
        def __repr__(self):
            """String representation of the character."""
            return f"VisualNovelCharacter(name='{self.name}', prefix='{self.image_prefix}', emotions={len(self.emotions)})"