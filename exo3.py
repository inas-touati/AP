ta = float(input("Total amount: "))
nb_items = int(input("Number of items: "))
day = input("Day of the week: ")
dis = ta

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    dis -= ta * (10 / 100)
elif day in ["Saturday", "Sunday"]:
    dis -= ta * (20 / 100)
if nb_items > 5:
    dis -= ta * (5 / 100)
print(f"Total price after discount: {dis:.1f} dinars")
