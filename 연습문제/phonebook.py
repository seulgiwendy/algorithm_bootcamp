def solution(phone_book):
    answer = True

    prefix_hash = {}

    for number in phone_book:
        if number in prefix_hash:
            return False
        prefix_hash[number] = 1

    for prefix in prefix_hash:
        pass


    return answer

def listify_number(number):

    for i in range(len(number)):
        pass
    pass

print solution(["12", "123", "1235", "567", "88"])