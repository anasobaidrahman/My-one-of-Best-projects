print("THis is BMi software")
w=float(input("Enter weight in kg :"))
h=float(input('Enter hight in meters :'))
bmi=w/h
if bmi < 18.5 :
        print('under weight')
        print("Oh no! May you need health cunsultant.")
        print('Recomendation:You need much care of health')
elif bmi >=18.5 and bmi<=24.9:
        print('healthy')
        print('Good! you have to hold this healh.')
elif bmi>=25 and bmi<=29:
        print('over weight')
        print('You have need 10,000 steps daily.')
elif bmi>=30:
        print('Obesity')
        print('Please take care of your health.')
        print('Long time obesity causes many deadly desease.')

