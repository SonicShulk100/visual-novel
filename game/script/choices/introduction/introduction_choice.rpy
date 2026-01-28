#Added the variables.
default mari_introduced = False
default jess_introduced = False

label introduction_choice:
    "Which character do you want to know?"

    menu:
        "Maria" if not mari_introduced:
            $ mari_introduced = True
            jump introduction_mari
        "Jessica" if not jess_introduced:
            $ jess_introduced = True
            jump introduction_jess
        "Continue" if mari_introduced and jess_introduced:
            jump introduction_part_2
