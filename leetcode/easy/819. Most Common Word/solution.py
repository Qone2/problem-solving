from collections import defaultdict
from typing import *


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para1 = ""
        for c in paragraph:
            para1 += c
            if c in [",", ".", "?", "!"]:
                para1 += " "
        para = ""
        for c in para1:
            if c.isalpha() or c.isdigit() or c == " ":
                para += c.lower()

        dic = defaultdict(int)
        para = para.strip()
        para = para.replace("  ", " ")
        for s in para.split(" "):
            if s.strip() not in banned:
                dic[s.strip()] += 1

        maxv = 0
        maxk = ""
        for key in dic:
            if dic[key] > maxv:
                maxv = dic[key]
                maxk = key
        return maxk
