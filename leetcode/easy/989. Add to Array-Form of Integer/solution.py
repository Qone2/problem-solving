from typing import *


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = ""
        for i in num:
            num_str += str(i)
        return list(int(c) for c in str(int(num_str) + k))
