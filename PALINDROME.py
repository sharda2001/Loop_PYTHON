num=int(input('enter the number'))
tem=num
r=0
while num>0:
	digit=num%10
	r=r*10+digit
	num=num//10
if tem==r:
	print('palindrom num')
else:
	print('not palindrom no')