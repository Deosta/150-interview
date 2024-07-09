""" 
This was my first run at the solution. It was incorrect. I'm not sure why this didn't work.
It should have walked through the list and if num == val, remove it from the list.
It missed the 2 at index[7].
Input
nums =
[0,1,2,2,3,0,4,2]
val =
2
Output
[0,1,3,0,4,2]
Expected
[0,1,4,0,3]
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num == val:
                nums.remove(val)
        k = len(nums)
        return k
    
"""
I had to look at the solutions to get to this.
This works because it checks each index of nums in range of the len of the list.
If the the value at nums[i] does not match val then nums[k] = nums[i].
k is then incremented by 1 which steps through the list.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k