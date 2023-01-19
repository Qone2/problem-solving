from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        # 덱 선언
        deq = deque()
        for c in s:
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
    solution = Solution()
    print(solution.isPalindrome(-121))
