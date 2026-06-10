class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for this just remember floyd's cycle detection algorithm

        fast, slow = 0, 0

        # since there is a duplicate this has to happen
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                return slow
