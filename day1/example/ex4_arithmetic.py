# a = 10
# b = 3

# print(a + b)   = 13 (덧셈)
# print(a - b)   = 7  (뺄셈)
# print(a * b)   = 30 (곱셈)
# print(a / b)   = 3.333... (나눗셈)
# print(a // b)  = 3  (몫) ⭐ 중요
# print(a % b)   = 1  (나머지) ⭐ 중요
# print(a ** b)  = 1000 (거듭제곱)



# 물건 가격 계산
price = 15000
quantity = 5

total = price * quantity
print(f"총 가격: {total}원")

# 거스름돈 계산
payment = 100000
change = payment - total
print(f"거스름돈: {change}원")

manwon = change // 10000
print(f"만원: {manwon} 장")