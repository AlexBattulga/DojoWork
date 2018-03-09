class MathDojo(object):                                                         # Assignment Math Dojo
    def __init__(self):                                                         # Create a Python class called MathDojo that has the methods add and subtract.
        self.result = 0                                                         # Have these 2 functions take at least 1 parameter.Then create a new instance called md
    def add(self, *args):                                                       # Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list.
        if not args:                                                            # Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons
            print 'Please provide number'                                       # Checks if parameter is null
        else:
            for arg in args:                                                    # Checks passed value is not a string or dict
                if type(arg) is int:
                    self.result += arg
                elif type(arg) is list:
                    for val in range(len(arg)):
                        self.result += arg[val]
                elif type(arg) is tuple:
                    for tval in arg:
                        self.result += tval                                     # If type is tuples adding to self.result
                else:
                    print 'Invalid input. Please enter number or a list'
        return self

    def subtract(self, *args):
        if not args:                                                            # Checks if parameter is null
            print 'Please provide number'
        else:
            for arg in args:                                                    # Checks passed value is not a string or dict
                if type(arg) is int:
                    self.result -= arg
                elif type(arg) is list:
                    for val in range (len(arg)):
                        self.result -= arg[val]
                elif type(arg) is tuple:
                    for tval in arg:
                        self.result -= tval
                else:
                    print 'Invalid input!!!!'
        return self
md = MathDojo()
# print md.add(2).add(2, 5).subtract(3, 2).result
# print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result
print md.add((1,2,3), 3, 4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, (2,3,4), [1.1,2.3]).result       # Passing tuples and lists of integers
