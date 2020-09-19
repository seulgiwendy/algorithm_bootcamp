# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, C):
    # write your code in Python 3.6
    resultString = ""

    consecutiveCounts = {'a' : 0, 'b' : 0, 'c' : 0}

    while(A > 0 or B > 0 or C > 0):

        if A > 0 and consecutiveCounts['a'] < 2:
            A = A - 1

            consecutiveCounts['b'] = 0
            consecutiveCounts['c'] = 0

            consecutiveCounts['a'] = consecutiveCounts['a'] + 1
            resultString += 'a'
            continue

        if B > 0 and consecutiveCounts['b'] < 2:
            B = B - 1

            consecutiveCounts['a'] = 0
            consecutiveCounts['c'] = 0

            consecutiveCounts['b'] = consecutiveCounts['b'] + 1
            resultString += 'b'
            continue

        if C > 0 and consecutiveCounts['c'] < 2:
            C = C - 1

            consecutiveCounts['a'] = 0
            consecutiveCounts['b'] = 0

            consecutiveCounts['c'] = consecutiveCounts['c'] + 1
            resultString += 'c'

        else:
            if B == 1:
                return 'b' + resultString
            if B > 1:
                return 'bb' + resultString
            if C == 1:
                return 'c' + resultString
            if C > 1:
                return 'cc' + resultString

    return resultString

print(solution(7, 8, 3))
print(solution(1, 3, 0))
