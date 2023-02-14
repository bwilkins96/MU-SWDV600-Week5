# Prints the character of a string at an index
# Exception handling using try, except blocks

def main():
    try:
        inputString = input("Enter your String: ")
        characterIndex = int(input("Enter the index of the character you want: "))

        character = inputString[characterIndex]
        print( "The character is", character )
    except IndexError:
        print('The string does not have that many characters')
    except:
        print('Invalid input')

main()