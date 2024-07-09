# First one I was able to do without looking at the solution!!! YES!!

# 1. Compare needle to haystack, if needle isn't in haystack return -1
# 2. Otherwise, return the index where needle is first found in haystack

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        return haystack.find(needle)