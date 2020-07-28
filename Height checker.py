class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        temp = []
        for i in range(len(heights)):
            temp.append(heights[i])
        heights.sort()
        for i in range(len(heights)):
            if heights[i]!=temp[i]:
                count = count+1
        return count