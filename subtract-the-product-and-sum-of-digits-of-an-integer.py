class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_of_digits = 0
        while(n>0):
            product *= n % 10
            sum_of_digits += n % 10
            n = n // 10 
            
        return product - sum_of_digits 
        