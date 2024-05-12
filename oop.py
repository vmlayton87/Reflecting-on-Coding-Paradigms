'''
Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.

Define a repair() method that will update the condition of the podracer to "repaired".

Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.

Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

'''
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    def repair(self):
        self.condition = 'repaired'
        return self.condition
    
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    def boost(self):
        self.max_speed *= 2
        return self.max_speed
    
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    def flame_jet(self, opponent):
        opponent.condition = 'thrashed'
        return opponent.condition

pod_one = Podracer(20,'thrashed', 200)
print("pod one condition:", pod_one.condition)
print("pod one repaired?", pod_one.repair())

pod_two = AnakinsPod(20, 'perfect', 500)
print("pod two max speed:", pod_two.max_speed)
print("pod two with boost", pod_two.boost())

pod_three = SebulbasPod(20, 'perfect', 800)
print("pod two's condition before flame jet:", pod_two.condition)
print("pod three flame jets pod two:", pod_three.flame_jet(pod_two))
print("pod two's condition after flame jet:", pod_two.condition)
'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    Encapsulation: I am able to create my own instances of each class that was created without having to define the mehtods and attributes every time.
    
    Abstraction: I am able to call methods from the classes without neccessarily knowing what the process is such as the boost method in pod_two. I can call boost but I don't see the work behind it when I call it. 

    Inheritance : creates one main class called Podracer, then uses others to inherit from the Podracer.
    
    Polymorphism: There is no polymorphism here since there are no functions or methods that are named the same with different definitions/purposes.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    Not for this problem. Using OOP makes sense since there are multiple items that use the same methods/attributes as another. Helps with DRY.

How in particular did Object Oriented Programming assist in the solving of this problem?
    Being able to keep the code DRY by implementing inheritence from classes.

'''