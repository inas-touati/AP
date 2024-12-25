
numbers = [1, 2, 3, 4, 5]

def get_user_input():
    while True:
        try:

            index = int(input("Enter index : "))
            if index == -1:
                return index, None

            new_value = int(input("Enter new value: "))

            return index, new_value
        except ValueError:
            print("Invalid input. Please enter integers only.")
while True:
    index, new_value = get_user_input()
    if index == -1:
        break
    if 0 <= index < len(numbers):
        numbers[index] = new_value
        print(numbers)
    else:
        print("Invalid index. Please try again.")

print("Program terminated.")
