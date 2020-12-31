n = int(input())

arr = list(map(str, input().rstrip().split()))
    
arr.reverse()

#print(arr)
seperator = " "

print(seperator.join(arr))
