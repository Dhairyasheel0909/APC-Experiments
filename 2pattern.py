n =int(input("Enter a number"))

for i in range(n+1,0,-1):
	for j in range(65,65 + i):
        	print(chr(j), end="")
	print()