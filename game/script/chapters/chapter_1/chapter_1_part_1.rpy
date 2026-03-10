label chapter_1_part_1:
    scene farm-day with fade

    "The sun was shining brightly over the vast expanse of the farm. The birds were chirping, and the gentle breeze rustled through the leaves of the trees. It was a perfect day for work."

    "One day, a young man, who was looking for a job, stumbled upon the farm. He was tired and hungry, and he hoped to find some work to earn a living."

    show dijo neutral at center
    with dissolve

    "There, she noticed Dijonay waiting by the gate, looking at her phone."

    "The young man approached her."

    python:
        player_name = renpy.input("What is the young man's name?", default="John").strip()

        if not player_name:
            player_name = "John"

        Player = VisualNovelCharacter(player_name, player_name.lower(), color="#7fffd4")
        player = Player.character
        dijo = Dijonay.character

    player "Excuse me, miss. Do you, um... know if there are any jobs available around here?"

    "Dijonay looked up to the young man, her eyes widening with surprise. She hadn't expected anyone to approach her, especially not someone who seemed so out of place in the rural setting."

    dijo "Oh, um... What's your name?"

    player "My name is [player_name], and I was supposed to be here for an interview."

    dijo "Oh! I remember, now! I was supposed to meet someone here today for an interview. It's you, right?"

    player "Yes, that's me."

    dijo "Wonderful! Follow me. All will be explained."

    "And so, both [player_name] and Dijonay walked towards the farmhouse, where the rest of the story would unfold."

    scene farm-livingroom with fade

    show dijo neutral at center
    with dissolve

    "They first went to where Dijonay was working. The two sat down."

    dijo "So, [player_name], what do you know about this farm? Do you have any experience working on a farm?"

    player "No... but I just happen to see the job description, saying that I would be working with sexy females."

    player "Not to be rude or anything, but I was skeptical about it seeing your... body..."

    "Dijonay rubbed her belly."

    dijo "Well, I can understand your skepticism, but I assure you that this farm is quite unique. We have a special way of doing things here."

    dijo "And by that I mean, we all are 8 hyperpregnant ladies, myself included."

    player "Wait, what? Hyperpregnant? What does that even mean?"

    dijo "It means that we are all pregnant, and not just a little bit. We are all very, very pregnant."

    dijo "In fact, it's been 12 years since all of us have become hyperpregnant."

    player "That's... quite a situation. If I may ask, how many are in your womb?"

    dijo "We each have 24 babies."

    player "24?! That's... that's a lot of babies! How do you even manage to take care of all of them?"

    dijo "They're inside our womb. Though our ways of getting this hyperpregnant differ, it's not rocket science."

    player "I see... So, what exactly would my job be here on the farm?"

    dijo "Well..."

    "Dijonay put [player_name]'s hands on her belly."