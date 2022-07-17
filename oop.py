#Prompt 2: Object Oriented Programming
#first, we define a class 'Podracer' which will have max_speed, condition(perfect, trashed, repaired), and price attributes.
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

#next we define a repair() method which will update the condition of the podracer to 'repaired'
    def repair(self):
        self.condition = 'repaired'

#next we will introduce a new class 'AnakinsPod' which inherits from the Podracer class but has a new method 'boost' which multiplies max_speed by 2.
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    def boost(self):
        self.max_speed *= 2

#next, another class 'SebulbasPod' which inherits from the same Podracer class, but has a special method flame_jet() which updates the condition of another podracer to 'trashed'
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)
    def flame_jet(self,other):
        other.condition = 'trashed'


pod = Podracer(100, 'perfect', 100)

pod.repair()
print(pod.condition)

new_pod = AnakinsPod(100, 'perfect', 100)

print(new_pod.condition)

#could not figure out error with this code. 
#this code shows encapsulation and inheritance. the initial podracer class is both encapsulated in the following classes, which also inherit their properties from the parent class.
