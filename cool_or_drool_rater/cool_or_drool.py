# Cool or Drool Movie Rater
# Produces a GUI summarizing the ratings of a movie from a .csv file

from graphics import *

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

    ratingImageName = ''
    ratingText = ''

    if totalRatings < 10:
        ratingImageName = 'tooSoonToRule.gif'
        ratingText = 'Too soon to rule'
    elif coolPct >= 60:
        ratingImageName = 'cool.gif'
        ratingText = 'Certified COOL'
    else:
        ratingImageName = 'drool.gif'
        ratingText = 'Certified DROOL'
    
    print(ratingText)
    
    win = GraphWin('COOL or DROOL rater', 400, 400)
    
    titleText = Text(Point(200, 50), title)
    titleText.draw(win)

    ratingImage = Image(Point(200, 200), ratingImageName)
    ratingImage.draw(win)

    coolPctText = Text(Point(200, 350), f'{coolPct:0.0f}% {ratingText}')
    coolPctText.draw(win)

    while True:
        keyPress = win.checkKey()
        if keyPress == 'Escape': break
    
    win.close()

if __name__ == '__main__':
    main()