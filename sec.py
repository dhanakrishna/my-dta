def sec(x):
	s = 0
	a=b= float('-inf')
	for y in x:
		s +=1
		if y > b :
			if y >= a:
				a,b = y , a
			else :
				b = y
	return b if s >= 2 else None




w=sec([44,55,22,66,99,88,77,445,66,2,5,5,2,5,44,45,2,5,56,4545,6565,6,21212,6])
print(w)
