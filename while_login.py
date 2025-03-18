import time

while True:
    user = input(f'Please enter your username:')
    passw = input(f'Please enter your password:')
    if user == f'Admin' and passw == f'12345':
        print(f'Logging in')
        for i in range (5, 0, -1):
            print(i)
            time.sleep(1)
        print(f'Welcome to APT Bank Account')
        
        while True:
            de_wi = int(input (f'Select the desired command (press 1. Deposit // press 2. Withdraw):'))
            if de_wi == 1:
                while True:
                    doepo = input(f'Amount to deposit:')
                    if int(doepo) > 0:
                        print(f'The amount is equal to {doepo} baht')
                        break
                    else:
                        print(f'The deposit amount is too small. Please enter again.')                       
                break
            elif de_wi == 2:
                Withdraw = input(f'Amount to withdraw:')
                if int(Withdraw) <= 0:
                    print(f'The withdrawal amount is too small. Please enter again.')
                else:
                    print(f'You withdraw money equal to {Withdraw}')
                    print(f'Withdrawing money')
                    for i in range(3,0,-1):
                        print(i)
                        time.sleep(1)
                    break
            else:
                print(f'Enter the correct number.')
        break
    else:
        print(f'Wrong password')
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        print(f'------------------')
