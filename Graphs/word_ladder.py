# code : https://leetcode.com/problems/word-ladder/
# resource : https://www.youtube.com/watch?v=tRPda0rcf8E

from queue import Queue
class Solution:
'''

Initialization:

Import the Queue class for BFS traversal.
Create a queue (q) to store words along with their sequence lengths.
Convert wordList to a set (st) for efficient lookup and removal operations.
Add beginWord along with its sequence length of 1 to the queue (q).
If beginWord exists in st, remove it to avoid revisiting.

BFS Traversal:

Begin the BFS traversal loop (while not q.empty()).
Dequeue a word (val) along with its sequence length (seq) from the front of the queue (q).
Check if the dequeued word (val) is equal to the endWord. If it is, return its sequence length (seq) as the result.

Generating Neighbors:

For each character at every position in the dequeued word (val), generate a new word by replacing that character with all possible lowercase alphabets (a to z).
Convert val to a list (temp) to modify the character at the current position (i).
Replace the character at index i with a new character from the alphabet.
Convert the modified list back to a string (new_word).

Checking and Enqueuing Neighbors:

Check if the newly generated word (new_word) exists in the st set (indicating it hasn't been visited yet).
If new_word exists in st, remove it from the set to mark it as visited and enqueue it into the queue (q) along with its sequence length (seq + 1).

Termination:

If the BFS traversal completes without finding endWord, return 0, indicating that there is no transformation sequence from beginWord to endWord in wordList.

'''

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = Queue()
        q.put((beginWord, 1))
        st = set(wordList)
        if beginWord in st:
            st.remove(beginWord)

        while not q.empty():
            val, seq = q.get()
            if val == endWord:
                return seq

            for i in range(len(val)):
                og = val[i]
                for ch in range(ord('a'), ord('z') + 1):
                    j = chr(ch)
        # Convert val to list and modify the character at index i
                    temp = list(val)
                    temp[i] = j
                    new_word = ''.join(temp)
                    if new_word in st:
                        st.remove(new_word)
                        q.put((new_word, seq + 1))
                

        return 0


        
