# 1. Initialize a variables to hold the value to be moved to the front of the list and the while loop counter
# 2. Itterate through the array
# 3. Remove the value at the last index
# 4. Put the stored value at the front of the list
# 5. Do this k number of times

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #initialize variables to hold value at last index and while loop counter
        moved_value, i = nums[-1], 1

        #loop while i <= k, remove last index, insert stored value at start of list, set holder to new value at last index, finally increment the counter.
        while i <= k:
            nums.pop()
            nums.insert(0, moved_value)
            moved_value = nums[-1]
            i += 1