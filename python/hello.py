squares = []
for value in range(1,11): # loop1->value=1,loop2->value=2,loop3->value=3
	square = value**2    #loop1->value=1,square=1,loop2->value=2,square=2,loop3->value=3,suaree=9
	     #loop1->squares=[],loop2->squares=[1],loop3->squares=[1,4]
	squares.append(square)  #loop1->square=1,squares=[1],loop2->square=2,squares=[1,4],loop3->square=9,square=[1,4,9]

print(squares)
	




