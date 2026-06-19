class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's Algorithm
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        s1 = 0
        s2 = slow
        while True:
            s1 = nums[s1]
            s2 = nums[s2]
            if s1 == s2:
                return s1