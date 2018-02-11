bio = {"name": "Anna", "age": "101", "country of birth": "The United States", "favorite language": "Python"}

def basicDict(a):
    for i, j in a.iteritems():
        print "My", i, "is", j
basicDict(bio)
