#This one was simple. I probably didn't solve it in the most efficient way, but it works well.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #convert passed int to str
        txt = str(x)
        #assign variable to the reverse of the passed int
        reverse_txt = txt[::-1]
        #compare strings, if the same, return true
        if txt == reverse_txt:
            return True