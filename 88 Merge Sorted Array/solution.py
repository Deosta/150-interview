"""
This one just outright stumped me. I was going at it from the 0 index, not the last index of the arrays. It kind of broke my brain, but I learned.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # last index of original nums1 array
        j = n - 1  # last index of nums2 array
        k = m + n - 1  # last index of answer array (nums1 itself, including zeros)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1


        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1