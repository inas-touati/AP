
def get_positive_integer():
    while True:
        try:
            N = int(input("Please enter an integer: "))
            if N <= 0:
                print("The number must be positive. Try again.")
            else:
                return N
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
N = get_positive_integer()
for i in range(-N, N + 1):
    if i != 0:
        print(i)
