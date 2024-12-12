word = input("Please enter a word: ")

b = True
for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        b = False
        break
if b == True:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
