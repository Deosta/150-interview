# #Wrong, yet again. Had to look at the solution.

# #1. Use two pointers, one for each string.
# 2. Traverse t with the pointer. Anytime a character in t matches the current character in s, move the pointer in s to the next character.
# 3. if the pointer for s reaches the end of s, then all characters in s have to be in string t in the correct order. 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_s = 0
        p_t = 0

        while p_t < len(t):
            if p_s < len(s) and s[p_s] == t[p_t]:
                p_s += 1
            p_t += 1
        
        return p_s == len(s)