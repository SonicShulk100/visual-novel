default mari_rescue = False

label rescue_choice:

    show mari neutral at right
    show jess neutral at left
    with dissolve

    "Who do you want to help the unconscious werewolf boy?"

    menu:
        "Maria":
            $ mari_rescue = True

            hide mari neutral
            hide jess neutral
            with dissolve

            jump rescue_mari
