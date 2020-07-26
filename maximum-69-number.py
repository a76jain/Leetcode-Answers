class Solution:
    def maximum69Number (self, num: int) -> int:
        index = ""
        for i, val in enumerate(str(num)):
            if val == "6":
                index = i
                break
        
        if index  == "":
            return num
        else:
            return num +  3 * 10 ** (len(str(num)) - 1 - index)   
                