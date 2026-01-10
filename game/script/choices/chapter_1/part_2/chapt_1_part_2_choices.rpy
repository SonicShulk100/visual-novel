default dijo_picked = False
default mari_picked = False

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
