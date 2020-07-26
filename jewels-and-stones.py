class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in range(len(S)):
            if S[i] in J:
                count += 1
        return count 
		