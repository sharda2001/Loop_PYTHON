n=int(input('enter the number'))
tem=n
s=0
while tem>0:
	i=1
	f=1
	digit=tem%10
	while i<=digit:
		f=f*i
		i+=1
	s=s+f
	tem=tem//10
if s==n:
	print(n,'strong number')
else:
	print(n,'not strong number')