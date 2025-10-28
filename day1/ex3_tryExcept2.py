# 문자열을 ASC|| 로 변환
user_input2 = "A"

try:
    input_str = ord(user_input2)
    print(f"출력 : {input_str}")

    input_str2 = float(user_input2)
    print(f"출력 : {input_str2}")
except:
    print("숫자가 아닙니다")