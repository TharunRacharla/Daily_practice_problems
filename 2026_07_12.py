class Mango():
    def __init__(self, price, quality):
            self.__price = price
            self.quality = quality

    def profit(self, quantity):
          return self.__price * 0.1 * quantity
    
raw_mango = Mango(30, "medium")
ripe_mango = Mango(40, "medium")

print(ripe_mango.profit(40))
print(Mango.profit(raw_mango, 40))
print(raw_mango._Mango__price)