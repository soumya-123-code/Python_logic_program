string="python"
length=len(string)
# print(length);


for row in range(length):
	# print(row)
	for col in range(row+1):
		print (string[col],end="")
	print()
