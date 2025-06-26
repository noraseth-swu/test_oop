class BankAccount:
    
    # 1. เขียน Constructor (__init__)
    # รับค่า account_number, owner_name, และยอดเงินเริ่มต้น (initial_balance)
    # แล้วกำหนดค่าให้กับ self.account_number, self.owner_name, self.balance
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        print(f"กำลังเปิดบัญชีใหม่สำหรับคุณ {owner_name}...")
        # --- เติมโค้ดตรงนี้ ---
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = float(initial_balance)
        # --------------------
        print("เปิดบัญชีสำเร็จ!")

    # 2. เขียน Method สำหรับแสดงยอดเงิน
    def display_balance(self):
        print("--------------------")
        print(f"  บัญชี: {self.account_number}")
        print(f"  เจ้าของ: {self.owner_name}")
        # ใช้ f-string format ให้ตัวเลขมี comma จะดูสวยขึ้น -> f'{self.balance:,.2f}'
        print(f"  ยอดเงินคงเหลือ: {self.balance:,.2f} บาท")
        print("--------------------")
    
    # 3. เขียน Method สำหรับฝากเงิน
    def deposit(self, amount):
        if amount > 0:
            # --- เติมโค้ดตรงนี้ ---
            # บวก amount เข้าไปใน self.balance
            self.balance += amount
            print("ฝากเงินสำเร็จ!")
            # แสดงข้อความว่าฝากเงินสำเร็จ
            # --------------------
            pass # ลบ pass ออกเมื่อเขียนโค้ดแล้ว
        else:
            print("จำนวนเงินที่ฝากต้องมากกว่า 0")

    # 4. เขียน Method สำหรับถอนเงิน
    def withdraw(self, amount):
        if amount > 0:
            # --- เติมโค้ดตรงนี้ ---
            # เช็คว่า self.balance >= amount หรือไม่
            if self.balance >= amount:
                # ถ้าใช่, ลบ amount จาก self.balance
                self.balance -= amount
                print("ถอนเงินสำเร็จ!")
            else:
                print("ยอดเงินไม่พอสำหรับการถอน")

            # ถ้าใช่, ให้ลบ amount ออกจาก self.balance แล้ว print ข้อความ
            # ถ้าไม่ใช่, ให้ print ว่ายอดเงินไม่พอ
        else:
            print("จำนวนเงินที่ถอนต้องมากกว่า 0")


# --- ส่วนของการทดสอบ (สำคัญมาก!) ---

# สร้าง Object บัญชีที่ 1
acc1 = BankAccount("111-222-333", "สมชาย ใจดี", 1000)

# สร้าง Object บัญชีที่ 2 (คนละบัญชีกันโดยสิ้นเชิง)
acc2 = BankAccount("444-555-666", "สมหญิง เก่งมาก", 5000)

print("\n--- เริ่มทำธุรกรรม ---")
acc1.display_balance()
acc2.display_balance()

print("\n--- สมชายฝากเงิน ---")
acc1.deposit(500)
acc1.display_balance()

print("\n--- สมหญิงพยายามถอนเงินมากกว่าที่มี ---")
acc2.withdraw(6000)
acc2.display_balance() # ยอดเงินต้องไม่เปลี่ยนแปลง

print("\n--- สมหญิงถอนเงินปกติ ---")
acc2.withdraw(1500)
acc2.display_balance() # ยอดเงินต้องลดลง

# สังเกตว่าการทำธุรกรรมของ acc1 ไม่มีผลกระทบใดๆ กับ acc2
# นี่คือพลังของการที่แต่ละ Object มี state (self.balance) เป็นของตัวเอง