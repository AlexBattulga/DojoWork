import random                                                           # importing a random
def scoresGrades(a):
    grade = ""
    for i in range(a):
        random_num = random.randint(60, 100)                            # Generating a random numbers between 60 to 100
        if random_num >= 60 and random_num <= 69:                       # Adding a condition using if
            grade = "D"
        elif random_num >= 70 and random_num <= 79:
            grade = "C"
        elif random_num >= 80 and random_num <= 89:
            grade = "B"
        elif random_num >= 90 and random_num <= 100:
            grade = "A"
        print "Score: ",random_num,";","Your grade is ", grade

print "Scores and Grades\n",scoresGrades(10),"End of the program. Bye!" # Calling a function and displaying results
