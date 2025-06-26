class Task:
    def __init__(self, description, due_date):
        self.description=description
        self.due_date=due_date
        self.completed=False
        print(f"สร้างงานใหม่: '{self.description}' สำเร็จ")

    def display(self):
        if self.completed:
            print(f"[X] {self.description} (กำหนดส่ง {self.due_date})" )
        else:
            print(f"[ ] {self.description} (กำหนดส่ง {self.due_date})" )

    def mark_as_complete(self):
        if self.completed:
            print(f"Task '{self.description}' is already completed.")
            return
        else:
            self.completed=True
            print(f"Task '{self.description}' marked as completed.")

    def edit_description(self, new_description):
        self.description = new_description
        print(f"เปลี่ยนคำอธิบายงานเป็น '{self.description}'")

    def edit_due_date(self, new_date):
        self.due_date = new_date
        print(f"เปลี่ยนวันที่กำหนดส่งเป็น '{self.due_date}'")

task1 = Task("เรียนรู้ Python OOP", "2024-10-30")
task2 = Task("ส่งอีเมลหาลูกค้า", "2024-10-25")
task3 = Task("ออกกำลังกาย", "2024-10-26")

my_todo_list = [task1, task2, task3]

for task in my_todo_list:
    task.display()

task2.mark_as_complete()
task2.mark_as_complete()
task3.edit_description("ออกกำลังกายตอนเย็น")

for task in my_todo_list:
    task.display()