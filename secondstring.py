# This program asks the user to input a string.
# The string then outputs every second letter in reverse order.
# Author: Jonathon Grealish

secondString = "The quick brown fox jumps over the lazy dog."
secondArray = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

for i in range(len(secondString)):
    if i == 0:
        print([""])
    else:
        print(secondString)

# The quick brown fox jumps over the lazy dog.