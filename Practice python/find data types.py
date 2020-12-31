
n = int(input())
arr = [int(x) for x in input().split()]

arr.sort()
set_arr = set(arr)
print(set_arr)
list_arr = list(set_arr)
print(list_arr)
print(list_arr[-2])
