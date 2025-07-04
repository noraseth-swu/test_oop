class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        """
        เมธอดนี้ในคลาสแม่จะคืนค่าเงินเดือนพื้นฐาน
        ซึ่งในโลกจริงอาจจะเป็น 0 หรือ raise NotImplementedError
        """
        return 15000.0 # สมมติเงินเดือนพื้นฐาน

class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        # TODO 1: เรียก constructor ของคลาสแม่
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    # TODO 2: Overriding เมธอด calculate_payroll
    def calculate_payroll(self):
        # พนักงานประจำได้เงินเดือนตามที่ระบุไว้เลย
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        # TODO 3: เรียก constructor ของคลาสแม่
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    # TODO 4: Overriding เมธอด calculate_payroll
    def calculate_payroll(self):
        # พนักงานสัญญาจ้างได้เงินตามชั่วโมงที่ทำ * เรทต่อชั่วโมง
        self.monthly_salary = self.hours_worked * self.hourly_rate
        return self.monthly_salary

class PayrollSystem:
    def calculate(self, list_of_employees):
        print("--- กำลังคำนวณเงินเดือน ---")
        for emp in list_of_employees:
            # TODO 5: คำนวณเงินเดือนของพนักงานแต่ละคน
            # แล้วพิมพ์ผลลัพธ์ออกมาในรูปแบบ: "จ่ายเงินเดือนให้ [ชื่อพนักงาน]: [จำนวนเงิน] บาท"
            # (Hint: Polymorphism ทำให้เราเรียก .calculate_payroll() ได้เลย)
            salary = emp.calculate_payroll()
            print(f"จ่ายเงินเดือนให้ {emp.name}: {salary:,.2f} บาท")
        print("---------------------------")

# --- ส่วนของการทดสอบ ---
if __name__ == "__main__":
    # สร้างพนักงานประเภทต่างๆ
    emp1 = FullTimeEmployee("FT001", "สมศักดิ์", 50000)
    emp2 = ContractEmployee("CT002", "มานี", 120, 400) # ทำ 120 ชม. ชม.ละ 400
    emp3 = ContractEmployee("CT003", "ชูใจ", 80, 450)
    
    # สร้างระบบจ่ายเงิน
    payroll_system = PayrollSystem()
    
    # นำพนักงานทั้งหมดใส่ใน List
    all_employees = [emp1, emp2, emp3]
    
    # สั่งให้ระบบคำนวณ
    payroll_system.calculate(all_employees)
