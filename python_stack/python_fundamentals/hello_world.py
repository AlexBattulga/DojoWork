firstN = "Alex"
lastN = "Battulga"
dob = 1990
print "My name is {} {} {}".format(firstN, lastN, dob)
hw = "hello %s" % 'world'
print hw

str = " Alex success success success success success Alex success"
print str.count("success")

str1 = " Alex success success success success success Alex success"
print str1.endswith("success")

str1 = "Alex Alex Alex Alex Alex success success success success success Alex success"
print str1.find("success")
print len("Total number of letters are: " +str1);

str1 = "nartai"
print str1.isupper()

print enumerate(str)

list = [5, 6, 6, 7, 8]

print list.insert(2, 90)

for count in range(1, 10):
    if(count % 2 != 0):
        print "Even numbers ", count
i = 1
while i < 10:
    print "While loop - ", i
    i += 1

x = 3
y = x
while y > 0:
  print y
  y = y - 1
else:
  print "Final else statement"
