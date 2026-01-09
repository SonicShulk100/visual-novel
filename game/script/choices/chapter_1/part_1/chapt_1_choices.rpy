default talked_dijo = False
default talked_mari = False
default talked_jess = False
default talked_cin = False
default talked_jeha = False

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
    "Jehanne" if not talked_jeha:
      $ talked_jeha = True
      jump chapt_1_jeha
    "Continue" if (
      talked_dijo and
      talked_mari and
      talked_jess and
      talked_cin and
      talked_jeha
      ):
      jump chapter_1_part_2
