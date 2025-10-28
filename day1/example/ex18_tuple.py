# # 리스트와 비슷하지만 수정 불가 (immutable)
# point = (10, 20)
# rgb = (255, 128, 0)

# # 접근은 동일
# print(point[0])  # 10

# # 수정 불가
# point[0] = 30  # 오류!

# # 언패킹
# x, y = point
# print(x, y)  # 10 20



# 2D 좌표
point = (3, 4)
x, y = point

print(f"좌표: ({x}, {y})")

# 원점으로부터의 거리
distance = (x**2 + y**2) ** 0.5
print(f"원점으로부터 거리: {distance:.2f}")