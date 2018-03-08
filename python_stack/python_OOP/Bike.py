class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print 'Bike price: {}'.format(self.price)
        print 'Max speed: {}'.format(self.max_speed)
        print 'Total miles: {}'.format(self.miles)
        return self
    def ride(self):
        print  'Riding'
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5
        return self
bike1 = Bike(200, 30)
bike2 = Bike(180, 40)
bike3 = Bike(210, 50)
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
