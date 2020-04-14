if __name__ == '__main__':
    n = int(input())
    print(n)
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        print(name,line)
        scores = list(map(float, line))
        print(scores)
        student_marks[name] = scores
        print(student_marks)
    query_name = input()


    def check(student_marks, query_name):
        if query_name in student_marks.keys():
            res = student_marks[query_name]
            a=sum(res)
            a=a/3
            print('%.2f'%a)

    check(student_marks, query_name)