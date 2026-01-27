init python:
    Maria = VisualNovelCharacter("Maria", "mari", "#5199e9")
    Jessica = VisualNovelCharacter("Jessica", "jess", "#e1c5da")

    character_list = [Maria, Jessica]

    emotion_list = ["angry", "babykicks", "contraction", "neutral", "sad", "waterbreak"]

    for char in character_list:
        for emotion in emotion_list:
            char.add_emotion(f"{emotion}", f"images/characters/{char.image_prefix}/{char.image_prefix}_{emotion}.png")

define mari = Maria.character
define jess = Jessica.character

# The game starts here.

label start:
    jump introduction_part_1