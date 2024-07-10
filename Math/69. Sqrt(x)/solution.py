# I had NO clue how to approach this without the use of built-in exponent operator. This is NOT my solution.
# 1 If x is 0, return 0.
# 2 Initialize first to 1 and last to x.
# 3 While first is less than or equal to last, do the following:
#     a. Compute mid as first + (last - first) / 2.
#     b. If mid * mid equals x, return mid.
#     c. If mid * mid is greater than x, update last to mid - 1.
#     d. If mid * mid is less than x, update first to mid + 1.
# 4 Return last.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last