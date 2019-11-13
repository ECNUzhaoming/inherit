class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print
        'Member init:%s' % self.name

    def tell(self):
        print
        'Name:%s,Age:%d' % (self.name, self.age),


class Student(Member):
    def __init__(self, name, age, marks):
        Member.__init__(self, name, age)
        self.marks = marks
        print
        'Student init:%s' % self.name

    def tell(self):
        Member.tell(self)
        print
        'Marks:%d' % self.marks


class Teacher(Member):
    def __init__(self, name, age, salary):
        Member.__init__(self, name, age)
        self.salary = salary
        print('Teacher init:%s' % self.name)

    def tell(self):
        Member.tell(self)
        print('Salary:%d' % self.salary)



s = Student('Tom', 20, 80)
t = Teacher('Mrs.Huang', 30, 50000)

members = [s, t]
for mem in members:
    mem.tell()