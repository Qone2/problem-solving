class Solution:
    def addBinary(self, a: str, b: str) -> str:
        low = ""
        high = ""
        if len(a) > len(b):
            high = a[::-1]
            low = b[::-1]
        else:
            high = b[::-1]
            low = a[::-1]

        answer = ""
        carry = 0
        for i in range(len(low)):
            tmp_sum = int(low[i]) + int(high[i])
            tmp_sum += carry
            answer += str(tmp_sum % 2)
            carry = 1 if tmp_sum >= 2 else 0

        for i in range(len(low), len(high)):
            tmp_sum = int(high[i]) + carry
            answer += str(tmp_sum % 2)
            carry = 1 if tmp_sum >= 2 else 0

        if carry == 1:
            answer += '1'

        return answer[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("1111", "1111"))
