# count = 0

# while count < 5:
#     print(count)
#     count += 1


# # break: 반복문 종료
# for i in range(10):
#     if i == 5:
#         break    
#     print(i)  # 0, 1, 2, 3, 4
    
# # continue: 다음 반복으로
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)  # 0, 1, 3, 4




# 소수 판별
for number in range(1, 18):
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False            
                print(f"{number}는 {i}로 나누어떨어짐")
                break
    if is_prime:
        print(f"{number}는 소수입니다")
    else:
        print(f"{number}는 소수가 아닙니다")