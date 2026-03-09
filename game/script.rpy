init python:
    Dijonay = VisualNovelCharacter("Dijonay", "dijo", "#0000FF")

    emotion_list = ["neutral", "happy", "sad", "angry", "babykicks", "contraction", "waterbreak", "intimidated"]
    characters = [Dijonay]

    for character in characters:
        for emotion in emotion_list:
            character.add_emotion(emotion, f"images/characters/{character.image_prefix}/{character.image_prefix}_{emotion}.png")

#Defining the characters.
define dijo = Dijonay.character

label start:

    scene bg room

    "Which character do you want to test?"

    menu:
        "Dijonay":
            jump dijonay_test
        "None":
            return

#Characters to test
default emotion_list = ["neutral", "sad", "angry", "babykicks", "contraction", "waterbreak", "intimidated"]

#For Dijonay.
label dijonay_test:
    python:
        for emotion in emotion_list:
            if emotion not in Dijonay.emotions:
                continue
            renpy.show("dijo " + emotion, at_list=[center])
            renpy.with_statement(dissolve)
            renpy.say(dijo, f"This is me {emotion}.")
            renpy.hide("dijo " + emotion)
            renpy.with_statement(dissolve)
    
    jump start