class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "{}'s health: {}".format(self.name, self.health)
        return self
class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health -= 10
        return self.health

    def displayHealth(self):
        print 'I am a DRaGON'
        super(Dragon, self).displayHealth()

dog = Animal('Totoro', 100)
dog.walk().walk().walk().run().run().displayHealth()

small_dog = Dog('Johnny')
small_dog.walk().walk().walk().run().pet().run().displayHealth()

dragon = Dragon('Drogon')
dragon.walk().walk().displayHealth()
