# Prints the min and max values entered by a user
# indefinite loop using a sentinel value to quit

def main():
    next_val = float(input('Enter a number (negative to quit): '))
    min_val = next_val
    max_val = next_val

    while next_val >= 0:
        if next_val < min_val:
            min_val = next_val
        
        if next_val > max_val:
            max_val = next_val

        next_val = float(input('Enter a number (negative to quit): '))

    if min_val < 0:
        print('\nNo values entered')
    else:
        print(f'\nMin value: {min_val}, Max value: {max_val}')

main()