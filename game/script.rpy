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
    jump introduction_part_1
