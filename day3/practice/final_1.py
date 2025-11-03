# 종합 문제 1: 성적 처리 프로그램
# 학생들의 점수를 입력받아 다음을 출력하는 프로그램을 만드세요.
# - 총점
# - 평균
# - 최고점
# - 최저점
# - 평균 이상인 학생 수



students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "정지원": 88,
    "최동욱": 95
    }

total = sum(students.values())
avg = total / len(students)
count = sum(1 for score in students.values() if score >= avg)
# count = 0
# for score in students.values():
#     if score >= avg:
#         count += 1
    
print(f"총점 : {total}")
print(f"평균 : {avg:.1f}")
print(f"최고점 : {max(students.values())}")
print(f"최저점 : {min(students.values())}")
print(f"평균 이상인 학생 수 : {count}명")