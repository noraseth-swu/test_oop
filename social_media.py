# --- social_media.py ---

class Post:
    def __init__(self, author_username, content):
        self.author = author_username
        self.content = content
        self.likes = [] # ใช้ List เก็บชื่อ username ของคนที่มากดไลค์

    def like(self, user_who_liked):
        """เมธอดสำหรับให้ User มากดไลค์โพสต์นี้"""
        # ป้องกันการกดไลค์ซ้ำ
        if user_who_liked.username not in self.likes:
            self.likes.append(user_who_liked.username)
            print(f"'{user_who_liked.username}' ได้กดไลค์โพสต์ของ '{self.author}'")
        else:
            print(f"'{user_who_liked.username}' ได้กดไลค์โพสต์นี้ไปแล้ว")

    def display(self):
        """แสดงผลโพสต์"""
        print("--------------------")
        print(f"โพสต์โดย: {self.author}")
        print(f"> {self.content}")
        print(f"ถูกใจ {len(self.likes)} คน: {self.likes}")
        print("--------------------")

class User:
    def __init__(self, username):
        self.username = username

    def create_post(self, content):
        """User สร้าง Post ใหม่ของตัวเอง"""
        print(f"ผู้ใช้ '{self.username}' กำลังสร้างโพสต์ใหม่...")
        # สร้าง Object Post โดยส่งชื่อตัวเองเป็นผู้เขียน
        new_post = Post(self.username, content)
        return new_post

# --- การจำลองการใช้งาน ---
if __name__ == "__main__":
    # 1. สร้างผู้ใช้
    user_alice = User("Alice")
    user_bob = User("Bob")

    # 2. Alice สร้างโพสต์
    alices_post = user_alice.create_post("วันนี้อากาศดีจัง!")

    # 3. แสดงผลโพสต์เริ่มต้น
    alices_post.display()

    # 4. Bob มากดไลค์โพสต์ของ Alice
    alices_post.like(user_bob)

    # 5. Alice มากดไลค์โพสต์ของตัวเอง
    alices_post.like(user_alice)

    # 6. Bob พยายามกดไลค์ซ้ำ
    alices_post.like(user_bob)

    # 7. แสดงผลโพสต์สุดท้าย
    print("\n--- สถานะโพสต์ล่าสุด ---")
    alices_post.display()