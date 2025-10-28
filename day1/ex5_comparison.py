# x = 5
# y = 10

# print(x == y)  = False (같다)
# print(x != y)  = True  (다르다)
# print(x > y)   = False (크다)
# print(x < y)   = True  (작다)
# print(x >= y)  = False (크거나 같다)
# print(x <= y)  = True  (작거나 같다)

# 삼항 조건식
# if is_even:
#     print(f"{number}는 짝수입니다")
# else:
#     print(f"{number}는 홀수입니다")



number = 30

# 홀짝 판별
is_even = (number % 2 == 0) # true
print(f"{number}는 {'짝수' if is_even else '홀수'}입니다") 

# 3의 배수이면서 4의 배수인지 확인
is_multiple_of_3 = (number % 3 == 0)
is_multiple_of_4 = (number % 4 == 0)
is_both = is_multiple_of_3 and is_multiple_of_4

print(f"3의 배수: {is_multiple_of_3}")
print(f"4의 배수: {is_multiple_of_4}")
print(f"3과 4의 공배수: {is_both}")