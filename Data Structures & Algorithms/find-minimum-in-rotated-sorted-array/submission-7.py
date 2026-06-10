class Solution:

    def findMin(self, nums: List[int]) -> int:

        lo, hi = 0, len(nums) - 1
        res = nums[lo]
        while lo <= hi:

            if nums[lo] < nums[hi]:
                res = min(res, nums[lo])
                break

            mid = (hi + lo) // 2
            
            if nums[lo] <= nums[mid] and nums[hi] < nums[mid]:
                lo = mid + 1
            else:
                if nums[mid-1] > nums[mid]:
                    res = nums[mid]
                    break
                else:
                    hi = mid - 1

        return res
        
        