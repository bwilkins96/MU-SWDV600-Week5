# Recommends a gold club based on inputed data

def main():
    print('Welcome to the Golf Club Helper!')
    print('Tell me your situation, and I\'ll recommend a club\n')

    on_green = input('Did you hit your ball on the green (y/n)? ')[0]
    ball_dist = int(input('How far is the ball from the hole (in yards)? '))
    
    recommendation = ''
    if on_green == 'y':
        recommendation = 'Putter'
    elif ball_dist >= 200:
        recommendation = 'Driver'
    elif ball_dist < 200 and ball_dist >= 140:
        recommendation = '5-Iron'
    elif ball_dist < 140 and ball_dist >= 100:
        recommendation = '9-Iron'
    else:
        recommendation = 'Pitching Wedge'
    
    print('\nI recommend using your {}'.format(recommendation))

main()