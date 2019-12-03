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
	def from_str(cls, emp_string):
		fname, lname, salary = emp_string.split("-")
		return cls(fname, lname, salary)

	@staticmethod
	def isopen(day):
		if day=="sunday":
			return False
		else:
			return True

soumya=Employee("soumya","nayak","4000")
print(soumya.isopen('sunday')) #help of instanace
print(Employee.isopen('sunday'))   #help of class


