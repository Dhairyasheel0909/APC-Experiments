n = int(input("Enter a number: "))

fact = 1
sum=1
for i in range(1, n + 1):
	
	fact = 1/fact * i
	sum=sum+fact
print(sum)
	
	