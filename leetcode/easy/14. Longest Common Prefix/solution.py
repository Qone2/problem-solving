from typing import *


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for st in strs:
            i = -1
            for i in range(min(len(answer), len(st))):
                if answer[i] != st[i]:
                    i -= 1
                    break
            answer = answer[:i + 1]

        return answer
