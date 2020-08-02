class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            if x & 1 != y & 1:
                res += 1
                x >>= 1
                y >>= 1
                return res
        