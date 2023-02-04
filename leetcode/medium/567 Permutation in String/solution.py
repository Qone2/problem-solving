from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        is_in = False
        for i in range(0, len(s2) - len(s1) + 1):
            if self.is_permutation(s1, s2[i:i + len(s1)]):
                is_in = True
        return is_in

    def is_permutation(self, s1: str, s2: str) -> bool:
        hashtable1 = defaultdict(int)
        hashtable2 = defaultdict(int)
        for c in s1:
            hashtable1[c] += 1
        for c in s2:
            hashtable2[c] += 1
        return hashtable1 == hashtable2


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))
    print(sol.checkInclusion("ab", "eidboaoo"))
    print(sol.checkInclusion("adc", "dcda"))
