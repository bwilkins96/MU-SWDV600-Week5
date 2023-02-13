# prints the inputted word that comes first alphabetically
# sequential processing version

def main():
    num_words = int(input('Enter the number of words: '))
    
    first_word = input('\nEnter word 1: ').lower()
    for i in range(2, num_words+1):
        word = input(f'Enter word {i}: ').lower()

        if word < first_word:
            first_word = word

    print(f'\nThe first word alphabetically is {first_word}')

main()