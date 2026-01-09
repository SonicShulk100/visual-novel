label jess_introduct:
  show jess neutral at center
  with dissolve

  "Jessica is the third member of the party."

  "She's a Mewtwo Psychic, wearing a tiger-skinned bikini swimsuit like Maria."
  "And just like the latter, she got hyperpregnant from the magic of the swimsuit. But unlike Maria, she actually liked it."

  hide jess neutral with dissolve

  show mari neutral at left
  show jess neutral at right
  with dissolve

  "They may not look like it, but Maria and Jessica considered themselves as siblings because they once lived in the same orphanage."

  hide mari neutral
  hide jess neutral
  with dissolve

  "Do you want to repeat it?"

  menu:
    "Yes":
      jump jess_introduct
    "No":
      jump introduct_choice
