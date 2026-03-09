default dijo_introduced = False
label introduction_choice:

    "Which one of you want to introduce?"

    #TODO: Do the introduction for each character, and then jump to the next part of the story.
    menu:
        "Dijonay" if not dijo_introduced:
            #Do the introduction for Dijonay.*
            $ dijo_introduced = True
            jump dijo_introduct
        "Maria":
            #TODO: Do the introduction for Maria.
            pass
        "Jessica":
            #TODO: Do the introduction for Jessica.
            pass
        "Cindy":
            #TODO: Do the introduction for Cindy.
            pass
        "Jehanne":
            #TODO: Do the introduction for Jehanne.
            pass
        "Antoinette":
            #TODO: Do the introduction for Antoinette.
            pass
        "Whitney":
            #TODO: Do the introduction for Whitney.
            pass
        "Kootie":
            #Do the introduction for Kootie.
            pass
        "Continue":
            #TODO: Jump to the next part of the story.
            pass
