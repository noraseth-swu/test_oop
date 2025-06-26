class Snack():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"ชื่อ: {self.name}, ราคา: {self.price:.2f} บาท, จำนวน: {self.quantity} ชิ้น")
    
    def dispense(self):
        if self.quantity <= 0:
            return False
        else:
            self.quantity -= 1
            return True


class VendingMachine():
    def __init__(self):
        self.items = {}
        self.credit = 0.0
    
    def load_snack(self, slot_code, snack_object):
        self.items[slot_code] = snack_object

    def display_items(self):
        for slot_code, snack_object in self.items.items():
            print(f"รหัส: {slot_code}, ", end="")
            snack_object.display()


    def insert_money(self, amount):
        if amount <= 0:
            print("จำนวนเงินต้องมากกว่า 0")
            return
        else:
            self.credit += amount
            print(f"เติมเงินสำเร็จ จำนวนเงินสะสม: {self.credit:.2f} บาท")
    
    def purchase(self, slot_code):
        if slot_code not in self.items:
            print(f"รหัสสินค้าไม่ถูกต้อง")
            return
        elif self.items[slot_code].quantity <= 0:
            print(f"สินค้า {self.items[slot_code].name} มีไม่พอสำหรับการซื้อ")
            return
        else:
            snack_to_buy = self.items[slot_code]
            if snack_to_buy.dispense():
                if self.credit >= snack_to_buy.price:
                    self.credit -= snack_to_buy.price
                    print(f"ซื้อสินค้า {snack_to_buy.name} สำเร็จ")
                else:
                    print("จำนวนเงินไม่พอสำหรับการซื้อสินค้า")
            else:
                print(f"สินค้า {snack_to_buy.name} มีไม่พอสำหรับการซื้อ")

    def get_refund(self):
        refund = self.credit
        self.credit = 0.0
        print(f"คืนเงินจำนวน {refund:.2f} บาท")
        return refund