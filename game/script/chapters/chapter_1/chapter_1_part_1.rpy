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

    player "Testing..."