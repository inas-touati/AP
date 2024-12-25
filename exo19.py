# Initialize an empty set to store unique words
unique_words = set()
total_words = 0

print("Welcome to the Unique Word Counter!")
print("Enter words one at a time. The program ends when you enter a duplicate word.")

while True:
    word = input("Enter a word: ").strip() 
    total_words += 1 
    if word in unique_words:
        print(f"You typed in {len(unique_words)} unique words.")
        print(f"Total words entered: {total_words}")
        print(f"Unique words: {', '.join(sorted(unique_words))}")
        save_option = input("Do you want to save the unique words to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            with open("unique_words.txt", "w") as file:
                file.write("\n".join(sorted(unique_words)))
            print("Unique words saved to 'unique_words.txt'.")
        break
    
    unique_words.add(word) 
