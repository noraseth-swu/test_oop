# --- zoo_system.py ---

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        # สัตว์ทั่วไปไม่มีเสียงเฉพาะ
        return "(ความเงียบ...)"

    def eat(self):
        return f"{self.name} กำลังกินอาหาร"

class Lion(Animal):
    # Lion is-a Animal
    def make_sound(self): # Overriding
        return "โฮกกก!"

class Monkey(Animal):
    # Monkey is-a Animal
    def make_sound(self): # Overriding
        return "เจี๊ยกๆ!"
    
    def climb_tree(self):
        return f"{self.name} ปีนต้นไม้อย่างคล่องแคล่ว"

class Zookeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal_object):
        """ให้อาหารสัตว์ 1 ตัว"""
        print(f"ผู้ดูแล {self.name} กำลังจะให้อาหาร {animal_object.name}")
        # เรียกเมธอด .eat() ของสัตว์
        print(f"  -> {animal_object.eat()}")

    def listen_to_zoo(self, list_of_animals):
        """ฟังเสียงสัตว์ทั้งสวนสัตว์"""
        print(f"\n{self.name} กำลังฟังเสียงในสวนสัตว์...")
        for animal in list_of_animals:
            # Polymorphism in action!
            sound = animal.make_sound()
            print(f"ได้ยินเสียงจากกรงของ {animal.name}: {sound}")

# --- การจำลองการใช้งาน ---
if __name__ == "__main__":
    # สร้างสัตว์ชนิดต่างๆ ซึ่งทั้งหมดก็คือ Animal ชนิดหนึ่ง
    simba = Lion("ซิมบ้า", 5)
    abu = Monkey("อาบู", 3)
    unknown = Animal("ตัวอะไรไม่รู้", 1)

    # สร้างผู้ดูแล
    keeper_bob = Zookeeper("บ๊อบ")

    # ผู้ดูแลให้อาหารลิง
    keeper_bob.feed_animal(abu)
    
    # สร้าง List ของสัตว์ทั้งหมดในสวน
    all_animals_in_zoo = [simba, abu, unknown]
    
    # ผู้ดูแลเดินฟังเสียงสัตว์ทั้งหมด
    keeper_bob.listen_to_zoo(all_animals_in_zoo)