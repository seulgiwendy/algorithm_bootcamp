def longest_palindrom(string):

    string_array = list(string)

    if len(string_array) < 3:
        return 0

    if is_palindrom(string_array):
        return len(string_array)

    else:
        new_string_array = string_array[:-1]
        print(new_string_array)
        return longest_palindrom(''.join(new_string_array))


def is_palindrom(string):

    palindrome_flag = False

    for i in range(0, len(string)):

        palindrome_flag = string[i] == string[-i - 1]

    return palindrome_flag

print(longest_palindrom("토마토맛토마토"))
print(longest_palindrom("토마토맛있어"))