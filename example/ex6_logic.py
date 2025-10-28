# a = True
# b = False

# print(a and b)  = False (둘 다 참이어야 참)
# print(a or b)   = True  (하나만 참이어도 참)
# print(not a)    = False (반대)

# # 실전 예시
# age = 20
# has_license = True
# can_drive = (age >= 18) and has_license  # True



# 복리 이자 계산 (원금, 이율, 기간)
principal = 2500000  # 원금 250만원
rate = 0.032          # 연 3.2%
years = 1           # 1년

# 복리 공식: A = P(1 + r)^t
final_amount = principal * (1 + rate) ** years
interest = final_amount - principal

print(f"원금: {principal:,}원")
print(f"이율: {rate * 100}%")
print(f"기간: {years}년")
# :,.0f → 소수점 생략, 반올림 + 콤마 구분
print(f"최종 금액: {final_amount:,.0f}원")
print(f"이자: {interest:,.0f}원")

# 2배가 되는 기간 계산 (72의 법칙)
doubling_time = 72 / (rate * 100)
print(f"원금이 2배가 되는 기간: 약 {doubling_time:.1f}년")