class Solution(object):
    def flipAndInvertImage(self, A):
        return [list(reversed([1 if j==0 else 0 for j in i])) for i in A]
