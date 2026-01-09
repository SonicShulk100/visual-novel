#Initialiazing charactes with emotions
init python:
    Dijonay = VisualNovelCharacter("Dijonay", "dijo", "#0000FF")
    Maria = VisualNovelCharacter("Maria", "mari", "#5199E9")
    Jessica = VisualNovelCharacter("Jessica", "jess", "#F4F3F5")
    Cindy = VisualNovelCharacter("Cindy", "cin", "#B2A78A")
    Jehanne = VisualNovelCharacter("Jehanne", "jeha", "#5A5A5A")

    characters = [Dijonay, Maria, Jessica, Cindy, Jehanne]
    emotion_list = ["neutral", "angry", "sad", "babykicks", "contraction", "waterbreak"]

    for char in characters:
        for emotion in emotion_list:
            char.add_emotion(emotion, f"images/characters/{char.image_prefix}/{char.image_prefix}_{emotion}.png")

#Defining protagonists.
define dijo = Dijonay.character
define mari = Maria.character
define jess = Jessica.character
define cin = Cindy.character
define jeha = Jehanne.character

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
        "Maria":
            jump mari_action
        "Jessica":
            jump jess_action
        "Cindy":
            jump cin_action
        "Jehanne":
            jump jeha_action
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

    dijo "This is me going in labor"

    hide dijo waterbreak with dissolve
    jump start

label mari_action:
    show mari neutral at center
    with dissolve

    mari "This is me being neutral"

    show mari angry at center
    with dissolve

    mari "This is me being angry"

    show mari sad at center
    with dissolve

    mari "This is me being sad"
    
    show mari babykicks at center
    with dissolve

    mari "This is me feeling the babies kick"

    show mari contraction at center
    with dissolve

    mari "This is me feeling a contraction"

    show mari waterbreak at center
    with dissolve

    mari "This is me going in labor"
    
    hide mari waterbreak with dissolve
    jump start

label jess_action:
    show jess neutral at center
    with dissolve

    jess "This is me being neutral"

    show jess angry at center
    with dissolve

    jess "This is me being angry"

    show jess sad at center
    with dissolve

    jess "This is me being sad"

    show jess babykicks at center
    with dissolve

    jess "This is me feeling the babies kick"

    show jess contraction at center
    with dissolve

    jess "This is me experiecing a contraction"

    show jess waterbreak at center
    with dissolve

    jess "This is me going in labor"

    hide jess waterbreak with dissolve
    jump start

label cin_action:
    show cin neutral at center
    with dissolve

    cin "This is me being neutral"

    show cin angry at center
    with dissolve

    cin "This is me being angry"

    show cin sad at center
    with dissolve

    cin "This is me being sad"

    show cin babykicks at center
    with dissolve

    cin "This is me feeling the babies kick"

    show cin contraction at center
    with dissolve

    cin "This is me experiecing a contraction"

    show cin waterbreak at center
    with dissolve

    cin "This is me going in labor"

    hide cin waterbreak with dissolve
    jump start

label jeha_action:
    show jeha neutral at center
    with dissolve

    jeha "This is me being neutral"

    show jeha angry at center
    with dissolve

    jeha "This is me being angry"

    show jeha sad at center
    with dissolve

    jeha "This is me being sad"

    show jeha babykicks at center
    with dissolve

    jeha "This is me feeling the babies kick"

    show jeha contraction at center
    with dissolve

    jeha "This is me experiecing a contraction"

    show jeha waterbreak at center
    with dissolve

    jeha "This is me going in labor"

    hide jeha waterbreak with dissolve
    jump start
