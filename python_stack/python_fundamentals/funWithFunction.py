def oddEven(a):                    # Odd or even function
    oddOrEven = ""
    if type(a) is int:             # Checking if parameter value is integer
        for i in range(1, a):
            if i % 2 is 0:         # Finding a even numbers
                addOrEven = ".  This is an even number"
            else:
                addOrEven = ".  This is an odd number"
            print "Number is ", i,addOrEven

# oddEven(2)                       # Calling a function and passing a integer

def multiply(b, num):              # Multiply
    multi = []
    for i in b:
        multi.append(i * num)      # Each value of list "b" is multiplied by 5 and added into new list multi
    return multi                   # Returning multi value

a = [2,4,10,16]
b = multiply(a, 5)                 # Passing a two values a list and integer
# print b

def layered_multiples(arr):
    val = 1
    new_arr = []
    for i in range(len(arr)):      # It will create loop 3 times
        second_arr = []
        for j in range(arr[i]):
            second_arr.append(val) # Storing "1" to list called second_arr
        new_arr.append(second_arr) # Storing second_arr list into new_arr
    return new_arr

x = layered_multiples(multiply([2,4,5],3)) #Calling multiply function and passing a list and passing a result to layered_multiples
print x
