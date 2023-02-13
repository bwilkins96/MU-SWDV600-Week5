# prints a message based on the length of an inputted word

def main():
    word = input('Enter your word: ')

    if len(word) > 10:
        print('Maybe consider a more diminutive option?')
    else:
        print('Short and sweet!')

main()