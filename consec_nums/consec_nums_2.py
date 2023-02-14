# Prints whether inputted numbers can be consecutive if sorted

def main():
    nums = []

    while True:
        num = input('Enter a number (<enter> to finish): ')
        if num:
            nums.append(int(num))
        else:
            break

    nums.sort()

    consecutive = True
    for i in range(len(nums) - 1):
        num_1 = nums[i]
        num_2 = nums[i+1]

        if not (num_1 + 1 == num_2):
            consecutive = False
            break

    if len(nums) == 0:
        print('\nThere were no inputted numbers')
    elif consecutive:
        print('\nThe inputted numbers are consecutive when sorted')
    else:
        print('\nThe inputted numbers are not consecutive when sorted')

main()