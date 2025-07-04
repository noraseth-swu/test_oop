# --- transport_system.py ---

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.distance_traveled = 0

    def drive(self, kilometers):
        self.distance_traveled += kilometers
        print(f"ยานพาหนะ {self.brand} เดินทางไป {kilometers} กม.")

    def display_info(self):
        print(f"ยี่ห้อ: {self.brand}, ปี: {self.year}")
        print(f"ระยะทางสะสม: {self.distance_traveled} กม.")

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        # เรียก constructor ของคลาสแม่
        super().__init__(brand, year)
        # เพิ่ม attribute ของตัวเอง
        self.num_doors = num_doors

    # Overriding เมธอด display_info
    def display_info(self):
        print("--- ข้อมูลรถยนต์ ---")
        # เรียก display_info ของแม่ เพื่อพิมพ์ข้อมูลพื้นฐานก่อน
        super().display_info()
        # พิมพ์ข้อมูลเฉพาะของ Car
        print(f"จำนวนประตู: {self.num_doors}")

class Motorcycle(Vehicle):
    # คลาสนี้ไม่มี __init__ ของตัวเอง
    
    # Overriding เมธอด drive
    def drive(self, kilometers):
        print("🏍️ บิดคันเร่ง!")
        # เรียก drive ของแม่ เพื่อทำการบวกระยะทาง
        super().drive(kilometers)

# --- การจำลองการใช้งาน ---
if __name__ == "__main__":
    my_car = Car("Toyota", 2022, 4)
    my_moto = Motorcycle("Honda", 2023)

    print("--- การเดินทางรอบแรก ---")
    my_car.drive(100)
    my_moto.drive(50)

    print("\n--- แสดงข้อมูล ---")
    my_car.display_info()
    print("") # เว้นบรรทัด
    my_moto.display_info()