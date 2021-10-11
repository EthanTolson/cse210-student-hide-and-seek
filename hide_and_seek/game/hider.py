import random

# TODO: Define the Hider class here
class Hider:

    def __init__(self):
        self.location = random.randint(1,1000)
        self.distance = [0]
        pass

    def get_hint(self):
        if(self.distance[-1] == 0):
            message = "( ; . ;) You found me!"
        elif(self.distance[-1] > self.distance[-2]):
            message = "( ^ . ^) Getting Colder"
        elif(self.distance[-1] < self.distance[-2]):
            message = "Getting Warmer (> . < )"
        else:
            message = "Why did you try the same guess? (¬‿ ¬)"

        return message

    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)
        pass