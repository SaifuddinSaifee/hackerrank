# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.


n = int(input())
main_list = []

for i in range(n):
    commd, *line = input().split()
    ints = list(map(int, line))

    if commd == "insert": 
        main_list.insert(ints[0], ints[1])
    if commd == "print":
        print(main_list)
    if commd == "remove":
        main_list.remove(ints[0])
    if commd == "append":
        main_list.append(ints[0])
    if commd == "sort":
        main_list.sort()
    if commd == "pop":
        main_list.pop()
    if commd == "reverse":
        main_list.reverse()
