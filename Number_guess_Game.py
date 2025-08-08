import  random
c=1
attempt = 5
print(f'You have {attempt} attempts to guess the secret number.')
while c<=attempt:
    a=random.randint(1,10)
    if c>=2:
        print(f'You have left {(attempt - c)+1} attempts to guess the secret number.')
    try:
        b=int(input('Guess number between 1 to 10:'))
        print(f'Computer thinked:{a}')
        if a == b:
            print('Nice! you won the game')
            print('you guessed correct')
            break
        else:
            print('you lost this turn')
            c += 1
            print('make another one try')
    except ValueError :
        print('Please enter a number.')

