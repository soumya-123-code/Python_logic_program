n=int(input("enter the no. :"))

if n == 1:
	print("no. is not prime")
else:
	for x in range(2,n):
		if(n%x==0):
			print("no. is not prime")
			break
	else:
			print("no. is prime")