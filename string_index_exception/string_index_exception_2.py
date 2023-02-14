# Prints the character of a string at an index
# Exception handling using conditionals

def main():
    inputString = input("Enter your String: ")
    characterIndex = int(input("Enter the index of the character you want: "))

    if characterIndex >= len(inputString):
        print('The string does not have that many characters')
    else:
        character = inputString[characterIndex]
        print( "The character is", character )

main()