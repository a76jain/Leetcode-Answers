class Solution:
    def numberOfSteps (self, num: int) -> int:
        count_1 = 0
        count_2 = 0
        while num > 0:
            if num % 2 == 0:
                num = num/2
                count_1 = count_1 + 1
            else:
                num = num - 1
                count_2 = count_2 + 1
        return count_1 + count_2