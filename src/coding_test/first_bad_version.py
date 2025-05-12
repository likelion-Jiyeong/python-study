class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            mid = (start + end) // 2
            
            if isBadVersion(mid) == False:
                start = mid + 1
            else:
                end = mid - 1
        return start