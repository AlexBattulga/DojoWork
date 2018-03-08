class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
        self.add_tax(12).displayInfo()

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax_amount):
        if type(tax_amount) == float:
            print 'Total price with sales tax: ${}'.format(self.price + (self.price * tax_amount))
        elif type(tax_amount) == int:
            tax_amount = float(tax_amount)/100
            print 'Total price with sales tax: ${}'.format(self.price + (self.price * tax_amount))
        return self

    def Return(self, status):
        if status == 'defective':
            self.status = 'defective'
            self.price = 0
        elif status == 'new':
            self.status = 'for sale'
        else:
            self.status = 'used'
            print 'With 20 percent discount: ${}'.format(self.price * .80)
        return self

    def displayInfo(self):
        print 'Price: ${}'.format(self.price)
        print 'Item Name: {}'.format(self.item_name)
        print 'Weight: {}lb'.format(self.weight)
        print 'Brand: {}'.format(self.brand)
        print 'Status: {}'.format(self.status)
        return self

iphone = Product(800, 'iphone 7 plus', 2, 'apple')
