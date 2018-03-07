def longest_palindrom(string):

    string_array = list(string)

    if len(string_array) < 3:
        return 0

    palindroms = []

    for i in range(0, len(string_array)):
        for j in range(1, len(string_array) + 1):

            if string_array[i:j] == string_array[i:j][::-1]:
                palindroms.append(len(string_array[i:j]))

    return max(palindroms)






