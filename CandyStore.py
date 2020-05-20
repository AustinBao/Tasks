class Customer:
    def __init__(self, firstname, lastname, money):
        self.firstname = firstname
        self.lastname = lastname
        self.money = money

    def buy(self, candybar):
        print("Candy bought: " + candybar.brandname)


class CandyBar:
    def __init__(self, brandname, price):
        self.brandname = brandname
        self.price = price


class Store:
    def __init__(self, brandofbar):
        self.brandofbar = brandofbar

    def sell(self, customer, candybar):
        change = customer.money - candybar.price
        print("Money left " + str(change))


twix = CandyBar('Twix', 4)
snicker = CandyBar('Snickers', 3)
kitkat = CandyBar('KitKat', 2)
mars = CandyBar('Mars', 3)


cust_1 = Customer('Austin', 'Bao', 12)

cust_1.buy(mars)
cust_1.buy(kitkat)


cashier_1 = Store(mars)
cashier_1.sell(cust_1, mars)




