class SchoolMember(object):#定义学校
    member=0#默认成员为0个
    amount=0#默认学费为0元
    def __init__(self,name,age,sex):#构造函数，定义父类的属性
        self.name=name
        self.age=age
        self.sex=sex
        self.enroll()#调用注册的函数

    def enroll(self):
        '''注册'''
        print("just is enrolled a new school member[%s]"% self.name)
        SchoolMember.member+=1#每注册一名成员，成员数量加1
    def tell(self):#用来获取成员的属性
        print("-----info:%s----"%self.name)
        for k,v in self.__dict__.items():#用字典的形式来获取成员的属性
            print("\t",k,v)
        print("------end-------")
class Teacher(SchoolMember):#定义一个老师的类，并且继承这个学校
    def __init__(self,name,age,sex,salary,course):#继承父类并且重构
        SchoolMember.__init__(self,name,age,sex)#继承父类
        self.salary=salary
        self.course=course
    def teaching(self):
        print("the teacher is [%s] and his course is [%s]"% (self.name,self.course))

class Student(SchoolMember):#定义一个学生的类来继承父类
    def __init__(self,name,age,sex,course,tuition):
        SchoolMember.__init__(self,name,age,sex)
        self.course=course
        self.tuition=tuition
    def pay_tuition(self,amount):#学费
        print("student %s has justed paied %s"%(self.name,amount))
        self.amount+=amount


t1=Teacher("xiangshucai",54,"F",4500,"physical")
s1=Student("xiangxiao",24,"F","python",6500)
s2=Student("liuhaimei",23,"F","python15",11000)
t1.teaching()
t1.tell()
s1.tell()