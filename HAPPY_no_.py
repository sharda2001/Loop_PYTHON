num=int(input('enter number'))
num2=num
s=0
while s!=1 and s!=4:
	s=0
	while num2!=0:
		r=int(num2%10)
		s=s+r*r
		num2=num2//10
	num2=s
if s==1:
	print(num,'is happy')
else:
	print(num,'is unhappy')