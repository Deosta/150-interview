"""
Thought I had a good solution for this one. I kept getting out of index errors. Once again, I approached this incorrectly. I ended up having to view a solution.

This makes A LOT of sense to me. Assuming there will always be a value that appares more then n / 2 times, you step through the list. Starting off, set the return variable to whatever is first in the list. As it steps through the list it will 
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = 0   #contains the value to be returned
        j = 0   #count for how many times an element appares in the list.

        for num in nums:
            if j == 0:
                k = num
        
            if num == k:
                j += 1
            else:
                j -= 1

        return k