# Prints the number of entered strings that start and end with the same character
# Strings must be at least 5 characters long
def get_string():
    while True:
        string = input('Enter a word (<enter> to quit): ')
        if len(string) >= 5 or not string:
            break
        print('Word must be at least 5 characters long')
    
    return string

def main():
    next_str = get_string()
    
    count = 0
    while next_str:
        if next_str[0] == next_str[-1]:
            count+=1
        
        next_str = get_string()
    
    print(f'\nYou entered {count} words with the same first and last character!')

main()