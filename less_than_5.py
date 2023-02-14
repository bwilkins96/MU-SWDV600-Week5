# Counts the number of inputted words that have less than 5 characters
# indefinite loop using a sentinel value to quit

def main():
    count = 0
    inputWord = input("Enter a word ('quit' to stop): ")

    while inputWord != 'quit':
        if len( inputWord ) < 5:
            count = count + 1
            
        inputWord = input("Enter a word ('quit' to stop): ")

    print("\nYou entered {0} words with less than 5 characters".format(count))

main()