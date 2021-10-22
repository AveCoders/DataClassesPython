# Python 3.7
from dataclasses import dataclass, field
import random

def price_gen():
    return float(random.randrange(20000, 30000))


@dataclass(frozen=True)
class Car:
    make : str = "BMW"
    model : str = "Mini-Cooper"
    price : float = field(default_factory=price_gen)

    def new_promo(self, promo_price):
        self.price = promo_price

    # def __post_init__(self):
    #     self.promo = f"{self.model} by {self.make} for just {self.price}"

# car1 = Car("BMW", "Mini-Cooper", 27000.85)
# car3 = Car("BMW", "Mini-Cooper", 27000.85)
# car2 = Car("BMW", "i8", 57000.85)
# # print(car1 == car3)
# print(car1.promo)

# car0 = Car()
# print(car0)

car4 = Car()
print(car4.new_promo(20000.50))
# car4.make = "Renault"
# print(car4.make)