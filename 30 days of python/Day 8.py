# # Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# dictt = {}
# l1 = []

# for x in range (n):
#     name, number = input().split()
#     dictt[name] = number
#     name_list = list(dictt.keys())
#     num_list = list(dictt.values())
#     # print(name_list)
# # print(name_list)

# for i in range (n):
#     temp = input()
#     l1.append(temp)
    
# # print(l1)

# for i in range(len(l1)):
#     if l1[i] in name_list: 
#         print(name_list[i] + "=" + num_list[i])
#     else:
#         print("Not found")

# Enter your code here. Read input from STDIN. Print output to STDOU
n, d = int(input()), dict()

for i in range(0, n):
    name, number = input().split()
    d[name] = number
    
for i in range(0,n):
    checker = input()
    if checker in d:
        print("{}={}".format(checker, d[checker]))
    else:
        print("Not found")
        
    


# print(dictt)
