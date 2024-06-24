"""
My solution was incorrect. I kept getting an index out of range error.
i+1 was always going to throw an error when it got to the last list item for i.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    nums.remove(j)
                    k += 1
        return k
"""
Had to look at the answers. I was itterating thorugh the list at i +1, not i -1.
This is an accepted answer. It starts at the 1 index and compares that with i - 1 until the len of the list is reached.
"""
class Solution:
    def removeDuplicates(self, nums):
        k = 1  # Initialize the count of unique elements to 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Overwrite the next unique element
                k += 1
        
        return k