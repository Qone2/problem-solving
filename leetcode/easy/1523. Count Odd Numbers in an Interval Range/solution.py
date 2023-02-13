class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        if diff % 2 == 1:
            return diff // 2 + 1
        if low % 2 == 1:
            return diff // 2 + 1
        else:
            return diff // 2
