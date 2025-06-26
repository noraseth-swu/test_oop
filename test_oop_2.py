class product:
    def __init__(self, name, sku, price, quantity):
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity
        print(f" สร้างสินค้า {self.name} (SKU: {self.sku}) จำนวน {self.quantity} ชิ้น สำเร็จ")
    def display_info(self):
        print(f"ชื่อสินค้า: {self.name}, SKU: {self.sku}, ราคา: {self.price:.2f} บาท, จำนวนคงเหลือ: {self.quantity} ชิ้น")

    def restock(self, quantity):
        if quantity > 0:
            self.quantity += quantity
            print(f"เพิ่มสินค้า {self.name} จำนวน {quantity} ชิ้น สำเร็จ สินค้าคงเหลือ: {self.quantity} ชิ้น")
        else:
            print("จำนวนสินค้าต้องมากกว่า 0")

    def sell(self, sell_quantity):
        if  sell_quantity <= self.quantity and sell_quantity > 0:
            self.quantity -= sell_quantity
            print(f"ขายสินค้า {self.name} จำนวน {sell_quantity} ชิ้น สำเร็จ สินค้าคงเหลือ: {self.quantity} ชิ้น")
        elif sell_quantity <= 0:
            print("จำนวนสินค้าที่ขายต้องมากกว่า 0")
        else:
            print(f"สินค้า {self.name} มีไม่พอสำหรับการขาย จำนวนคงเหลือ: {self.quantity} ชิ้น")

    def get_total_value(self):
        return self.price * self.quantity

product1 = product("Laptop", "COM-01", 25000, 10)
product2 = product("Mouse", "ACC-05", 800, 30)
product1.display_info()
product2.display_info()
product1.restock(5)
product2.sell(12)
product1.display_info()
product2.display_info()
product1.get_total_value()
product2.get_total_value()