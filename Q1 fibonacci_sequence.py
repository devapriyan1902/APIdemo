#fibonacci sequence

n=int(input("enter the no of fibonacci sequence : "))
n1,n2 = 0,1
temp = 0
fibonacci_no=[]
if n <= 0:
	print("enter correct no")	
elif n == 1 :
	print(n1)	
else:
	while temp<n:
		print(n1)
		n3 = n1 + n2
		fibonacci_no.append(n3)
		n1 = n2
		n2 = n3	
		temp+=1			
	print(fibonacci_no)

#sum of fibonacci sequence
	
total=0
fibonacci_no
for i in range(0,n):
	total=total + fibonacci_no[i]
print("the sum of fibonacci sequence is : ",total)	

no=int(input("enter any number : "))
temp=[]
while i in range(1,no):
	i=(no%i)==0
	temp.append(i)	
	if (no%i)!=0 :
	  continue	
	  i+=1
print ("the number divisible by : ",temp )
