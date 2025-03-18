import time

while True:
    user = input(f'Please enter your username:')
    passw = input(f'Please enter your password:')
    if user == f'Admin' and passw == f'Mi_56_loy':
        print(f'Logging in')
        for i in range (5, 0, -1):
            print(i)
            time.sleep(1)
        print(f'Welcome to the world')
        break
    else:
        print(f'Wrong password')
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        print(f'------------------')
