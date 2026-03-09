#Initializing the characters and their emotions.
init python:
    #Characters
    Dijonay = VisualNovelCharacter("Dijonay", "dijo", "#0000FF")
    Maria = VisualNovelCharacter("Maria", "mari", "#5199e9")
    Jessica = VisualNovelCharacter("Jessica", "jess", "#f4f3f5")
    Cindy = VisualNovelCharacter("Cindy", "cin", "#b2a78a")
    Jehanne = VisualNovelCharacter("Jeanne", "jeha", "#5a5a5a")
    Antoinette = VisualNovelCharacter("Antoinette", "antoinette", "#9aab67")
    Whitney = VisualNovelCharacter("Whitney", "whitney", "#11c9cf")

    emotion_list = ["neutral", "happy", "sad", "angry", "babykicks", "contraction", "waterbreak", "intimidated"]
    characters = [Dijonay, Maria, Jessica, Cindy, Jehanne, Antoinette, Whitney]

    for character in characters:
        for emotion in emotion_list:
            character.add_emotion(emotion, f"images/characters/{character.image_prefix}/{character.image_prefix}_{emotion}.png")

#Defining the characters.
define dijo = Dijonay.character
define mari = Maria.character
define jess = Jessica.character
define cin = Cindy.character
define jeha = Jehanne.character
define antoinette = Antoinette.character
define whitney = Whitney.character
label start:

    scene bg room

    "Which character do you want to test?"

    menu:
        "Dijonay":
            jump dijonay_test
        "Maria":
            jump maria_test
        "Jessica":
            jump jessica_test
        "Cindy":
            jump cindy_test
        "Jehanne":
            jump jehanne_test
        "Antoinette":
            jump antoinette_test
        "Whitney":
            jump whitney_test
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

#For Maria.
label maria_test:
    python:
        for emotion in emotion_list:
            if emotion not in Maria.emotions:
                continue
            renpy.show("mari " + emotion, at_list=[center])
            renpy.with_statement(dissolve)
            renpy.say(mari, f"This is me {emotion}.")
            renpy.hide("mari " + emotion)
            renpy.with_statement(dissolve)
    
    jump start

#For Jessica.
label jessica_test:
    python:
        for emotion in emotion_list:
            if emotion not in Jessica.emotions:
                continue
            renpy.show("jess " + emotion, at_list=[center])
            renpy.with_statement(dissolve)
            renpy.say(jess, f"This is me {emotion}.")
            renpy.hide("jess " + emotion)
            renpy.with_statement(dissolve)
    
    jump start

#For Cindy.
label cindy_test:
    python:
        for emotion in emotion_list:
            if emotion not in Cindy.emotions:
                continue
            renpy.show("cin " + emotion, at_list=[center])
            renpy.with_statement(dissolve)
            renpy.say(cin, f"This is me {emotion}.")
            renpy.hide("cin " + emotion)
            renpy.with_statement(dissolve)
    
    jump start

#For Jehanne.
label jehanne_test:
    python:
        for emotion in emotion_list:
            if emotion not in Jehanne.emotions:
                continue
            renpy.show("jeha " + emotion, at_list=[center])
            renpy.with_statement(dissolve)
            renpy.say(jeha, f"This is me {emotion}.")
            renpy.hide("jeha " + emotion)
            renpy.with_statement(dissolve)
    
    jump start

#For Antoinette.
label antoinette_test:
    python:
        for emotion in emotion_list:
            if emotion not in Antoinette.emotions:
                continue
            renpy.show("antoinette " + emotion, at_list=[center])
            renpy.with_statement(dissolve)
            renpy.say(antoinette, f"This is me {emotion}.")
            renpy.hide("antoinette " + emotion)
            renpy.with_statement(dissolve)
    
    jump start

#For Whitney.
label whitney_test:
    python:
        for emotion in emotion_list:
            if emotion not in Whitney.emotions:
                continue
            renpy.show("whitney " + emotion, at_list=[center])
            renpy.with_statement(dissolve)
            renpy.say(whitney, f"This is me {emotion}.")
            renpy.hide("whitney " + emotion)
            renpy.with_statement(dissolve)
    
    jump start