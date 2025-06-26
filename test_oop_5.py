class CartItem:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_subtotal(self):
        return self.price * self.quantity
        
    
    def display(self):
        sub_total = self.get_subtotal()
        return f"{self.name} ({self.price:,.2f} บาท) - {self.quantity} ชิ้น - ยอดรวม {sub_total:,.2f} บาท"
    
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, new_item_object):
        item_found = False
        for existing_item in self.items:
            if existing_item.name == new_item_object.name:
                existing_item.quantity += new_item_object.quantity
                print(f"อัพเดต {existing_item.name} ในตระกร้าเป็น {existing_item.quantity} ชิ้น")
                item_found = True
                break

        if not item_found:
            self.items.append(new_item_object)
            print(f"เพิ่ม {new_item_object.name} จำนวน {new_item_object.quantity} ชิ้น")

    def remove_item(self, item_name_to_remove):
        item_to_remove = None
        for items in self.items:
            if items.name == item_name_to_remove:
                item_to_remove = items
                break
        if item_to_remove:
            self.items.remove(item_to_remove)
            print(f"ลบ {item_name_to_remove} ออกจากตระกร้าสำเร็จ")
        
        else:
            print(f"ไม่พบชื่อสินค้า {item_name_to_remove} ในตระกร้า")

    def get_grand_total(self):
        total = 0.0
        for item in self.items:
            total += item.get_subtotal()
        return total

    def display_cart(self):
        print("--- ตะกร้าสินค้าของคุณ ---")
        if not self.items:
            print(f"ไม่มีสินค้าในตระกร้า")
        else:
            for item in self.items:
                print(item.display())

            grand_total = self.get_grand_total()
            print("--------------------------")
            print(f"ยอดรวมสุทธิ: {grand_total:,.2f} บาท")
            print("--------------------------")
        
if __name__ == "__main__":
    my_cart = ShoppingCart()

    print("--- สถานะตะกร้าเริ่มต้น ---")
    my_cart.display_cart()

    print("\n--- เพิ่มสินค้า ---")
    my_cart.add_item(CartItem("นม", 25.50, 2))
    my_cart.add_item(CartItem("ไข่ไก่", 80.00, 1))
    my_cart.add_item(CartItem("ขนมปัง", 45.00))
    my_cart.display_cart()

    print("\n--- เพิ่ม 'นม' อีก 1 กล่อง ---")
    my_cart.add_item(CartItem("นม", 25.50, 1))
    my_cart.display_cart()

    print("\n--- ลบ 'ไข่ไก่' ออกจากตะกร้า ---")
    my_cart.remove_item("ไข่ไก่")
    my_cart.display_cart()
    
    print("\n--- พยายามลบ 'น้ำเปล่า' ---")
    my_cart.remove_item("น้ำเปล่า")






