# 리스트에서 짝수만 골라내는 함수를 만드세요.

def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))