class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i, ans, nums = 0, 0, sorted(nums)
        for j in range(1, len(nums)):
            if nums[i] == nums[j]: ans += (j - i)
            else: i = j
        return ans