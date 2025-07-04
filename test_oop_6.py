class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False # สถานะว่าถูกยืมไปหรือยัง

    def check_out(self):
        """เมธอดสำหรับการยืมหนังสือ"""
        if not self.is_checked_out:
            self.is_checked_out = True
            return True # ยืมสำเร็จ
        return False # ถูกยืมไปแล้ว

    def return_book(self):
        """เมธอดสำหรับการคืนหนังสือ"""
        if self.is_checked_out:
            self.is_checked_out = False
            return True # คืนสำเร็จ
        return False # หนังสืออยู่ที่ชั้นอยู่แล้ว

    def display(self):
        status = "ถูกยืมไปแล้ว" if self.is_checked_out else "อยู่ที่ชั้นวาง"
        return f"'{self.title}' โดย {self.author} (สถานะ: {status})"

class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = {} # ใช้ dict เก็บหนังสือ โดยมี title เป็น key และ Book object เป็น value

    def add_book(self, book_object):
        """เพิ่ม Book object เข้าไปใน catalog"""
        # ใช้ชื่อหนังสือเป็น key        
        self.catalog[book_object.title] = book_object

        print(f"เพิ่มหนังสือ '{book_object.title}' เข้าห้องสมุด {self.name}")

    def display_catalog(self):
        """แสดงรายชื่อหนังสือทั้งหมดในห้องสมุด"""
        print(f"\n--- หนังสือในห้องสมุด {self.name} ---")
        if not self.catalog:
            print("ยังไม่มีหนังสือในห้องสมุด")
            return

        # วนลูปใน dictionary เพื่อแสดงผล
        for book in self.catalog.values():
            print(book.display())

    def lend_book(self, book_title):
        """ให้ยืมหนังสือตามชื่อเรื่อง"""
        # 1. เช็คว่ามีหนังสือชื่อนี้ใน catalog หรือไม่
        if book_title in self.catalog:
            # 2. ดึง Book object ออกมา
            book_to_lend = self.catalog[book_title]
            
            # 3. เรียกเมธอด .check_out() ของ Book object นั้น
            is_lend = book_to_lend.check_out()
            #    แล้วเช็คผลลัพธ์ที่ได้กลับมา (True หรือ False)
            if is_lend: # YOUR CODE HERE ...
                print(f"ให้ยืม '{book_title}' สำเร็จ")
            else:
                print(f"ขออภัย '{book_title}' ถูกยืมไปแล้ว")
        else:
            print(f"ขออภัย ไม่มีหนังสือชื่อ '{book_title}' ในห้องสมุด")
            
# --- ผลลัพธ์ที่คาดหวัง ---
#
# เพิ่มหนังสือ 'The Lord of the Rings' เข้าห้องสมุด Central Library
# เพิ่มหนังสือ 'Dune' เข้าห้องสมุด Central Library
#
# --- หนังสือในห้องสมุด Central Library ---
# 'The Lord of the Rings' โดย J.R.R. Tolkien (สถานะ: อยู่ที่ชั้นวาง)
# 'Dune' โดย Frank Herbert (สถานะ: อยู่ที่ชั้นวาง)
#
# --- การยืมหนังสือ ---
# ให้ยืม 'Dune' สำเร็จ
# ขออภัย 'Dune' ถูกยืมไปแล้ว
# ขออภัย ไม่มีหนังสือชื่อ '1984' ในห้องสมุด
#
# --- หนังสือในห้องสมุด Central Library ---
# 'The Lord of the Rings' โดย J.R.R. Tolkien (สถานะ: อยู่ที่ชั้นวาง)
# 'Dune' โดย Frank Herbert (สถานะ: ถูกยืมไปแล้ว)
if __name__ == "__main__":
    mybook1 = Book("The Lord of the Rings","J.R.R. Tolkien")
    mybook2 = Book("Dune","Frank Herbert")

    mylibrary = Library("Central Library")

    mylibrary.add_book(mybook1)
    mylibrary.add_book(mybook2)

    mylibrary.display_catalog()

    mylibrary.lend_book("Dune")
    mylibrary.lend_book("Dune")
    mylibrary.lend_book("1984")
    mylibrary.display_catalog()



