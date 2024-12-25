import statistics

user_list = []

print("Welcome to the Sorted List Builder!")
print("Enter numbers to build a list. Enter 0 to stop.")

while True:
    try:
        user_input = input("Enter a number: ").strip()
        number = int(user_input)
        
        if number == 0: 
            print("\nFinal List Summary:")
            print(f"Current List: {user_list}")
            print(f"Sorted List (Ascending): {sorted(user_list)}")
            print(f"Sorted List (Descending): {sorted(user_list, reverse=True)}")
            if user_list:
                mean = statistics.mean(user_list)
                median = statistics.median(user_list)
                print(f"Mean: {mean:.2f}")
                print(f"Median: {median}")
            save_option = input("\nDo you want to save the list to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                with open("user_list.txt", "w") as file:
                    file.write(f"Current List: {user_list}\n")
                    file.write(f"Sorted List (Ascending): {sorted(user_list)}\n")
                    file.write(f"Sorted List (Descending): {sorted(user_list, reverse=True)}\n")
                    if user_list:
                        file.write(f"Mean: {mean:.2f}\n")
                        file.write(f"Median: {median}\n")
                print("List saved to 'user_list.txt'.")
            break
        user_list.append(number)
        print(f"Current List: {user_list}")
        print(f"Sorted List (Ascending): {sorted(user_list)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

