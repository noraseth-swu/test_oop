import random

class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        """ผู้เล่นโจมตีเป้าหมาย"""
        print(f"🤺 {self.name} โจมตี {target.name}!")
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        """ผู้เล่นได้รับความเสียหาย"""
        self.health -= float(damage)
        self.health = max(0, self.health)
        print(f"💥 {self.name} ได้รับความเสียหาย {damage} หน่วย! (HP เหลือ {self.health})")

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, name, health, attack_power):
        # TODO: กำหนดค่า attributes ให้กับ Monster
        self.name = name
        self.health = float(health)
        self.attack_power = float(attack_power)

    def attack(self, target):
        """มอนสเตอร์โจมตีเป้าหมาย"""
        print(f"👹 {self.name} โจมตี {target.name}!")
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        """มอนสเตอร์ได้รับความเสียหาย"""
        # TODO: ลดค่า self.health ตาม damage ที่ได้รับ
        self.health -= float(damage)
        self.health = max(0, self.health)
        print(f"🩸 {self.name} ได้รับความเสียหาย {damage} หน่วย! (HP เหลือ {self.health})")

    def is_alive(self):
        return self.health > 0

# --- ส่วนของ Game Loop ---
if __name__ == "__main__":
    player = Player("อัศวิน", 100, 15)
    monster = Monster("สไลม์", 80, 10)

    turn = 1
    # ต่อสู้ไปเรื่อยๆ จนกว่าใครคนหนึ่งจะตาย
    while player.is_alive() and monster.is_alive():
        print(f"\n--- เทิร์นที่ {turn} ---")
        
        # --- ตาของผู้เล่น ---
        # TODO: เรียกให้ผู้เล่นโจมตีมอนสเตอร์
        player.attack(monster)

        # เช็คว่ามอนสเตอร์ตายหรือยัง
        if not monster.is_alive():
            print(f"🎉 {monster.name} ถูกกำจัดแล้ว!")
            break

        # --- ตาของมอนสเตอร์ ---
        # TODO: เรียกให้มอนสเตอร์โจมตีผู้เล่น
        
        monster.attack(player)

        # เช็คว่าผู้เล่นตายหรือยัง
        if not player.is_alive():
            print(f"💀 {player.name} พ่ายแพ้...")
            break
            
        turn += 1

    print("\n--- จบการต่อสู้ ---")