#create a list of n prime no.

def nextPrime(num):
	while True:
		num+=1
		for i in range(2,num):
			if num%2==0:
				break
			else:
				return num

def primeproducer(N):
	num=1
	count=1
	while (count<=1):
		num=nextPrime(num)
		yield num
		count+=1

N=int(input("How many prime numbers you want to generate ? :"))
l=[x for x in primeproducer(N)]
print(l)