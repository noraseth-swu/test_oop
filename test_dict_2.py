def grade_analyzer(student_scores):
    """
    วิเคราะห์คะแนนนักเรียนและคำนวณเกรด
    student_scores: List ของ Dict, เช่น [{"name": "สมชาย", "score": 85}, ...]
    คืนค่าเป็น: Dict สรุปผล
    """
    
    if not student_scores:
        return {"summary": "No student data provided.", "grades": {}}

    # ใช้ dict เพื่อเก็บว่าแต่ละเกรดมีนักเรียนกี่คน
    grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    # ใช้ list เพื่อเก็บชื่อนักเรียนที่ได้เกรด A
    top_students = []
    
    total_score = 0
    student_names = []

    for student in student_scores:
        name = student.get("name", "Unknown")
        score = student.get("score", 0)
        
        student_names.append(name)
        total_score += score
        
        # --- TODO 1: เขียนเงื่อนไข if/elif/else เพื่อคำนวณเกรด ---
        # 80-100 -> "A"
        # 70-79  -> "B"
        # 60-69  -> "C"
        # 50-59  -> "D"
        # < 50   -> "F"
        grade = ""
        if score >= 80:
            grade = "A"
            # TODO 2: ถ้าได้เกรด A, ให้เพิ่มชื่อนักเรียนลงใน list `top_students`
            top_students.append(name)
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"
        
        # TODO 3: เมื่อได้เกรดแล้ว, ให้อัปเดต counter ใน dictionary `grade_distribution`
        # เช่น ถ้าได้เกรด "B", ให้เพิ่มค่าของ key "B" ขึ้น 1
        if grade: # เช็คว่ามีการกำหนดเกรดแล้ว
            grade_distribution[grade] += 1

    # --- TODO 4: คำนวณค่าเฉลี่ยของคะแนนทั้งหมด ---
    average_score = total_score / len(student_scores) if student_scores else 0.0
    statistics = (len(student_scores), average_score)
    
    # สร้าง Dictionary สรุปผลสุดท้าย
    final_report = {
        "stats": statistics,
        "grade_distribution": grade_distribution,
        "top_students": top_students
    }
    
    return final_report

# --- ส่วนของการทดสอบ ---
if __name__ == "__main__":
    scores = [
        {"name": "สมศักดิ์", "score": 85},
        {"name": "มานี", "score": 92},
        {"name": "ชูใจ", "score": 78},
        {"name": "ปิติ", "score": 65},
        {"name": "สมศรี", "score": 49},
        {"name": "ไม่มีชื่อ", "score": 75}
    ]
    
    report = grade_analyzer(scores)
    
    # แสดงผล
    import json
    print(json.dumps(report, indent=4, ensure_ascii=False))