# print("Quater Precision Floating point Representation")
print("Half Precision Floating point Representation")
# print("Single Precision Floating point Representation")
# print("Double Precision Floating point Representation")
print("Enter chioices :-\n 1.Decimal to Floation Point\n 2.Floating point to Decimal\n 3.Exit")
while(True):
	try:
		a=int(input("Choice :- "))
		if(a==1):
			print("Decimal to Floating point ")
			num=float(input("Enter a Decimal Number :-"))
			d=bin(int(num)).split('b')[1]
			f=int(str(num).split('.')[1])
			print(num,",",d,f)

		elif(a==2):
			print("Floating point to Decimal")			
			num=input("Enter a binary half precision (s e m)format Number :-")
			# num=num.split(" ")
			if(len(num)==16):#half precision
				print("Correct")
				
			else:
				print("Wrong format")
		elif(a==3):
			break
		else:
			print("Wrong input")
	except(ValueError):
		print("Unknown Format")
