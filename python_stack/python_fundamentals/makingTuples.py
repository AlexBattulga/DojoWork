my_dict = {                                                                     # function input
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tupleMaker(a):
    new_list = []
    for i in a.items():
        new_list.append(i)
    print new_list,

tupleMaker(my_dict)
