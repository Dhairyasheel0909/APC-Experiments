li = []

for i in range(10):
    num = int(input("Enter number: "))
    li.append(num)

total = 0

for num in li:
    total = total + num

average = total / 10

print("Sum:", total)
print("Average:", average)
