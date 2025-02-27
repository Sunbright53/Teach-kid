import csv

def load_data_from_csv(file_path):
    """โหลดข้อมูลสินค้าจากไฟล์ CSV และส่งกลับเป็น list ของ dict"""
    data_list = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # แปลงชื่อคีย์ให้เป็นมาตรฐานและดึงข้อมูลที่ต้องการ
            product = row.get('Product') or row.get('product') or row.get('Product_name') or row.get('product_name') or row.get('Name') or row.get('name')
            price = row.get('Price') or row.get('price')
            store = row.get('Store') or row.get('store') or row.get('Shop') or row.get('shop') or row.get('Website') or row.get('website')
            category = row.get('Category') or row.get('category') or row.get('Type') or row.get('type') or "Uncategorized"
            if product and price and store:               # ตรวจสอบว่ามีข้อมูลสำคัญครบ
                try:
                    price = float(price)                 # แปลงราคาจากข้อความเป็นตัวเลข
                except:
                    continue                             # ข้ามถ้าแปลงไม่ได้ (เช่น ข้อมูลไม่ใช่ตัวเลข)
                data_list.append({
                    "product": product,
                    "price": price,
                    "store": store,
                    "category": category if category else "Uncategorized"
                })
    return data_list

def find_cheapest_overall(data):
    """ค้นหารายการสินค้าที่ราคาถูกที่สุดในข้อมูลทั้งหมด"""
    if not data:
        return None
    return min(data, key=lambda item: item["price"])

def find_cheapest_by_product(product_name, data):
    """ค้นหารายการที่ราคาถูกที่สุดของสินค้าที่ชื่อระบุ (ไม่แบ่งแหล่ง)"""
    # กรองรายการที่ชื่อสินค้าตรงกับที่ต้องการ (ไม่สนตัวพิมพ์เล็กใหญ่)
    matches = [item for item in data if item["product"].lower() == product_name.lower()]
    if not matches:
        return None
    return min(matches, key=lambda item: item["price"])

def filter_by_category(category_name, data):
    """กรองรายการสินค้าตามหมวดหมู่ที่ระบุ (ค้นหาแบบไม่สนตัวพิมพ์เล็กใหญ่)"""
    return [item for item in data if item["category"] and category_name.lower() in item["category"].lower()]

def sort_data(data, by="price"):
    """เรียงลำดับรายการสินค้าใน list ตามคีย์ที่กำหนด (ค่าเริ่มต้นคือ price จากน้อยไปมาก)"""
    if by == "price":
        # เรียงตามราคาตัวเลขจากน้อยไปมาก
        return sorted(data, key=lambda item: item["price"])
    else:
        # เรียงตามข้อความ (ชื่อสินค้า, ร้าน หรือหมวดหมู่) ตามลำดับตัวอักษร
        return sorted(data, key=lambda item: str(item.get(by, "")).lower())

# ===== ส่วนหลักโปรแกรม (ตัวอย่างการใช้งาน) =====
# สร้างข้อมูลตัวอย่าง (ในสถานการณ์จริงอาจใช้ load_data_from_csv อ่านจากไฟล์แทน)
sample_data = [
    {"product": "Milk",    "price": 45.0,  "store": "Store A",   "category": "Dairy"},
    {"product": "Milk",    "price": 50.0,  "store": "Store B",   "category": "Dairy"},
    {"product": "Bread",   "price": 30.0,  "store": "Store A",   "category": "Bakery"},
    {"product": "Bread",   "price": 25.0,  "store": "Store B",   "category": "Bakery"},
    {"product": "Bread",   "price": 28.0,  "store": "Store C",   "category": "Bakery"},
    {"product": "Eggs",    "price": 60.0,  "store": "Store A",   "category": "Groceries"},
    {"product": "Eggs",    "price": 55.0,  "store": "Store B",   "category": "Groceries"},
    {"product": "Chicken", "price": 120.0, "store": "Market",    "category": "Meat"},
    {"product": "Chicken", "price": 130.0, "store": "Supermart","category": "Meat"},
]

# แสดงข้อมูลสินค้าทั้งหมดในรูปแบบตาราง
print(f"{'Product':10s} {'Price':>6s} {'Store':10s} {'Category':10s}")
for item in sample_data:
    print(f"{item['product']:10s} {item['price']:6.2f} {item['store']:10s} {item['category']:10s}")
print()  # เว้นบรรทัด

# ค้นหาสินค้าที่ราคาถูกที่สุดในข้อมูลทั้งหมด
cheapest = find_cheapest_overall(sample_data)
if cheapest:
    print(f"Cheapest item overall: {cheapest['product']} at {cheapest['store']} (Price {cheapest['price']:.2f})\n")

# ค้นหาราคาถูกที่สุดของสินค้าบางชนิด (เช่น Milk และ Bread)
for product_name in ["Milk", "Bread"]:
    result = find_cheapest_by_product(product_name, sample_data)
    if result:
        print(f"Cheapest price for \"{product_name}\": {result['price']:.2f} at {result['store']}")
print()  # เว้นบรรทัด

# กรองรายการสินค้าตามหมวดหมู่ (เช่น Bakery)
category = "Bakery"
filtered_items = filter_by_category(category, sample_data)
print(f"Items in category '{category}':")
for item in filtered_items:
    print(f"- {item['product']:10s} {item['price']:6.2f} {item['store']:10s}")
print()  # เว้นบรรทัด

# แสดงสินค้าทั้งหมดเรียงตามราคา (จากถูกไปแพง)
sorted_items = sort_data(sample_data, by="price")
print("Products sorted by price (low to high):")
for item in sorted_items:
    print(f"- {item['product']:10s} {item['price']:6.2f} {item['store']:10s}")
