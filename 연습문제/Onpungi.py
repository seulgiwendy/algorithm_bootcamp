def solution(office, k):
    middle_list = []
    sub_list = []

    for i in range(0, len(office) - k + 1):
        for j in range(i, i + k - 1):
            for y in range(0, k):
                print(j, y)
                sub_list.append(office[j][y])
                middle_list.append(sub_list)

    print middle_list
    answer = 0
    return answer


print solution([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]], 2)