# length of the last word

a = input("Enter a string:")
words = a.split()
last_word = words[-1]
length = len(last_word)
print("Length of the last word:", length)