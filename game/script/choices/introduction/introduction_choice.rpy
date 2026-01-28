#Added the variables.
default mari_introduced = False
default jess_introduced = False

label introduction_choice:
    "Which character do you want to know?"
    
    #TODO: Do the introduction for Jessica.

    menu:
        "Maria" if not mari_introduced:
            $ mari_introduced = True
            jump introduction_mari
        "Jessica" if not jess_introduced:
            $ jess_introduced = True
            jump introduction_jess
