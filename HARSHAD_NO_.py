num=int(input('enter the num'))
rem=0
sum=0
n=num
while num>0:
	rem=num%10
	sum=sum+rem
	num=num//10
if(n%sum==0):
	print(str(n)+'is a harsad num')
else:
	print(str(n)+'is not a harsad num')