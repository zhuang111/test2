class Person:
	#公共属性
	name = ""
	age = ""
	#私有属性	
	__weight = ""
	#构造方法 自动执行
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w
	
	def speak(self):
		print("%s says： %s years old"%(self.name,self.age))

#Define Student 
class Student(Person):
	grade = ""
	
	def __init__(self,n,a,w,g):
		Person.__init__(self,n,a,w)
		self.grade = g
		
	def speak(self):
		print("%s says： %s years old and I am in grade %s"%(self.name,self.age,self.grade))
	
	#使用父类的方法
	def speak_parent(self):
		super(Student,self).speak()
		
#实例化
p = Student("xiaoming","12","50kg","8")
p1 = Person("SS","21","34")
p.speak()
p.speak_parent()
print(p1.__weight)
		