# word = input() 
# list_even_fin, list_odd_fin =[], []

# for i in range(len(word)):

#     w_list =list(word)

#     list_even = w_list[2*i]
#     list_even_fin.append(list_even)
#     list_odd = w_list[2*i + 1] 
#     list_odd_fin.append(list_odd)
#     l_even = ""
#     l_even = l_even.join(list_even_fin)
#     l_odd = l_even.join(list_odd_fin)

# print(l_even)
# print(l_odd)

n = int(input())
for i in range(n): 
    s=input() 
    print("".join(s[::2]),"".join(s[1::2]))

# 2
# Hacker
# Word
# 2
# Hacker
# Word






