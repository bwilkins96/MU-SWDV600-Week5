# Prints if an inputted grade is passing

def main():
    grade = float(input('Enter your course grade (out of 100): '))

    if grade < 0 or grade > 100:
        print('The entered value is invalid')
    elif grade >= 90:
        print('You passed the class with honors!')
    elif grade >= 60:
        print('You passed the class')
    else:
        print('I\'m sorry, you need to retake the class')

main()