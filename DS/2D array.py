from typing import SupportsComplex


main_arr = []
sub_arr = []
ans_arr = []
sum_list = []

for i in range (0, 6):
    sub_arr = list(map(int, input(). split()))
    main_arr.append(sub_arr)

for i in range(0, 6):
    for j in range(0, 6):
        ans_arr = main_arr[i][j], main_arr[i][j+1], main_arr[i][j+2], main_arr[i+1][j+1], main_arr[i+2][j], main_arr[i+2][j+1], main_arr[i+2][j+2]
        print(ans_arr)
        sum_list.append(sum(ans_arr))
        print(sum_list)
        print(max(sum_list))