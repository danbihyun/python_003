# person = {"name": "Kim", "age": 25}

# # 추가/수정
# person["city"] = "Seoul"   # 추가
# person["age"] = 26         # 수정

# print(person)

# # 삭제
# del person["city"]
# removed = person.pop("age")  # 삭제하고 값 반환
# print(person)
# print(removed)

# # 조회
# print(person.keys())    # 모든 키
# print(person.values())  # 모든 값
# print(person.items())   # 모든 (키, 값) 쌍

# # 순회
# for key, value in person.items():
#     print(f"{key}: {value}")



text = "python is great python is fun python is powerful"

# 단어 분리
words = text.split()

# 빈도수 계산
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1    
    else:
        word_count[word] = 1
        
print("단어 빈도수:")

for word, count in word_count.items():
    print(f"{word}: {count}번")
    
# 가장 많이 나온 단어
#max_word = max(word_count)  # 딕셔너리를 그냥 max()에 넣으면 키들 중 가장 큰 것을 반환
max_word = max(word_count, key=word_count.get)
print(f"\n가장 많이 나온 단어: {max_word} ({word_count[max_word]}번)")