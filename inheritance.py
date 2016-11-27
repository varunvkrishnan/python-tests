class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("last_name : "+self.last_name)
        print ("eye_color : "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        print ("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys

    def show_info(self):
        print ("last_name : "+self.last_name)
        print ("eye_color : "+self.eye_color)
        print ("num_of_toys : "+str(self.num_of_toys))

billy_cyrus = Parent("Cyrus","blue")
print(billy_cyrus.last_name)
billy_cyrus.show_info()

miley_cyrus = Child("Cyrus","Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.num_of_toys)
miley_cyrus.show_info()
