if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
query_name = input()

query_ans = student_marks[query_name]
main_ans = sum(query_ans)/3
print ("{:.2f}".format(main_ans))



