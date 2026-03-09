#Introduced or not
default dijo_introduced = False
default maria_introduced = False
label introduction_choice:

    "Which one of you want to introduce?"

    #TODO: Do the introduction for each character, and then jump to the next part of the story.
    menu:
        "Dijonay" if not dijo_introduced:
            $ dijo_introduced = True
            jump dijo_introduct
        "Maria" if not maria_introduced:
            $ maria_introduced = True
            jump mari_introduct
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
        "Continue" if dijo_introduced:
            #TODO: Jump to the next part of the story.
            pass
