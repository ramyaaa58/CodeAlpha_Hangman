import random

easy_words = ["cat", "dog", "pen", "sun", "hat"]
medium_words = ["apple", "tiger", "chair", "robot", "house"]
hard_words = ["python", "program", "network", "science", "complex"]

print("Welcome to Advanced Hangman")
print("Select Difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    words = easy_words
    limit = 8
elif choice == "2":
    words = medium_words
    limit = 6
else:
    words = hard_words
    limit = 5

word = random.choice(words)

guessed = []
wrong = 0
display = ["_"] * len(word)

hint_used = False

print("\nGame Started\n")

while wrong < limit and "_" in display:
    print("Word:", " ".join(display))
    print("Guessed letters:", ", ".join(guessed))
    print("Remaining chances:", limit - wrong)

    option = input("Enter a letter or type 'hint': ").lower()

    if option == "hint":
        if not hint_used:
            remaining_indexes = []
            for i in range(len(word)):
                if display[i] == "_":
                    remaining_indexes.append(i)

            reveal = random.choice(remaining_indexes)
            display[reveal] = word[reveal]
            hint_used = True
            print("A letter has been revealed\n")
        else:
            print("Hint already used\n")
        continue

    if option in guessed:
        print("You already guessed that letter\n")
        continue

    guessed.append(option)

    if option in word:
        for i in range(len(word)):
            if word[i] == option:
                display[i] = option
        print("Correct guess\n")
    else:
        wrong += 1
        print("Wrong guess\n")

if "_" not in display:
    print("You won! The word is:", word)
else:
    print("You lost! The word was:", word)

again = input("\nDo you want to play again? (yes/no): ").lower()

if again == "yes":
    print("Please run the program again to restart")
else:
    print("Thank you for playing")