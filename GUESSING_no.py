num=10
i=1
while i<=10:
	user=int (input("enter your number"))
	if user==10:
		print("guess is right")
		break
	elif user>num:
		print("guess is large")
	else:
		print(" guess is small")
		i=i+1


# num=5
# i=0
# while i<=5:
# 	user=int(input("enter the number"))
# 	if user==5:
# 		print("guessing is right")
# 		break
# 	else:
# 		print("your guess is wrong")
# 		i=i+1