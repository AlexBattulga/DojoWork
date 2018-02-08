def compareList(a, b):
    if cmp(a, b) == 0:                  # cmp function is compareing two lists and if return 0 they are the same if 1 or -1 they are not the same
        print "The lists are the same"
    else:
        print "The lists are not the same"
#Inputs
a = [1,2,5,6,2]
b = [1,2,5,6,2]

c = [1,2,5,6,5]
d = [1,2,5,6,5,3]

e = [1,2,5,6,5,16]
f = [1,2,5,6,5]

g = ['celery','carrots','bread','milk']
h = ['celery','carrots','bread','cream']

compareList(g, h)                       #Calling a function and passing the input
