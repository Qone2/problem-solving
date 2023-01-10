from typing import *


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


if __name__ == "__main__":
    sol = Solution()
    arr = ["a", "s", "d"]
    sol.reverseString(arr)
    print(arr)
