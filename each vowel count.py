inputString = input("Enter a String: ")
inputString = inputString.casefold()

vowels = "aeiou"

vowelsdata = {}.fromkeys(vowels, 0)

for character in inputString:
    if character in vowels:
        vowelsdata[character] += 1

for vowel in vowelsdata:
    print(vowels, " =>",vowelsdata[vowel])        