import random

class Die:
    """
    a n-sided object for casting
    """

    def __init__(self, sides=6):
        """
        Parameters:
        - sides - the number of sides of an object
        """
        self.sides = sides
       
    def cast_me(self):
        return random.randrange(1,self.sides)


