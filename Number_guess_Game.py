import  random
c=1
attempt = 5
while c<=attempt:
    a=random.randint(1,10)
    b=int(input('Guess number between 1 to 10:'))
    print(f'Computer thinked:{a}')
    if a==b:
        print('Nice! you won the game')
        print('you guessed correct')
    else:
        print('you lost this turn')
        c+=1
        print('make another one try')