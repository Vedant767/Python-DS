class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # We can create a object of inner class in init function
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
        

    class Laptop:
        
        def __init__(self):
            self.brand = "Asus"
            self.cpu = "i5"
            self.ram = "4"
            
        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Ved", 1)
s2 = Student("Ram", 2)

#Two ways to call a function of a class
s1.show()
Student.show(s2)


#Call a variable which is in second class
# print(s2.lap.cpu)

l1= s1.lap
l2= s2.lap
#Id's of object created
# print(id(l1))
# print(id(l2))

#Create a object of inner class outside the class
# l3 = Student.Laptop()
# print(l3.ram)
