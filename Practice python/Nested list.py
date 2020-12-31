n = int(input())
main_list, A_list = [], []
name_list = []
score_list = []
draw_list = []

for i in range(n):
    name = input()
    name_list.append(name)

    score = float(input())
    score_list.append(score)
    
    
    A_list = [score, name]
    main_list.append(A_list)
    sort_sl = sorted(main_list)
    # print(sort_sl)

# print(sort_sl[1][1])

if sort_sl[1][1] == sort_sl[2][1]:
    draw_list.append(sort_sl[1][1])
    draw_list.append(sort_sl[2][1])
    draw_list = draw_list.sort()
    print(draw_list)
    
    






















# print(main_list)