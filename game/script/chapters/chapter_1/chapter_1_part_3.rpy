label chapter_1_part_3:
    #TODO: Do the ending of the first chapter.

    hide mari neutral
    hide jess neutral
    with dissolve

    scene forest-night
    with fade

    if mari_rescue:
        show mari neutral at center
        show jess neutral at right
        with dissolve
    
    elif jess_rescue:
        show jess neutral at center
        show mari neutral at right
        with dissolve

    "For quite a while, the two girls stayed like that, their hands on each other's ass, waiting for the unconscious werewolf boy to wake up."

    if mari_rescue:
        "With Maria still craddling the young werewolf boy in her arms."

        jess "How long is it going to take for him to wake up?"

        mari "Just be patient. I'm sure it will not be long."
    
    elif jess_rescue:
        "With Jessica still craddling the young werewolf boy in her arms."

        mari "How long is it going to take for him to wake up?"

        jess "Just be patient. I'm sure it will not be long."
    
    "It was just as the two girls had hoped, the werewolf boy began to stir and slowly open his eyes."

    unknown "Hmm...? W-Where... am I...?"

    jess "Ah. You're finally awake."

    mari "Welcome back. You were unconscious for a while."

    unknown "I... I was...? So... Why am I here?"

    if mari_rescue:
        jess "We found you unconscious in the forest and brought you here to safety."

        mari "Right. Hence why you see me craddling you in my arms."
    
    elif jess_rescue:
        mari "We found you unconscious in the forest and brought you here to safety."

        jess "Right. Hence why you see me craddling you in my arms."

    unknown "Oh... I see... Thank you for saving me..."

    jess "That aside, do you remember anything about yourself? Like who you are or how you got here?"

    unknown "My name is Kurt... But anything else I don't remember... I don't even remember how I got here... Aside from what you said..."

    jess "Well then, Kurt... Until you remember anything else, you can stay here with us. We will take care of you."

    mari "That's right. It's not safe for you to be out in the forest alone, especially with the full moon tonight."

    kurt "T-Thank you two... I really appreciate it..."

    jess "It's Jessica, by the way. And this is Maria."

    mari "Nice to meet you, Kurt. I hope we can get along well together."

    kurt "Y-Yeah... Nice to meet you both too..."

    "And so, the three of them stayed together at the campfire for the rest of the night, talking and getting to know each other better."

    "Eventually, they all went to sleep, with Kurt sleeping in between Maria and Jessica for warmth and comfort."

    hide mari neutral
    hide jess neutral
    with dissolve

    jump chapter_2_part_1