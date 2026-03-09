init python:
    class VisualNovelCharacter:
        """
        A class to manage visual novel characters with their names, images, and dialogue properties.
        Optimized for 1280x720 resolution.
        """
        
        def __init__(self, name, image_prefix, default_size=(400, 500), color="#c8ffc8"):
            """
            Initialize a character with all essential properties.
            
            Args:
                name (str): Character's display name shown in dialogue
                image_prefix (str): Prefix for image files (e.g., "eileen" for "eileen_happy.png")
                default_size (tuple): Default image size (width, height) for 1280x720 screen
                color (str): Hex color code for the character's name in dialogue boxes
            """
            #Added the default size parameter to ensure images are optimized for 1280x720 resolution
            self.name = name
            self.image_prefix = image_prefix
            self.default_size = default_size
            self.color = color
            self.emotions = {}
            
            # Create the Ren'Py Character object for dialogue
            self.character = Character(self.name, color=self.color)
        
        def add_emotion(self, emotion_name, image_path, size=None):
            if size is None:
                size = self.default_size

            # Check if the image file exists before registering
            if not renpy.loadable(image_path):
                return

            self.emotions[emotion_name] = {
                'path': image_path,
                'size': size
            }

            try:
                image_tag = f"{self.image_prefix} {emotion_name}"
                renpy.image(image_tag, image_path)
            except Exception:
                self.emotions.pop(emotion_name, None)  # Roll back if registration fails
        
        def show(self, emotion="neutral", position="center", transition="dissolve"):
            """
            Show the character with specified emotion, position, and transition.
            
            Args:
                emotion (str): The emotion/expression (default: "neutral")
                position (str): Screen position like "left", "center", "right" (default: "center")
                transition (str): Transition effect like "dissolve", "fade" (default: "dissolve")
            
            Example:
                char.show("happy", "left", "dissolve")
                # Executes: show char happy at left with dissolve
            """
            image_tag = f"{self.image_prefix} {emotion}"
            
            if transition:
                renpy.show(image_tag, at_list=[position], transition=getattr(renpy, transition, dissolve))
            else:
                renpy.show(image_tag, at_list=[position], transition=dissolve)
        
        def hide(self, emotion=None, transition="dissolve"):
            """
            Hide the character with optional emotion specification and transition.
            
            Args:
                emotion (str): Optional emotion to hide specific expression (default: None)
                transition (str): Transition effect (default: "dissolve")
            
            Example:
                char.hide("happy", "dissolve")
                # Executes: hide char happy with dissolve
                
                char.hide()
                # Executes: hide char with dissolve
            """
            if emotion:
                image_tag = f"{self.image_prefix} {emotion}"
            else:
                image_tag = self.image_prefix
            
            if transition:
                renpy.hide(image_tag, transition=getattr(renpy, transition, dissolve))
            else:
                renpy.hide(image_tag)
        
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
                dict: Character properties including name, image_prefix, size, color, and emotions
            """
            return {
                'name': self.name,
                'image_prefix': self.image_prefix,
                'default_size': self.default_size,
                'color': self.color,
                'emotions': self.get_emotions_list()
            }
        
        def __repr__(self):
            """String representation of the character."""
            return f"VisualNovelCharacter(name='{self.name}', prefix='{self.image_prefix}', emotions={len(self.emotions)})"