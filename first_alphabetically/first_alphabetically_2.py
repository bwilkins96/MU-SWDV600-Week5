# prints the inputted word that comes first alphabetically
# decision tree version

def main():
    word_1 = input('Enter word 1: ').lower()
    word_2 = input('Enter word 2: ').lower()
    word_3 = input('Enter word 3: ').lower()

    if word_1 <= word_2:
        if word_1 <= word_3:
            print(word_1)
        else:
            print(word_3)
    else:
        if word_2 <= word_3:
            print(word_2)
        else:
            print(word_3)

main()