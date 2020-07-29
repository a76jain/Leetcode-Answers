class Solution:
    def sortString(self, s: str) -> str:
        d = {i:0 for i in s}
        for i in s:
            d[i]+=1
            
        sort_d = sorted(d)
        result = []
        i = 0
        
        while i!=len(s):
            
            for j in sort_d:
                if d[j]:
                    result+=[j]
                    d[j]-=1
                    i+=1
                    
            for j in sort_d[::-1]:
                if d[j]:
                    result+=[j]
                    d[j]-=1
                    i+=1
                    
        return ''.join(result)