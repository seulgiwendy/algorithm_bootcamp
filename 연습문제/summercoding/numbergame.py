def solution(A, B):
    ateam_numbers = sorted(A)
    bteam_numbers = sorted(B)

    if bteam_numbers[-1] <= A[0]:
        return 0

    return find_bigger(ateam_numbers, bteam_numbers)



def find_bigger(a_array, b_array):

    winning_point = len(b_array)

    for i in range(len(b_array)):
        if a_array[i] >= b_array[i]:
            winning_point -= 1

    return winning_point


print(solution([14, 15, 18, 17], [20, 21, 25, 24]))



