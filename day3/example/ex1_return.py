# def greet(name):
#     """인사 함수"""    
#     print(f"안녕하세요, {name}님!")
    
# greet("홍길동")  # 안녕하세요, 홍길동님!



# def add(a, b):
#     return a + b
    
# result = add(3, 5)
# print(result)  # 8

# # 여러 값 반환
# def get_stats(numbers):
#     total = sum(numbers)
#     avg = total / len(numbers)
#     return total, avg
    
# total, avg = get_stats([1, 2, 3, 4, 5])
# print(f"합계: {total}, 평균: {avg}")  # 합계: 15, 평균: 3.0



def rectangle_area(width, height):
    """직사각형 넓이 계산"""    
    return width * height
    
def rectangle_perimeter(width, height):
    """직사각형 둘레 계산"""    
    return 2 * (width + height)
    
# 사용
w = 5
h = 3
area = rectangle_area(w, h)
perimeter = rectangle_perimeter(w, h)

print(f"가로: {w}, 세로: {h}")
print(f"넓이: {area}")
print(f"둘레: {perimeter}")