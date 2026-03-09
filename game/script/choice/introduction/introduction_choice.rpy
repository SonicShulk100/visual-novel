#Introduced or not
default dijo_introduced = False
default maria_introduced = False
default jessica_introduced = False
default cindy_introduced = False
default jehanne_introduced = False
default whitney_introduced = False
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
        "Jessica" if not jessica_introduced:
            $ jessica_introduced = True
            jump jess_introduct
        "Cindy" if not cindy_introduced:
            $ cindy_introduced = True
            jump cin_introduct
        "Jehanne" if not jehanne_introduced:
            $ jehanne_introduced = True
            jump jeha_introduct
        "Antoinette":
            #TODO: Do the introduction for Antoinette.
            pass
        "Whitney" if not whitney_introduced:
            $ whitney_introduced = True
            jump whitney_introduct
        "Kootie":
            #Do the introduction for Kootie.
            pass
        "Continue" if dijo_introduced and maria_introduced and jessica_introduced and cindy_introduced and jehanne_introduced and whitney_introduced:
            #TODO: Jump to the next part of the story.
            pass
