# 종합 문제 2: 간단한 메뉴 시스템
# 다음과 같은 메뉴 시스템을 만드세요.



menu = {
    "1": "회원가입",
    "2": "로그인",
    "3": "종료"
    }
    
# 메뉴 출력
for key, value in menu.items():
    print(f"{key}. {value}")
    
# 사용자 선택 (여기서는 하드코딩)
choice = "2"

# # 선택에 따른 동작
# if choice == "1" in menu:
#     print("회원가입을 선택했습니다.")
# elif choice == "2" in menu:
#     print("로그인을 선택했습니다.")
# else:
#     print("프로그램을 종료합니다.")

# 간결하게 표현하는 법    
print(f"{menu[choice]} 버튼을 선택하셨습니다.")