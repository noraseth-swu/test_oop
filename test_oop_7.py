class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def get_info(self):
        """คืนค่าสตริงข้อมูลพื้นฐานของสินค้า"""
        return f"{self.name} - ราคา {self.price:.2f} บาท"

class Coffee(MenuItem):
    def __init__(self, name, price, bean_type, size="M"):
        # TODO 1: เรียก constructor ของคลาสแม่ (MenuItem)
        # เพื่อจัดการ name และ price
        super().__init__(name, price)    

        # เพิ่ม attributes เฉพาะของ Coffee
        self.bean_type = bean_type
        self.size = size

    # TODO 2: Overriding เมธอด get_info
    def get_info(self):
        # ดึงข้อมูลพื้นฐานจากคลาสแม่มาก่อน
        base_info = super().get_info()
        # ต่อท้ายด้วยข้อมูลเฉพาะของกาแฟ
        return f"{base_info} (เมล็ด: {self.bean_type}, ขนาด: {self.size})"

class Bakery(MenuItem):
    def __init__(self, name, price, is_gluten_free=False):
        # TODO 3: เรียก constructor ของคลาสแม่
        super().__init__(name, price)
        self.is_gluten_free = is_gluten_free

    # TODO 4: Overriding เมธอด get_info
    def get_info(self):
        # ดึงข้อมูลพื้นฐานจากคลาสแม่
        base_info = super().get_info()
        # ตรวจสอบ attribute เฉพาะของ Bakery แล้วต่อท้าย
        if self.is_gluten_free:
            return f"{base_info} [Gluten-Free]"
        else:
            return base_info

# --- ส่วนของการทดสอบ ---
if __name__ == "__main__":
    # สร้างรายการสินค้า
    latte = Coffee("ลาเต้", 60, "อาราบิก้า", "L")
    croissant = Bakery("ครัวซองต์", 50)
    brownie_gf = Bakery("บราวนี่", 75, True)

    # ใส่รายการทั้งหมดลงใน List
    order_list = [latte, croissant, brownie_gf]
    
    total_price = 0
    print("--- รายการสั่งซื้อ ---")
    for item in order_list:
        # พิมพ์ข้อมูลของแต่ละรายการ
        print(f"- {item.get_info()}")
        # บวกราคาเข้ายอดรวม
        total_price += item.price

    print("---------------------")
    print(f"ราคารวมทั้งหมด: {total_price:.2f} บาท")