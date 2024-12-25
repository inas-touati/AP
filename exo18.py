import os

numbers = [1, 2, 3, 4, 5]

def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Search for an element")
    print("8. Save the list to a file")
    print("9. Load a list from a file")
    print("10. Quit")

def interactive_program():
    global numbers
    print(f"Initial List: {numbers}")
    while True:
        display_menu()
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue
        
        if option == 1:
            try:
                value = int(input("Enter value to append: "))
                numbers.append(value)
                print(f"Updated List: {numbers}")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif option == 2:
            try:
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index to insert at: "))
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                    print(f"Updated List: {numbers}")
                else:
                    print("Index out of range.")
            except ValueError:
                print("Invalid input. Please enter integers only.")

        elif option == 3:
            try:
                index = int(input("Enter index to pop (or leave blank to pop last): ") or len(numbers) - 1)
                if 0 <= index < len(numbers):
                    removed = numbers.pop(index)
                    print(f"Removed element: {removed}")
                    print(f"Updated List: {numbers}")
                else:
                    print("Index out of range.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")
            except IndexError:
                print("Cannot pop from an empty list.")

        elif option == 4:
            try:
                value = int(input("Enter value to remove: "))
                numbers.remove(value)
                print(f"Updated List: {numbers}")
            except ValueError:
                print("Value not found in the list.")

        elif option == 5:
            numbers.sort()
            print(f"List sorted: {numbers}")

        elif option == 6:
            numbers.reverse()
            print(f"List reversed: {numbers}")

        elif option == 7:
            try:
                value = int(input("Enter value to search for: "))
                if value in numbers:
                    index = numbers.index(value)
                    print(f"Value {value} found at index {index}.")
                else:
                    print(f"Value {value} not found in the list.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif option == 8:
            file_name = input("Enter file name to save the list: ")
            try:
                with open(file_name, "w") as file:
                    file.write(",".join(map(str, numbers)))
                print(f"List saved to {file_name}.")
            except Exception as e:
                print(f"Error saving the list: {e}")

        elif option == 9:
            # Load a list from a file
            file_name = input("Enter file name to load the list from: ")
            try:
                if os.path.exists(file_name):
                    with open(file_name, "r") as file:
                        content = file.read().strip()
                        numbers = list(map(int, content.split(",")))
                    print(f"List loaded from {file_name}: {numbers}")
                else:
                    print("File not found.")
            except Exception as e:
                print(f"Error loading the list: {e}")

        elif option == 10:
            # Quit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 10.")

interactive_program()
