s = input("Please type in a string: ")
v = ['a', 'e', 'o']
for vowel in v:
    if vowel in input:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
