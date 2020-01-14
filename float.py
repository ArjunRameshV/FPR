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
				for i in range(10+5):
					t*=2
					s+=str(t//(10**l))
					t=t%(10**l)
				num1=len(d)
				print("Number ",d+"."+s)
				d=d+s
				num2=d.find("1")+1
				t=num1-num2
				print(t)
				# print(d[:num2]+"."+d[num2:],t)
				d=d[d.find("1")+1:]
				x=bin(15+t).split("b")[1] #Half Precision (max exp of bin size 5)
				if(len(x)<5):
					ans=sign+" 0"+x+" "+d[:10]
				else:
					ans=sign+" "+x+" "+d[:10]
				print(ans)

		elif(a==2):
			print("Floating point to Decimal")
			print("Enter a binary half precision (s e m)format ")			
			num=input("Number : ")
			print(num)
			if(len(num)==16 or len(num)== 18): #half precision
				num=num.replace(" ","")
				ans,fract='',''
				if(num[0]=='1'):
					ans="-"
				exp=num[1:6]
				man="1"+num[6:]
				exp=1+int(exp,2)-15 #half Precision
				print(man[0]+"."+man[1:],exp,"actual ",exp-1)
				if(exp<0):
					for i in range(abs(exp)):
						man="0"+man
					ans=ans+"0"
					fract=man
				else:
					i=0
					while(i<exp):
						ans=ans+man[i]
						i+=1
					man=man[i:]
					fract=man
				n=0
				p=1
				for i in range(len(fract)):
					n=n+int(fract[i])*(1/(2**p))
					p+=1
				print(ans+","+fract)
				print(int(ans,2)+n)
			else:
				print("Wrong format")
		elif(a==3):
			# os.system("clear")
			break
		else:
			print("Wrong input")
		# os.system("clear")
	except(ValueError):
		print("Unknown Format")