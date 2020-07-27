class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = ''
        for i in address:
            if i == '.':
                a += '['
                a += '.'
                a += ']'
            else:
                a += i
        
        return a
   