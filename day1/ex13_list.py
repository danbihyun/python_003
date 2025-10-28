# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(data[2:5])    # [2, 3, 4] (인덱스 2~4)
# print(data[:3])     # [0, 1, 2] (처음부터 3개)
# print(data[5:])     # [5, 6, 7, 8, 9] (5부터 끝까지)
# print(data[::2])    # [0, 2, 4, 6, 8] (2칸씩)
# print(data[::-1])   # [9, 8, 7, ...] (역순) ⭐


fruits = ["사과", "바나나"]

# 추가
fruits.append("포도")           # 끝에 추가
fruits.insert(1, "딸기")        # 특정 위치에 추가
print(fruits)
fruits.extend(["수박", "참외"]) # 여러 개 추가
print(fruits)

# 삭제
fruits.remove("바나나")  # 값으로 삭제
print(fruits)
popped = fruits.pop()    # 마지막 요소 삭제 후 반환
print(fruits)
del fruits[0]            # 인덱스로 삭제
print(fruits)

# 기타
print(len(fruits))       # 길이
print("사과" in fruits)  # 포함 여부
print(fruits)
fruits.sort()            # 정렬
print(fruits)
fruits.reverse()         # 역순
print(fruits)