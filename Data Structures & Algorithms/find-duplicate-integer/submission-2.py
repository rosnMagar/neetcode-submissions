class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        curr = 0 
        res = -1

        while True:
            if nums[curr] == curr or nums[curr] == -1:
                res = curr
                break
            tmp = nums[curr] 
            nums[curr] = -1
            curr = tmp
        
        return res