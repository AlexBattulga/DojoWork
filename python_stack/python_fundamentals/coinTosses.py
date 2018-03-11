import random
def coinTosses(a):
    coinToss = ""
    countx = 0
    county = 0
    for i in range(1, a+1):
        x = random.random()                                 # random.random() will generate random numbers and store in the x, y variables. Random numbers will be less than 0
        y = random.random()
        x_rounded = round(x)                                # rounding up random numbers 1.0 and 0.0
        y_rounded = round(y)
        print                                                               x_rounded, y_rounded
        if x_rounded == 1.0:                                       # checking rounded numbers and adding a conditions
            coinToss = "... It's a head! ..."
            countx += 1
        if y_rounded == 0.0:
            coinToss = "... It's a tail! ..."
            county += 1
        print "Attemp #",i," Throwing a coin", coinToss,"Got", countx,"head(s) so far and",county,"tail(s) so far"
print "Starting the program...\n",coinTosses(5000),"\nEnding the program, thank you!"
