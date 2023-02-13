# Outputs if inputted number is one digit or not

def main():
    num = str(abs(int(input('Enter your number: '))))

    if len(num) == 1:
        print('This is a one digit number')
    else:
        print('This number has more than one digit')

main()