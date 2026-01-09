default talked_dijo = False
default talked_mari = False
default talked_jess = False
default talked_cin = False

label chapt_1_choices:
  "Which characters do you want to talk about"
  menu:
    "Dijonay" if not talked_dijo:
      $ talked_dijo = True
      jump chapt_1_dijo
    "Maria" if not talked_mari:
      $ talked_mari = True
      jump chapt_1_mari
    "Jessica" if not talked_jess:
      $ talked_jess = True
      jump chapt_1_jess
    "Cindy" if not talked_cin:
      $ talked_cin = True
      jump chapt_1_cin
