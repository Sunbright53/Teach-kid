import time

def ad_login():
    add_user = input("Username: ")
    add_pass = input("Password: ")
    def iflog():
        if add_user == "admin" and add_pass == "1111":
            print (f'กำลังเข้าสู่ระบบ')
            for i in range(10,0,-1):
                print (i)
                time.sleep(1)
            print(f'เข้าสู่ระบบ')
        else:
            print (f'คุณกรอกรหัสไม่ถูกต้อง')
    iflog()

ad_login()
