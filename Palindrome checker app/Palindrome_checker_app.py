print("Hi, name a palindrome and i will check if it is correct.")

pal = input("Palindrome: ")
revpal = pal[::-1]

if revpal == pal:
    print("The word", pal, "is a palindrome. Well done.")
elif revpal != pal:
    print("The word", pal, "is not a palindrome.")


