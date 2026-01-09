# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

init python:
    Dijonay = VisualNovelCharacter("Dijonay", "dijo", "#0000FF")

    characters = [Dijonay]
    emotion_list = ["neutral", "angry", "sad", "babykicks", "contraction", "waterbreak"]

    for char in characters:
        for emotion in emotion_list:
            char.add_emotion(emotion, f"images/characters/{char.image_prefix}/{char.image_prefix}_{emotion}.png")

define dijo = Dijonay.character

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Which one do you want to know about?"
    menu:
        "Dijonay":
            jump dijo_action
        "Finish":
            return

label dijo_action:
    show dijo neutral at center
    with dissolve

    dijo "This is me being neutral"

    show dijo angry at center
    with dissolve

    dijo "This is me being angry"

    show dijo sad at center
    with dissolve

    dijo "This is me sad."

    show dijo babykicks at center
    with dissolve

    dijo "This is me feeling the babies kick."

    show dijo contraction at center
    with dissolve

    dijo "This is me feeling a contraction"

    show dijo waterbreak at center
    with dissolve

    dijo "This is me going in labor."

    hide dijo waterbreak with dissolve
    jump start
