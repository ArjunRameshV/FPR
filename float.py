import os
os.system("clear")
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
			num=float(input("Enter a Decimal Number : "))
			sign=str(int(int(num)*-1>0))
			d=bin(int(num)).split('b')[1]
			t=int(str(num).split('.')[1])
			if(len(d)>10):
				print("too big input for half precision")
			else:
				s=''
				l=len(str(t))
				for i in range(13):
					t*=2
					s+=str(t//(10**l))
					t=t%(10**l)
				num1=len(d)
				# print(d+"."+s)
				d=d+s
				num2=d.find("1")+1
				t=num1-num2
				# print(d[:num2]+"."+d[num2:],t)
				d=d[d.find("1")+1:]
				x=bin(15+t).split("b")[1] #Half Precision (max exp of bin size 5)
				if(len(x)<5):
					ans=sign+" 0"+x+" "+d[2:12]
				else:
					ans=sign+" "+x+" "+d[2:12]
				print(ans)

		elif(a==2):
			print("Floating point to Decimal")			
			num=input("Enter a binary half precision (s e m)format Number : ")
			# num=num.split(" ")
			if(len(num)==16):#half precision
				print("Correct")
				sign=num[0]
				exp=num[1:6]
				man=num[7:]		
				print(sign,exp,man)
				exp=int(exp,2)
				exp=exp-15 #half Precision
				print(sign,exp,man)
				ans=''
				if(sign=='1'):
					ans="-"
				temp=int('1'+man[0])
			else:
				print("Wrong format")
		elif(a==3):
			# os.system("clear")
			break
		else:
			print("Wrong input")
	except(ValueError):
		print("Unknown Format")