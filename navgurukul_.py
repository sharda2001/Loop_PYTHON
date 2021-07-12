i=1
while i<=100:
	if i%3==0:
		print(i,'nav')
	elif i%7==0:
		print(i,'gurukul')
	elif i%3==0 or i%7==0:
		print(i,'navgurukul')
	else:
			print(i)
	i=i+1