class Student:
    
    school = 'Balvikas'
    
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #Instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    #Class Method
    @classmethod
    def getschool(cls):
        return cls.school
    
    # Static Method
    @staticmethod
    def info():
        print("This is student class")

s1 = Student(34, 23, 12)
s2 = Student(89, 43, 12)

print(s2.avg())
print(Student.getschool())

Student.info()