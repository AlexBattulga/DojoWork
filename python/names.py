students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(a):                                                                   # Part I
    fname = ""                                                                  # Empty strings for first and last name
    lname = ""
    for i in a:
        for j in i.iteritems():
            fname = i['first_name']                                             # Storing first and last name to empty string variables
            lname = i['last_name']
        print fname, lname
# names(students)                                                               # Passing a value

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def info(a):                                                                    # Part II
    for i, j in a.iteritems():                                                  # i contains 2 lists and j has value of dictionaries inside the lists
        print i                                                                 # i will display Students and Instructors
        count = 0                                                               # increment by +1
        for k in j:                                                             # accessing into dictionary 
            count += 1
            print count," - ",k['first_name'].upper(), k['last_name'].upper()," - ", len(k['first_name'])+len(k['last_name'])

info(users)
