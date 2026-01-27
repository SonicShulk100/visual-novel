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

    "Which do you want to test"

    menu:
        "Maria":
            jump maria_test
        "Jessica":
            jump jess_start
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

label jess_start:

    show jess neutral at center
    with dissolve
    jess "This is me neutral"
    show jess angry at center
    with dissolve
    jess "This is me angry"
    show jess sad at center
    with dissolve
    jess "This is me sad"
    show jess babykicks at center
    with dissolve
    jess "This is me babykicks"
    show jess contraction at center
    with dissolve
    jess "This is me contraction"
    show jess waterbreak at center
    with dissolve
    jess "This is me water break."
    hide jess waterbreak with dissolve
    jump start