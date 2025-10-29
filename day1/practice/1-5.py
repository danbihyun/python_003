# 세 개의 숫자 중 가장 큰 수를 찾으세요.
# if문만 사용해서 풀기

a = 15
b = 27
c = 19

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)



#  더 나은 코드
# a = 1
# 5b = 27
# c = 19

# if a > b and a > c:
#     print(f"가장 큰 수: {a}")
# elif b > c:
#     print(f"가장 큰 수: {b}")
# else:
#     print(f"가장 큰 수: {c}")
    
# # 더 간단한 방법
# print(f"가장 큰 수: {max(a, b, c)}")