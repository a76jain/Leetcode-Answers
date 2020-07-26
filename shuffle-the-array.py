class Solution(object):
    def shuffle(self, nums, n):
        lst = []
        for i in range(n):
            pair_lst = [nums[i],nums[i+n]]
            lst.extend(pair_lst)
        return lst