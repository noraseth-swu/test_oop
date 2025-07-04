# สร้าง Dictionary ว่าง
fruit_counts = {}
print(f"เริ่มต้น: {fruit_counts}")

# --- TODO 1: ลองเข้าถึง Key ที่ยังไม่มีอยู่ ---
# ลองเขียนโค้ดเพื่อ print ค่าของ fruit_counts["apple"]
# บรรทัดนี้จะทำให้เกิด Error จงใจให้มันเกิด แล้วอ่าน Error ที่เกิดขึ้น
print(fruit_counts["apple"]) # เอา # ออกเมื่อต้องการทดสอบ

# หลังจากเห็น Error แล้ว ให้ใส่ # กลับไปเหมือนเดิม

# --- TODO 2: เพิ่ม Key เข้าไปก่อน แล้วค่อยเข้าถึง ---
fruit_counts["apple"] = 1 # เพิ่ม apple เข้าไป
print(f"หลังจากเพิ่ม apple: {fruit_counts}")

# ลองเข้าถึง Key "apple" อีกครั้ง (ตอนนี้ไม่ควร Error แล้ว)
apple_count = fruit_counts["apple"]
print(f"จำนวน apple คือ: {apple_count}")

student_data = {
    "name": "สมศรี",
    "id": "S001"
    # สังเกตว่าไม่มี key "score"
}

# --- TODO 1: ใช้ .get() กับ Key ที่มีอยู่ ---
student_name = student_data.get("name")
print(f"ชื่อนักเรียน: {student_name}")

# --- TODO 2: ใช้ .get() กับ Key ที่ไม่มีอยู่ (ไม่ระบุ default) ---
# จะได้ค่าอะไรออกมา?
student_major = student_data.get("major")
print(f"วิชาเอก: {student_major}") # ผลที่คาดหวัง: None

# --- TODO 3: ใช้ .get() กับ Key ที่ไม่มีอยู่ (ระบุค่า default) ---
# นี่คือส่วนที่เหมือนกับคำถามข้อ 5
# ถ้าไม่มี "score" ให้ถือว่าเป็น 0
student_score = student_data.get("score", 0)
print(f"คะแนน: {student_score}") # ผลที่คาดหวัง: 0



sentence = "hello world"
char_counts = {} # Dictionary ที่จะใช้เก็บผลการนับ

# วน Loop ในแต่ละตัวอักษรของประโยค
for char in sentence:
    
    # --- TODO 1: ดึงจำนวนครั้งที่เคยเจอตัอักษรนี้ (char) มาก่อน ---
    # ใช้ .get() เพื่อดึงค่าเก่าของ char ออกมาจาก char_counts
    # ถ้ายังไม่เคยเจอตัวอักษรนี้มาก่อน ให้ค่าเริ่มต้นเป็น 0
    # ตั้งชื่อตัวแปรว่า old_count
    old_count = char_counts.get("char", 0)
    
    # --- TODO 2: คำนวณจำนวนครั้งใหม่ ---
    # เอาค่าเก่ามาบวก 1
    new_count = old_count + 1
    
    # --- TODO 3: อัปเดตค่าใหม่กลับเข้าไปใน Dictionary ---
    # ใช้ char เป็น Key และ new_count เป็น Value
    char_counts[char] = new_count

    # (ลอง print เพื่อดูการเปลี่ยนแปลงในแต่ละรอบ)
    print(f"เจอตัว '{char}', อัปเดต counter เป็น: {char_counts}")


print("\n--- ผลลัพธ์สุดท้าย ---")
print(char_counts)

# --- BONUS: เขียน TODO 1-3 ทั้งหมดในบรรทัดเดียว (เหมือนในโจทย์) ---
char_counts_oneline = {}
for char in sentence:
    # ลองเขียนโค้ดที่ทำงานเหมือน TODO 1-3 แต่อยู่ในบรรทัดเดียว
    char_counts_oneline[char] = char_counts.get("char", 0) + 1

print("\n--- ผลลัพธ์สุดท้าย (แบบบรรทัดเดียว) ---")
print(char_counts_oneline)