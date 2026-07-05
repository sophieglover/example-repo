name = input("What is your name?")

age = int(input("How old are you?"))

hair_colour = input("What colour is your hair?")

eye_colour = input("What colour are your eyes?")

class Adult():
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(f"{self.name}, you are old enough to drive")

class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        print(f"{self.name}, you are NOT old enough to drive")


if age >= 18:
    age_class = Adult(name, age, hair_colour, eye_colour)

else:
    age_class = Child(name, age, hair_colour, eye_colour)

age_class.can_drive()

