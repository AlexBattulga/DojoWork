#Find replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
print words.replace("day", "month", 1)

#Min and Max
x = [2,54,-2,7,12,98]
maxNum = max(x)
minNum = min(x)
print "Max number is: ", maxNum, "\nMin number is: ", minNum

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
firstNum = x[0]
lastNum = x[len(x) - 1]
print "First number is: ", firstNum, "\nLast number is: ", lastNum

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print "Sorted order: ",x
firstArr =[]
secondArr = []
newArr = []
for i in range (0, len(x)):
    if x[i] < 10:
        firstArr.append(x[i])
    else:
        secondArr.append(x[i])
secondArr.insert(0, firstArr)
print secondArr
