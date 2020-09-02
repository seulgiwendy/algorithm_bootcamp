import math


class Solution:
    def is_palindrome(self, x: int) -> bool:
        digits = self.decide_digits(x, 0)
        print("digits: {d}".format(d=digits))
        figures_in_reverse = self.get_digit_figures(x, digits)

        for i in range(0, digits // 2):
            compared_index = digits - i - 1

            if figures_in_reverse[i] != figures_in_reverse[compared_index]:
                return False

        return True

    def decide_digits(self, x: int, retry_count: int) -> int:
        divider = math.pow(10, retry_count)

        if x // divider == 0:
            return retry_count

        return self.decide_digits(x, retry_count + 1)

    def get_digit_figures(self, x: int, digits: int):
        digits_in_reverse_order = []
        for i in range(1, digits + 1):
            divider = math.pow(10, i)
            remainder = x % divider
            digits_in_reverse_order.append(remainder // math.pow(10, i - 1))

        return digits_in_reverse_order


print(Solution().is_palindrome(1221))
print(Solution().is_palindrome(1234321))
print(Solution().decide_digits(x=10000, retry_count=0))
