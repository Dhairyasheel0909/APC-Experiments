num = int(input("Enter a number: "))

root = -1


for i in range(1, num + 1):
    if i * i == num:
        root = i
       

else:
   
    if root < 2:
        print(root, "is not prime.")
    else:
        prime = True
        for j in range(2, root):
            if root % j == 0:
                prime = False
                

        if prime:
            print(root, "is a prime number.")
        else:
            print(root, "is not a prime number.")