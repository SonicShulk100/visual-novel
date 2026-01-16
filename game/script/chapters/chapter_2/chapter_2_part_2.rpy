label chapter_2_part_2:
    if not cin_picked:
        "As they prepared to leave the forest, the boy suddenly stirred from his sleep."

        #TODO: Finish the part for Maria
        #TODO: Finish the part for Jessica
        #TODO: Finish the part for Jehanne.

        if dijo_picked:
            dijo "Good morning, Kurt..."

            kurt "G-Good morning..."

            cin "He's awake... Slowly but surely..."

            hide cin neutral
            show jess neutral at left
            with dissolve

            jess "Hi there. The name's Jessica."

            kurt "I-I'm Kurt... Nice to meet you..."

            hide jess neutral
            show jeha neutral at left
            with dissolve

            mari "I'm Maria."

            jeha "And I'm Jehanne."
        
        elif mari_picked:
            mari "Well, speaking of which..."

            dijo "Well... Hello there, Kurt..."

            jess "Looks like our little friend is awake now."

            kurt "Um... Hello...?"

            mari "Don't worry about us. We won't harm you."

            hide mari neutral
            show jess neutral at center
            with dissolve

            jess "Yeah, we're all friends here."

            kurt "F-Friends...?"

            hide jess neutral
            show jeha neutral at right
            with dissolve

            jeha "Obviusly...! We decided to take you in after finding you alone in the forest."

            kurt "I... I see..."

            jeha "By the way, I'm Jehanne."

            dijo "And I'm Dijonay."
        
        elif jess_picked:
            jess "Hey there... Finally took a rest."

            dijo "Looks like our little friend is awake now."
    else:
        kurt "Um... I'm awake...?"

        cin "Ah! Kurt...! You were supposed to be resting..."

        mari "That's his name...?"

        jess "Kurt...?"

        cin "Um... Yes. His name is Kurt. And... That's the only thing he remembers..."

        jess "Well, it's nice to meet you, Kurt."

        mari "I'm Maria, and this is Jessica."

        kurt "R-Right... Nice to meet you both..."

        cin "There are also Jehanne and Dijonay that are still asleep at the moment."

        hide mari neutral
        hide jess neutral
        with dissolve

        show dijo neutral at left
        show jeha neutral at right
        with dissolve

        dijo "Did you say something...?"

        cin "Nevermind..."

        jeha "Good morning, sleepyheads~"

        kurt "G-Good morning..."

        cin "Looks like everyone is awake now..."

    #TODO: Continue the story from here for chapter 2 part 2