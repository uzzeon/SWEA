## 2056번

T = int(input())

for test_case in range(1, T + 1):
    
    numbers = list(map(int, input().split()))
    mid_num = numbers[len(numbers)//2]
            
    print(f'{mid_num}') 


