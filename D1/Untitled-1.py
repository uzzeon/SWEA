## 2056번

T = int(input())

for test_case in range(1, T + 1):
    
    numbers = list(map(int, input().split()))

    year = 0
    month = 0
    day = 0
    

    year = numbers[0] // 10000
    month = (numbers[0] // 100) % 100
    day = numbers[0] % 100

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 1 <= day <= 31:
            result = f'{year}/{month}/{day}'
        else:
            result == -1

    elif month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            result = f'{year}/{month}/{day}'
        else:
            result == -1

    elif month == 2:
        if i <= day <= 28:
            result = f'{year}/{month}/{day}' 
        else:
            result == -1
    
    else:
        result == -1

print(result)    



#    result = f'{year}/{month}/{day}' 
    


        

    
  


            
#    print(f'{mid_num}') 


