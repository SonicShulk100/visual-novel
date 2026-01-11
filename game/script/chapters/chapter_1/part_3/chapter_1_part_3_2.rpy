label chapter_1_part_3_2:
  "The group then went to the campsite."

  "As they arrived..."

  if dijo_picked == True:
    jump chapter_1_part_3_2_dijo
  elif mari_picked == True:
    jump chapter_1_part_3_2_mari
