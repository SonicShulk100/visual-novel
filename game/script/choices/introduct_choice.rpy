#For the choices
default dijo_introduced = False
default mari introduced = False
defualt jess introduced = False
default cin introduced = False
default jeha introduced = False

label introduct_choice:
  "Which of the characters fo you want to know...?"
  menu:
    "Dijonay" if not dijo_introduced:
      $ dijo_introduced = True
      jump dijo_introduct
