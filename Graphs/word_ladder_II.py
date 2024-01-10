# code : https://leetcode.com/problems/word-ladder-ii/
# resource : https://takeuforward.org/graph/g-30-word-ladder-ii/
from queue import Queue
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # st = set(wordList)
        # q = Queue()
        # q.put([beginWord]) # insert the 1st seq
        # usedOnLevel = [] # keep track of how many string are used
        # usedOnLevel.append(beginWord)
        # level = 0
        # ans = []

        # while not q.empty():
        #     vec = q.get()
        #     # remove all the words that has been used in the prev level
        #     if len(vec) > level: # for eg, initialy it's [bat] and q.get() gives [bat, cat]
        #         level += 1
        #         for it in usedOnLevel:
        #             if it in st: 
        #                 st.remove(it)
            
        #     word = vec[-1]
        #     if word == endWord:
        #         # the first seq where we reached end
        #         if len(ans) == 0:
        #             ans.append(vec)
        #         elif len(ans[0]) == len(vec):
        #             ans.append(vec)

        #     for i in range(len(word)):
        #         og = word[i]
        #         for ch in range(ord('a'), ord('z') + 1):
        #             j = chr(ch)
        # # Convert val to list and modify the character at index i
        #             temp = list(word)
        #             temp[i] = j
        #             new_word = ''.join(temp)
        #             if new_word in st:
        #                 vec.append(new_word)
        #                 q.put(vec[:])
        #                 #mark visited on that level
        #                 usedOnLevel.append(new_word)
        #                 vec.pop()
        #     return ans

        st = set(wordList)
        
        # Initialize a queue to store sequences.
        q = deque()
        q.append([beginWord])
        
        # List to keep track of words used on a level.
        used_on_level = [beginWord]
        level = 0
        
        # List to store the resultant transformation sequences.
        ans = []
        
        while q:
            vec = q.popleft()
            
            # Remove words used in previous levels.
            if len(vec) > level:
                level += 1
                for word in used_on_level:
                    st.discard(word)
                used_on_level = []
            
            word = vec[-1]
            
            # Store the sequences when endWord is found.
            if word == endWord:
                if not ans or len(ans[0]) == len(vec):
                    ans.append(vec[:])
            
            for i in range(len(word)):
                for ch in range(ord('a'), ord('z') + 1):
                    new_word = word[:i] + chr(ch) + word[i+1:]
                    
                    if new_word in st:
                        used_on_level.append(new_word)
                        vec.append(new_word)
                        q.append(vec[:])
                        vec.pop()
        
        return ans

    # Comparator function to sort the answer.
    def comp(self, a: List[str], b: List[str]) -> bool:
        x = ''.join(a)
        y = ''.join(b)
        return x < y


        
