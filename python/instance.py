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


print(Employee.no_of_employee)

harry=Employee('harry','jakson',4000)
print(Employee.no_of_employee)

rohan=Employee('rohan','das',5000)





harry.increase()
print(harry.salary)
print(Employee.no_of_employee)
