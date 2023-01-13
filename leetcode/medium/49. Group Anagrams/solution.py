from typing import *
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        for s in strs:
            my_map[self.simple_hash(s)].append(s)

        result = []
        for key in my_map:
            result.append(my_map[key])

        return result

    def is_anagram(self, str1, str2):
        return self.simple_hash(str1) == self.simple_hash(str2)

    def simple_hash(self, string):
        hash_val = 0
        for c in string:
            hash_val += hash(c)
        return hash_val
