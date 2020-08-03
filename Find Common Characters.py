class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        :type A: List[str]
        :rtype: List[str]
        """
        return list((reduce(lambda a,b: a & b, [Counter(word) for word in A])).elements())