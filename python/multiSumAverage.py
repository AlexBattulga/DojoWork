# #Multiples
# #Part I
for i in range(1, 1000):
    if i % 2 != 0:
        print i # ::::::::: Part I ends :::::::::::
#
# #Part II
sum = 0
for j in range(5, 1000000):
    if j % 5 == 0:
        print j # ::::::::: Part II ends ::::::::::
#
# #Sum List
sum = 0
a = [1, 2, 5, 10, 255, 3]
for k in range(len(a)):
    sum = sum + a[k]
print "Sum of List a value is: ", sum

#Average List
count = 0
total = 0
a = [1, 2, 5, 10, 255, 3]
for value in range(len(a)):
    total += a[value]
    count += 1
avg = total / count
print "Average is: ", avg
