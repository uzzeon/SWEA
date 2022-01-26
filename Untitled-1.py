## 2056번


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers = str(map(int, input()))

# 0. 입력값을 int로 할지 str로 받을지? "str"
# 1. 유효성을 판단 -- 월과 일을 판단) 월은 index 4,5 일은 6, 7
    if int(numbers[4:6]) == 1:
        if 1 <= int(numbers[4:6]) <= 31:
            answer = numbers
        else:
            answer == -1

    

# 2. 유효하다면, yyyy/mm/dd 형식
# 3. 유효하지 않다면, '-1'을 출력해야 함

