class Bird():
    def __init__(self):
        self.can_fly=True
        self.name="default bird"


    def print_can_fly(self):
        if self.can_fly==True:
            print(self.name,"can fly")
        else:
            print(self.name,"cannot fly")



crow=Bird()
crow.name="crow"
crow.print_can_fly()
penguin=Bird()
penguin.name="penguin"
penguin.can_fly=False
penguin.print_can_fly()
ostrich=Bird()
ostrich.name="ostrich"
ostrich.can_fly=False
ostrich.print_can_fly()
duck=Bird()
duck.name="duck"
duck.can_fly=False
duck.print_can_fly()
