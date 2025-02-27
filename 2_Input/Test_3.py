


import time

name1 = input("กรุณาป้อนชื่อลูกค้า: ")
band_phone1 = input("ยี่ห้อมือถือ" + " ")
price_phone1 = float(input("ราคามือถือ" + " "))
band_phone2 = input("ยี่ห้อมือถือ" + " ")
price_phone2 = float(input("ราคามือถือ" + " "))

total_price = price_phone1 + price_phone2
vat = total_price * 0.07
total_all = total_price + vat

print("คุณ", name1)
print("สินค้าที่ 1", band_phone1, "ราคา", price_phone1)
print("สินค้าที่ 2", band_phone2, "ราคา", price_phone2)
print("ราคาทั้งหมดที่ต้องชำระรวมภาษี", total_all)

print("\nกรุณาชำระเงิน...")
time.sleep(5)
print("ขอบคุณที่ใช้บริการ!")


