age_per1 = int(input("Please type in the age of the first person: "))
age_per2 = int(input("Please type in the age of the second person: "))


if age_per1 > age_per2:
    print(f"The older age is: {age_per1}")
elif age_per1 < age_per2:
    print(f"The older age is: {age_per2}")
else:
    print("Both people are the same age!")
