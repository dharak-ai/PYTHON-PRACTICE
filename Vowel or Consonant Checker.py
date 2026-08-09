# vowel and consonant checker

char = input("Enter a character:")
if char in 'aeiouAEIOU':
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")