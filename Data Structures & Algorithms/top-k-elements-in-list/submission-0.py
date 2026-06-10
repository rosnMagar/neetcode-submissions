class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        count_map = defaultdict(int)

        for num in nums:
            count_map[num] = count_map[num] + 1 
        
        for key in count_map.keys():
            arr[count_map[key]].append(key)

        res = []

        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res





        