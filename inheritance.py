class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("last name: " + self.last_name)
        print("eye color: " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys

    def show_info(self):
        print("last name: " + self.last_name)
        print("eye color: " + self.eye_color)
        print("number of toys: " + str(self.num_of_toys))


## demo code
billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.eye_color)

#billy_cyrus.show_info()

milly_cyrus = Child("Cyrus", "blus", 15)
print(milly_cyrus.eye_color)
print(milly_cyrus.num_of_toys)
milly_cyrus.show_info()
