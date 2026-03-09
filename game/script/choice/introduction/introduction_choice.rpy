#Introduced or not
default dijo_introduced = False
default maria_introduced = False
default jessica_introduced = False
default cindy_introduced = False
default jehanne_introduced = False
default whitney_introduced = False
default antoinette_introduced = False
default kootie_introduced = False
label introduction_choice:

    "Which one of you want to introduce?"

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
        "Antoinette" if not antoinette_introduced:
            $ antoinette_introduced = True
            jump antoinette_introduct
        "Whitney" if not whitney_introduced:
            $ whitney_introduced = True
            jump whitney_introduct
        "Kootie" if not kootie_introduced:
            $ kootie_introduced = True
            jump kootie_introduct
        "Continue" if dijo_introduced and maria_introduced and jessica_introduced and cindy_introduced and jehanne_introduced and whitney_introduced and antoinette_introduced and kootie_introduced and kootie_introduced:
            jump introduction_part_2
