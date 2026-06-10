class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort() 
        res = [] 

        # loop through the sorted list 
        for i, a in enumerate(nums): 
            # if the first number is greater than zero then 0 sum is not possible 
            if a > 0: 
                break 
            # in sorted list, skip same numbers 
            if i > 0 and nums[i - 1] == a:
                continue 

            l, r = i + 1, len(nums) - 1 
            while l < r: 
                t_sum = a + nums[l] + nums[r] 
                if t_sum < 0: 
                    l += 1 
                elif t_sum > 0: 
                    r -= 1 
                else: 
                    res.append([a, nums[l], nums[r]]) 
                    l += 1 
                    r -= 1 
                    while  nums[l] == nums[l - 1] and l < r: 
                        l += 1 
            
        return res