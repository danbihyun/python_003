1. 파이썬에서 콘솔에 출력하는 경우 : print()  
   문자열을 출력하는 경우 : print("")  
   문자열과 변수를 함께 출력하는 경우 : print(f"")  
   (f가 없을 경우 변수명이 그대로 출력됨)

```py
# 나이: 24세
print(f"나이: {age}세")
# 나이: {age}세
print("나이: {age}세")
```

```py
# 출력결과
나이: 24세
나이: {age}세
```

---

2. try - except문은 Java의 try - catch문과 흡사함.  
   try 문에서 코드가 죽어버리는 것을 막기 위해 except문을 추가해 줌.  
   try문만 단독으로 사용할 순 없다.

```py
try:
    number = float(user_input)
    print(f"변환 성공: {number}")
    print(f"타입: {type(number)}")

    # 정수부와 소수부 분리
    integer_part = int(number)
    decimal_part = number - integer_part
    print(f"정수부: {integer_part}, 소수부: {decimal_part:.2f}")
except ValueError:
    print("숫자가 아닙니다!")
```

---

3. 파이썬에서 거듭제곱을 나타내는 연산자는 : \*\*

```py
a = 10
b = 3

# 10x10x10
print(a ** b)  = 1000
```

---

4. 파이썬에서 if / else if / else 는 if / elif / else 로 표기.  
   또한 중괄호로 블럭을 잡지 않고 들여쓰기 4칸으로 상/하위를 나눔.  
   들여쓰기는 3칸도 2칸도 아닌 4칸이어야 적용됨!

```py
number = 72

if number > 0:
    print(f"{number}는 양수입니다")
elif number < 0:
    print(f"{number}는 음수입니다")
else:
    print("0입니다")
```

---

5.  파이썬에서의 for문

```py
for 변수명 in range(시작, 끝):
    print(...)
```

```py
# 1 ~ 9단 출력

for dan in range(2, 10):
    print(f"=== {dan}단 ===")

    for i in range(1, 10):
        result = dan * i
        print(f"{dan} x {i} = {result}")
    print()  # 단 사이에 빈 줄 추가
```

6. 리스트 (List)

```py
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(data[2:5])    # [2, 3, 4] (인덱스 2 ~ 5까지, 5는 잘림)
print(data[ :3])     # [0, 1, 2] (처음부터 3까지, 3은 잘림)
print(data[5: ])     # [5, 6, 7, 8, 9] (5부터 끝까지)
print(data[ : :2])    # [0, 2, 4, 6, 8] (처음부터 끝까지, 2칸씩 점프)
print(data[ : :-1])   # [9, 8, 7, ... , 0] (처음부터 끝까지, 역순)
```

```py
1. 끝에 추가할 때 : 변수명.append("내용")
2. 특정 위치에 추가할 때 : 변수명.insert(인덱스 번호, "내용")
3. 여러 내용을 추가할 때 : 변수명.extend(["내용1", "내용2"])

4. 특정 값을 삭제할 때 : 변수명.remove("내용")
5. 마지막 요소 삭제 후 반환할 때 : 변수명1 = 변수명2.pop()
6. 인덱스 번호로 삭제할 때 : del 변수명[인덱스 번호]
```

---

7. Comprehension

```py
# [표현식 for 변수 in 반복가능한객체]
# [표현식 for 변수 in 반복가능한객체 if 조건식]

squares = []

for i in range(10):
    squares.append(i ** 2)

# 리스트 컴프리헨션 (한 줄로 표현하는 식)
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 조건 포함
evens = [i for i in range(20) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

8. 튜플 (Tuple) - 수정이 불가한 리스트의 개념

```py
# 리스트와 비슷하지만 수정 불가 (immutable)
point = (10, 20)
rgb = (255, 128, 0)

# 접근은 동일
print(point[0])  # 10

# 수정 불가
point[0] = 30  # 오류!

# 언패킹
x, y = point
print(x, y)  # 10 20
```

```py
# 예제

# get_student_info() 에 각각의 변수명과 값을 저장
def get_student_info():
    name = "김철수"
    age = 20
    grade = "A"
    score = 95
    return (name, age, grade, score)

# 튜플(언패킹) - 각각의 변수명에 값을 차례대로 자동배분함
student_name, student_age, student_grade, student_score = get_student_info()

print(f"이름: {student_name}")
print(f"나이: {student_age}")
print(f"학점: {student_grade}")
print(f"점수: {student_score}")
```

```py
# 출력결과
이름: 김철수
나이: 20
학점: A
점수: 95
```
