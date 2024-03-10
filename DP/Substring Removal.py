'''
Hackerank Problem asked in the interview coding round of JP Morgan & Chase

1. Substring Removal

Given a string, seq, that consists of the characters 'A' and 'B' only, in one move, delete either an "AB" or a "BB" substring and
concatenate the remaining substrings.

Find the minimum possible length of the remaining string after performing any number of moves.

Note: A substring is a contiguous subsequence of a string.

Example
seq = "BABBA"

Using 0-based indexing, the following moves
are optimal.

· Delete the substring "AB" starting at index
1. "BABBA"-> "BBA"
. Delete the substring "BB" starting at index 0.
"BBA"-> "A"

Sample Case 1

Sample Input For Custom Testing

FUNCTION

seq = "AABBBAB"

STDIN

AABBBAB

Sample Output

1

Explanation
'''

def remove_substring(s, index):
  return s[:index] + s[index + 2 ::]

def get_sequences(s):
  seq = []
  i = 0
  while i < len(s):
    j = i+1
    if j < len(s):
      if s[i] == "A" and s[j] == "B":
        seq.append(i)
      if s[i] == "B" and s[j] == "B":
        seq.append(i)
    i += 1
  return seq

def get_min_len(s):
  seq = get_sequences(s)
  if len(seq) == 0:
    return len(s)
  
  seqSet = set()
  for j in seq:
    seqSet.add( remove_substring(s, j) )
  print(seqSet)
  minLen = float('inf')
  for i in seqSet:
    minLen = min(minLen, get_min_len(i))
  return minLen

s = "AABBBABB"
print(get_min_len(s))
