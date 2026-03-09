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
    Kootie = VisualNovelCharacter("Kootie", "kootie", "#dcde01")

    emotion_list = ["neutral", "happy", "sad", "angry", "babykicks", "contraction", "waterbreak", "intimidated"]
    characters = [Dijonay, Maria, Jessica, Cindy, Jehanne, Antoinette, Whitney, Kootie]

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
define kootie = Kootie.character
label start:

    jump introduction_part_1