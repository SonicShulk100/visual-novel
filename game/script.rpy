#Using python for initializing the characters.
init python:
    #Maria
    Maria = VisualNovelCharacter("Maria", "mari", "#5199e9")
    #Jessica
    Jessica = VisualNovelCharacter("Jessica", "jess", "#e1c5da")

    #Kurt
    Unknown = VisualNovelCharacter("Unknown", "unknown", "#a5a5a5")
    Kurt = VisualNovelCharacter("Kurt", "kurt", "#a5a5a5")

    character_list = [Maria, Jessica]

    emotion_list = ["angry", "babykicks", "contraction", "neutral", "sad", "waterbreak"]

    for char in character_list:
        for emotion in emotion_list:
            char.add_emotion(f"{emotion}", f"images/characters/{char.image_prefix}/{char.image_prefix}_{emotion}.png")

#Defining the characters.
define mari = Maria.character
define jess = Jessica.character
define unknown = Unknown.character
define kurt = Kurt.character

label start:
    jump introduction_part_1