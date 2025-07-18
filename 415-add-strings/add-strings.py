class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1 or not num2:
            raise ValueError
        ans = ""
        num1 = num1[::-1]
        num2 = num2[::-1]

        num1_len, num2_len = len(num1), len(num2)
        num1_ptr, num2_ptr = 0, 0

        carry = 0
        while num1_ptr < num1_len or num2_ptr < num2_len or carry == 1:
            digit1 = int(num1[num1_ptr]) if num1_ptr < num1_len else 0
            digit2 = int(num2[num2_ptr]) if num2_ptr < num2_len else 0

            intermediate_sum = digit1 + digit2 + carry
            if intermediate_sum > 9:
                carry = 1
            else:
                carry = 0

            ans += str(intermediate_sum % 10)

            num1_ptr += 1
            num2_ptr += 1

        return ans[::-1]
