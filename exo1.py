name = input("Please enter your name: ")
if name == "VIP":
    print("Enjoy the show for free!")
else:
    nb_tickets = int(input("How many tickets would you like to buy? "))
    tc = nb_tickets * 15.50
    print(f"The total cost is {tc}")
    print("Enjoy your tickets!")
