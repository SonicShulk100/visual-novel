default talked_dijo = False

label chapt_1_choices:
  "Which characters do you want to talk about"
  menu:
    "Dijonay" if not talked_dijo:
      $ talked_dijo = True
      jump chapt_1_dijo
