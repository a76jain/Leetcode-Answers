class Solution:
    def sortString(self, s: str) -> str:
        ans = []
		s=list(s)
        res=[]
        count=0
        finish =1
        while True:
            if s:
                ans =[]
                new_set = list(set(s))
                if finish%2 ==1:
                    new_set.sort()
                elif finish%2==0:
                    new_set.sort(reverse=True)
                for j in new_set:
                    ans.append(j)
                finish +=1
                for k in ans:
                    s.remove(k)
                res.extend(ans)
            else:
                break
        return "".join(res)
                