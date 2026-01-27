init python:
    Maria = VisualNovelCharacter("Maria", "mari", "#5199e9")

    character_list = [Maria]

    emotion_list = ["angry", "babykicks", "contraction", "neutral", "sad", "waterbreak"]

    for char in character_list:
        for emotion in emotion_list:
            char.add_emotion(f"{emotion}", f"images/characters/{char.image_prefix}/{char.image_prefix}_{emotion}.png")

define mari = Maria.character

# The game starts here.

label start:

    "Which do you want to test"

    menu:
        "Maria":
            jump maria_test
        "Cancel":
            return

label maria_test:
    show mari neutral at center
    with dissolve
    mari "This is me neutral"
    show mari angry at center
    with dissolve
    mari "This is me angry"
    show mari sad at center
    with dissolve
    mari "This is me sad"
    show mari babykicks at center
    with dissolve
    mari "This is me babykicks"
    show mari contraction at center
    with dissolve
    mari "This is me contraction"
    show mari waterbreak at center
    with dissolve
    mari "This is me water break."
    hide mari waterbreak with dissolve
    jump start