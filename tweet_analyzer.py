# --- tweet_analyzer.py ---

def process_tweets(tweet_data_list):
    """
    วิเคราะห์รายการ tweets ที่เป็น list ของ dictionary
    และคืนค่าเป็น dictionary สรุปผล
    """
    
    # ใช้ set เพื่อเก็บรายชื่อผู้ใช้ที่ไม่ซ้ำกัน
    unique_users = set()
    
    # ใช้ dict เพื่อนับจำนวน hashtag
    hashtag_counts = {}
    
    total_likes = 0
    all_mentioned_users = []

    for tweet in tweet_data_list:
        # tweet เป็น dictionary
        username = tweet.get("username")
        likes = tweet.get("likes", 0)
        
        # 1. จัดการกับผู้ใช้
        if username:
            unique_users.add(username)
        
        # 2. จัดการกับยอดไลค์
        total_likes += likes
        
        # 3. จัดการกับ hashtags
        hashtags_in_tweet = tweet.get("hashtags", []) # ได้เป็น list
        for tag in hashtags_in_tweet:
            # เพิ่ม counter ของ hashtag นั้นๆ
            hashtag_counts[tag] = hashtag_counts.get(tag, 0) + 1
            
        # 4. จัดการกับ user ที่ถูก mention
        all_mentioned_users.extend(tweet.get("mentions", []))

    # สร้าง Tuple สำหรับผลลัพธ์ที่ไม่ต้องการให้เปลี่ยนแปลง
    analysis_result = (len(unique_users), total_likes)
    
    # สร้าง Dictionary สำหรับผลสรุปสุดท้าย
    summary = {
        "analysis_data": analysis_result,
        "top_hashtag": max(hashtag_counts, key=hashtag_counts.get) if hashtag_counts else None,
        "mentioned_users_unique": list(set(all_mentioned_users))
    }
    
    return summary

# --- ข้อมูลตัวอย่าง ---
if __name__ == "__main__":
    tweets = [
        {"username": "alice", "content": "I love Python! #coding", "likes": 15, "hashtags": ["coding"], "mentions": ["bob"]},
        {"username": "bob", "content": "Learning about data structures.", "likes": 10, "mentions": ["charlie"]},
        {"username": "alice", "content": "OOP is fun. #python #coding", "likes": 25, "hashtags": ["python", "coding"]},
        {"username": "charlie", "content": "Hello world! #python", "likes": 5, "hashtags": ["python"]}
    ]
    
    report = process_tweets(tweets)
    print(report)
