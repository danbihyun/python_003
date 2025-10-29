# # key: value 쌍으로 저장
# student = {
#     "name": "홍길동",
#     "age": 20,
#     "major": "AI",
#     "grades": [90, 85, 95]
# }

# # Key로 접근
# print(student["name"])        # 홍길동
# print(student["grades"][0])   # 90

# # 안전한 접근 - get()
# print(student.get("name"))           # 홍길동
# print(student.get("email", "없음"))  # 없음 (기본값)



# 연락처 저장
contacts = {
    "엄마": "010-1234-5678",
    "아빠": "010-2345-6789",
    "친구": "010-3456-7890"
    }
    
# 연락처 조회
name = "엄마"
phone = contacts.get(name)
print(f"{name}의 번호: {phone}")

# 새 연락처 추가
contacts["동생"] = "010-4567-8901"

# 모든 연락처 출력
print("\n=== 전체 연락처 ===")
for name, phone in contacts.items():
    print(f"{name}: {phone}")