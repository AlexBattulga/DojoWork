def draw_stars(l):                              # Part I
    star = "*"
    for i in range (len(l)):
        new_stars = ""                          # Creating new empty string when i incremented by 1
        for j in range (l[i]):
            new_stars += star                   # Adding star to empty list "new_stars"
        print new_stars

x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x)                                 # Passing a list to function


def draw_stars(l):                              # Part II
    star = "*"
    for i in range (len(l)):
        new_stars = ""
        new_letters = ""
        if isinstance(l[i], basestring):
            new_stars = list(l[i])
            for k in new_stars:
                new_letters += new_stars[0]
            print new_letters.lower()
        else:
            for j in range (l[i]):
                new_stars += star
        print new_stars

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
a = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)
