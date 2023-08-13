'''
String Matching

Given an array of words containing n strings of the same lengths.
In one move, you can choose any position in any one string and change the letter at that position to the previous or next letter in alphabetical order. For example:
•	'c' can be changed to 'd' or 'b'.
•	'a' can only be changed to 'b'.
•	'z' can only be changed to 'y'.
Find the minimum difference over all the possible pairs of the n strings.
The difference between the two strings is the minimum number of moves required to make them equal. 
 
Example 1:
Input:
n = 5
words[] = { "cdd", "zba","dgf","xyz","mnp"}
Output: 6
Explanation:
Among all the pairs, the minimum difference 
is between the pairs ["cdd", "dgf"].
Convert 'c' to 'd' in one move.
Convert 'd' to 'g' in three moves.
Convert 'd' to 'f' in two moves.
Example 2:
Input:
n = 3
words[] = {"ab","ab","ab"}
Output: 0

Your Task:
You don't need to print or input anything. Complete the function minimum_difference() which takes integer n and words[ ] as input parameters and returns minimum possible difference.

Constraints:
•	2 <= n <= 50
•	1 <= words[i].length() <= 8
•	All strings are of same length.
•	Each string consists of lowercase English alphabet.

'''


from typing import List

class Solution:
    
    def compare_str(self, s1: str, s2: str) -> int:
        sum = 0
        for i,j in zip(s1, s2):
            sum += abs(ord(i) - ord(j))
        return sum
            
            
        
    def minimum_difference(self, n : int, words : List[str]) -> int:
        # code here
        ans = 10 ** 4
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = min(self.compare_str(words[i], words[j]), ans)
        return ans
