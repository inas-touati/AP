
nbp = int(input("How many people need a ride? "))
nbt = int(input("How many people fit in one taxi? "))
nbr_taxis = nbp // nbt
r = nbp % nbt
if r == 0:  
    print(f"Number of taxis needed: {nbr_taxis}")
else: 
    print(f"Number of taxis needed: {nbr_taxis + 1}")
