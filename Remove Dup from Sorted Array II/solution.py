"""
My though process here, verbaly, is this: Start by comparing 2 items in the list. If the items are equal, search the list for other duplicate items. If more than 2 duplicates, remove the extras. I will need a variable to keep track of the number of times a duplicate item appears in the list.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1     # set the starting index
        j = 1     # set the times a value will appare. Assuming every value will appare at least once setting to 1.

        for i in range(1, len(nums)):     # step through list
            if nums[i] == nums[i-1]:      # if value[i] == value[i-1] we increment the counter. otherwise set it back to 1.
                j += 1
            else:
                j = 1

            if j <= 2:                    # as long as the counter is less then or equal to 2, overwrite value. Then increment k to check the next value.
                nums[k] = nums[i]
                k += 1
        return k