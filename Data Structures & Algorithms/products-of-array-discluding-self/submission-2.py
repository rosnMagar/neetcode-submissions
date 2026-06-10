class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two pass method

        cpy = nums.copy()
        prev = 1
        for i in range(1, len(nums)):
            tmp = nums[i]
            nums[i] = prev * nums[i - 1]
            prev = tmp

        nxt = 1
        nums[0] = 1
        for j in range(len(cpy) - 2, -1, -1):
            tmp = cpy[j]
            cpy[j] = nxt * cpy[j + 1]
            nums[j] = nums[j] * cpy[j] 
            nxt = tmp
        
        return nums
