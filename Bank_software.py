import datetime
import os
import os
import datetime

print('🏦This is a Digital bank.')


def greet_start(fx):
    def wraper(*args, **kwargs):
        print('Welcome back again!')
        result= fx(*args, **kwargs,)
        return result
    return wraper

def greet_end(fx):
    def wraper(*args, **kwargs):
        result= fx(*args, **kwargs,)
        print('Thanks for using Bank software!')
        return result
    return wraper

@greet_end
def deposite(username):
    print('Enter an amount that you want to deposit')
    dep_amnt = get_input(100, 100000)
    path = os.getcwd()
    full_path = os.path.join(path, username + '.txt')

    with open(full_path, 'r') as f:
        data = f.readlines()
        stred_amount = data[-1].strip().split('=')[1]
        stored_amount = int(stred_amount.split()[0])

    new_balance = dep_amnt + stored_amount
    transaction = f'amount={dep_amnt} = deposited at {datetime.datetime.now()}\n'
    balance_line = f'amount={new_balance} = current balance\n'

    with open(full_path, 'a') as e:
        e.write(transaction)
        e.write(balance_line)

    print(f'\033[92m✔ {dep_amnt} is deposited successfully.\033[0m')

@greet_end
def withdraw(username):
    path = os.getcwd()
    full_path = os.path.join(path, username + '.txt')

    try:
        with open(full_path, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print("❌ No account found for this user.")
        return

    stred_amount = data[-1].strip().split('=')[1]
    stored_amount = int(stred_amount.split()[0])

    while True:
        print('🏧 Enter an amount that you want to withdraw')
        with_amnt = get_input(100, 100000)

        if 0 < with_amnt <= stored_amount:
            new_balance = stored_amount - with_amnt
            transaction = f'amount={with_amnt} = withdrawn at {datetime.datetime.now()}\n'
            balance_line = f'amount={new_balance} = current balance\n'

            with open(full_path, 'a') as f:
                f.write(transaction)
                f.write(balance_line)

            print(f'✅\033[93m {with_amnt} withdrawn successfully.\033[0m')
            break
        else:
            print('❌\033[91mInvalid amount. You entered more than your balance or less than 0.\033[0m')


@greet_end
def show(username):
    path = os.getcwd()
    full_path = os.path.join(path,username+'.txt')
    with open(full_path,'r') as f:
        data=f.readlines()
        stored_username=data[0]
        stored_balance=data[-1].strip().split('=')[1]
        print(stored_username)
        print(f'\033[94m💰 youre current balans is {stored_balance}\033[0m')


import os
import datetime


def acount_creat():
    print('🏦 Creating a new Bank account.')

    while True:
        name = input('Enter your username: ')
        path = os.getcwd()
        full_path = os.path.join(path, name + '.txt')

        if not os.path.exists(full_path):
            break
        else:
            print('❌ Username already exists. Try another username.\n')

    pass_user = input('Create a strong password: ')

    while True:
        try:
            amount_user = int(input('Enter the amount you want to deposit in this account: '))
            break
        except ValueError:
            print('❌ Invalid input. Enter the amount in numbers.')

    print(f'\n✅ Account created for username: {name}')
    print(f'🔐 Password: {pass_user}')
    print(f'💰 Amount of {amount_user} deposited.')

    with open(full_path, 'w') as user_data:
        user_data.write(f'username={name}\n')
        user_data.write(f'password={pass_user}\n')
        user_data.write(f'amount={amount_user} = deposited at {datetime.datetime.now()}\n')

@greet_start
def login_account():


    name = str(input('Enter your username:'))
    pass_user= str(input('Enter your pasword:'))
    try:
        path = os.getcwd()
        full_path = os.path.join(path,name+'.txt')
        with open(full_path,'r') as file:
            data = file.readlines()
            stored_username=data[0].strip().split('=')[1]
            stored_password=data[1].strip().split('=')[1]
            if stored_username == name and pass_user == stored_password:
                print('You have sucssesfully logined to your acount.')
                print('')
                print('If you want to check your balance, press 1')
                print('If you want to deposite money, press 2')
                print('If you want to withdraw money, press 3')
                print('If you want your Bank statment than press 4')
                b = get_input(1, 4)
                if b == 1:
                    show(name)
                elif b == 2:
                    deposite(name)
                elif b == 3:
                    withdraw(name)
                elif b == 4:
                    get_trn_list(name)
            else:
                print('your username or password is incorect')
                print('if you want to make another try, press 1')
                print('if you want to make new acount, press 2')
                c = get_input(1, 2)
                if c == 1:
                    login_account()
                else:
                    acount_creat()



    except FileNotFoundError:
        print('invilid credientals or account does not found')
        print('if you does not have acount, you have to make new one.')
        print('if you want to make another try, press 1')
        print('if you want to make new acount, press 2')
        c = get_input(1, 2)
        if c == 1:
            login_account()
        else:
            acount_creat()

@greet_end
def get_trn_list(username):
    path = os.getcwd()
    full_path = os.path.join(path, username + '.txt')

    try:
        with open(full_path, 'r') as f:
            data = f.readlines()

        print("\n📋 Transaction History (Most Recent First):")
        print("-" * 50)

        for line in reversed(data[2:]):  # Skip username and password
            clean_line = line.strip()

            # Only include lines that are actual transactions
            if 'deposited at' not in clean_line and 'withdrawn at' not in clean_line:
                continue

            # Set action and color
            if 'deposited' in clean_line:
                action = 'Deposit'
                color = '\033[92m'  # Green
            elif 'withdrawn' in clean_line or 'withdrawed' in clean_line:
                action = 'Withdraw'
                color = '\033[91m'  # Red
            else:
                action = 'Other'
                color = '\033[0m'

            # Extract amount and timestamp
            parts = clean_line.split('=')
            if len(parts) >= 3:
                amount = parts[1].strip()
                timestamp = parts[2].replace('deposited at', '').replace('withdrawed at', '').replace('withdrawn at', '').strip()
                print(f"{color}{action:<10} | Amount: {amount:<8} | Time: {timestamp}\033[0m")
            else:
                print(clean_line)

    except FileNotFoundError:
        print("❌ No transaction file found for this user.")




def get_input(a, b):
    while True:
        try:
            x = int(input(' '))
            if a <= x <= b:
                return x
            else:
                print(f'❌ Invalid input. Enter a number between {a} to {b}')
        except ValueError:
            print(f'❌ Invalid input. Press a number between {a} to {b}')



print('For login press 1')
print('If you do not have account, press 2 for sign up')
k=get_input(1, 2)
if k == 1:
    login_account()
elif k == 2:
    acount_creat()
