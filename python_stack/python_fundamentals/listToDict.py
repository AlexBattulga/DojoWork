name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "ALex"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def listToDict(list1, list2):
    new_dict = {}
    real_dict = {}
    for i in list1:
        for j in list2:
            new_dict = zip(list1, list2)
    real_dict = dict(new_dict)
    print real_dict
listToDict(name, favorite_animal)
