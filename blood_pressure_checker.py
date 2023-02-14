# Prints whether blood pressure is normal, 
# based on inputted systolic and diastolic readings

def main():
    sys_read = int(input('Enter your systolic pressure reading: '))
    dias_read = int(input('Enter your diastolic pressure reading: '))

    if (sys_read >= 80 and sys_read <= 120) and (dias_read >= 60 and dias_read <= 80):
        print('\nYour blood pressure is normal!')
    else:
        print('\nYour blood pressure is NOT normal!')

main()