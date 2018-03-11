def findChar(a):
    char = 'o'
    new_list = []
    for i in range(0, len(a)):
        if char in a[i]:                # using a 'in' function to checking if list of words has a characacter 'o' in it.
            new_list.append(a[i])       # adding them into new array called new_List
    print new_list

word_list = ['hello','world','my','name','is','Anna']
findChar(word_list)
