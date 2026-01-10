default dijo_picked = False
default mari_picked = False
default jess_picked = False
default cin_picked = False

label chapt_1_part_2_choices:
  show dijo neutral at center
  hide jeha neutral
  with dissolve

  dijo "So... Are there any volunteers for picking him up?"

  menu:
    "Silence was the only thing that Dijo heard.":
      $ dijo_picked = True
      jump chapt_1_part_2_dijo
    "Maria : Maybe I would like to.":
      $ mari_picked = True
      jump chapt_1_part_2_mari
    "Jessica : Do you mind if I pick him up?":
      $ jess_picked = True
      jump chapt_1_part_2_jess
    "Cindy : I'll do it!":
      $cin_picked = True
      jump chapt_1_part_2_cin
