n = [45, 12, 78, 23, 9, 56]

largest = n[0]
smallest = n[0]

for num in n:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
