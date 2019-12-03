class Employee:
	increment=3
	no_of_employee=0
	def __init__(self,fname,lname,salary):
		self.fname=fname
		self.lname=lname
		self.salary=salary
		self.increment=2
		Employee.no_of_employee+=1

	def increase(self):
		self.salary=int(self.salary*Employee.increment)

	@classmethod
	def change_increment(cls,amount):
		cls.increment=amount


harry=Employee("harry","jakson",2000)
print(harry.salary)
print(Employee.increment)
Employee.change_increment(4)
harry.increase()

print(harry.salary)
