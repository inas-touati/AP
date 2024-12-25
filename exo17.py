
numbers = []
shoe_sizes = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(2)
numbers.append(5)

for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)


print(f"Numbers List: {numbers}")
print(f"Shoe Sizes List: {shoe_sizes}")


numbers.append(3)  
if len(set(numbers)) != len(numbers):  
    numbers = list(set(numbers))  
    numbers.sort()  

print(f"Updated Numbers List: {numbers}")


combined_list = numbers + shoe_sizes
print(f"Combined List: {combined_list}")
