label chapter_1_part_3_1:
  dijo "Let's head back."

  if dijo_picked == True:
    jump chapter_1_part_3_1_dijo
  elif mari_picked == True:
    jump chapter_1_part_3_1_mari
  elif jess_picked == True:
    jump chapter_1_part_3_1_jess
  elif cin_picked == True:
    jump chapter_1_part_3_1_cin
  elif jeha_picked == True:
    jump chapter_1_part_3_1_jeha