#For the choices
default dijo_introduced = False
default mari_introduced = False
default jess_introduced = False
default cin_introduced = False
default jeha_introduced = False

label introduct_choice:
  "Which of the characters fo you want to know...?"
  menu:
    "Dijonay" if not dijo_introduced:
      $ dijo_introduced = True
      jump dijo_introduct
