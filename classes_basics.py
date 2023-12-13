# classes_practicing-

class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age

def __str__(self):
    return f"{self.name}{self.age}"
def Game():
    cat1 = Cat("Bob ", 9)
    cat2 = Cat("Blacky ", 7)
    cat3 = Cat("Rocky ", 3)
    cats = [cat1, cat2, cat3]
    for cat in cats:
        if cat.age < 4:
            r = "коть рад"
        elif cat.age < 6:
            r = "коть уталь"
        elif cat.age < 8:
            r = "кот ушёль"
        elif cat.age < 10:
            r = "кот спац"

        message = f'{cat.name}{cat.age}, {r}'
        print(message)

Game()
