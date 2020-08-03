class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        pending = []
        for i in arr1:
            if i not in arr2:
                pending.append(i)
        for i in arr2:
            for j in arr1:
                if i == j:
                    res.append(j)
        pending = sorted(pending)
        for i in pending:
            res.append(i)
        
        return(res)