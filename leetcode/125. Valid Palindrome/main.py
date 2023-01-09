from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 덱 선언
        deq = deque()
        for c in s:
            if c.isalpha() or c.isnumeric():
                deq.append(c)
        while deq:
            c1 = deq.popleft()
            if not deq:
                return True
            c2 = deq.pop()
            if c1 != c2:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
