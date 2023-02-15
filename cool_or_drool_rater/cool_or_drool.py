# Cool or Drool Movie Rater
# Produces a GUI summarizing the ratings of a movie from a .csv file

def main():
    movieFile = None

    while True:
        movieFileName = input('Enter the name of the ratings file: ')
        try:
            movieFile = open(movieFileName, 'r')
            break
        except FileNotFoundError:
            print(f'{movieFileName} was not found. Please try again.')

    title = movieFile.readline().split(',')[1].strip()
    totalRatings = 0
    coolRatings = 0

    for line in movieFile:
        ratings = line.split(',')
        
        for rating in ratings:
            totalRatings += 1

            if int(rating) >= 6:
                coolRatings += 1
    
    coolPct = (coolRatings / totalRatings) * 100
    movieFile.close()

    print(f'\nMovie Title: {title}')
    print(f'Total Number of Ratings: {totalRatings}')
    print(f'Cool Percentage: {coolPct:0.2f}%')

    if totalRatings < 10:
        print('Too soon to rule')
    elif coolPct >= 60:
        print('Certified COOL')
    else:
        print('Certified DROOL')

if __name__ == '__main__':
    main()