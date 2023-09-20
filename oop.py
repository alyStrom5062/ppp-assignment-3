class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2

class SebulPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
#    Encapsulation

#       Defining variables inside of the Podracer class, and then calling them inside of other classes using function paramaters can be considered 
#       encapsulation. These variables could be defined outside the classes and the nested functions, but they are declared inside the nested 
#       functions, which hides information.

#    Abstraction

#       Only the data relevant to the program is provides. Abstraction is the process of removing all additional traits which are not needed. This 
#       is to reduce complexity of a program and to increase efficiney, especially for older, less powerful computers to be able to run a program. This
#       one did not apply the same way the others did because price was irrelevant to what the functions performed.

#    Inheritance

#       In this assignment, examples of inheritance are Podracer being a seperate class from Anakin and Sebul's own specific podracers. Their specific 
#       podracers are derived from the parent podracer class, which describes what a podracer is. The indivifual owned podracers then can have different
#       attributes such as price, condition, and max speed.

#    Polymorphism

#       There are not polymorphic classes in this excersize. Polymorphism can mean several things and from my understand, they do not apply to these
#       objects in this assignment.


# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

#   I personally prefer functional programming, but with programs that describe multiple similar things that hold specific attributes, OOP 
#   is much more effifienct and sensible. 

# How in particular did Object Oriented Programming assist in the solving of this problem?

#   OOP inheritence helped with this problem. Even just having two podracers in this problem made it benefit from using OOP. In real applications, there 
#   are hundreads of thoasand, even millions, of objects. Functional programing is good for running something through a function. OOP is good for programming
#   that contains objects which then do things.