num=int(input("enter a number"))
i = 2
while (i<num):
	j=2
	while i>j:
		if i%j==0:
			break
		j+=1
	else:
		print(i)
	i+=1