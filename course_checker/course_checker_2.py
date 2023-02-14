# Prints if an inputted grade is passing
# Uses a validation loop to check inputed grade

def main():
    while True:
        grade = float(input('Enter your course grade (out of 100): '))

        if grade >= 0 and grade <= 100:
            break
        else:
            print('The entered value is invalid. Please try again.\n')

    if grade >= 90:
        print('You passed the class with honors!')
    elif grade >= 60:
        print('You passed the class')
    else:
        print('I\'m sorry, you need to retake the class')

main()