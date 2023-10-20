# code -> https://leetcode.com/problems/search-suggestions-system/description/
# resource -> https://www.youtube.com/watch?v=D4T2N0yAr20
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        n = len(products)
        left, right = 0, n-1
        res = []
        for i in range(len(searchWord)):
            c = searchWord[i]
            while left <= right and (i >= len(products[left]) or products[left][i] != c):
                left += 1       

            while left <= right and (i >= len(products[right]) or products[right][i] != c):
                right -= 1 
                

            res.append([])
            remain = right - left + 1
            for j in range(min(remain, 3)):
                res[-1].append(products[left + j])
        return res

        
