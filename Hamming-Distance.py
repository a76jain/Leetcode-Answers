class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x = ""
        bin_y = ""
        count = 0
        
        while x!= 0:
            bin_x = bin_x + str(x % 2)
            x = x // 2
        bin_x = bin_x[::-1]
        
        while y!= 0:
            #mod_y = y % 2
            bin_y = bin_y + str(y % 2)
            y = y // 2
        bin_y = bin_y[::-1]
            
        if len(bin_x) > len(bin_y):
            bin_y = bin_y.zfill(len(bin_x))
        else:
            bin_x = bin_x.zfill(len(bin_y))
           
        for i in range(len(bin_x)):
                if bin_x[i] != bin_y[i]:
                    count += 1
        return count