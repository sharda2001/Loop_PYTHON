num=int(input('enter the number'))
s=0
temp=num
while temp>0:
	digit=temp%10
	s+=digit**3
	temp//=10
if num==s:
	print(num,' armstrong number')
else:
	print(num,'not armstrong number')