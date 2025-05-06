class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        index_map = {}
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] in index_map:
                index_map[nums[i]].append(i)
            else:
                index_map[nums[i]] = [i]
        print(index_map)
        for key, v in index_map.items():
            for i in range(len(v)-1):
                for j in range(i+1, len(v)):
                    if (v[i] * v[j]) % k == 0:
                        print(v[i], v[j])
                        ans += 1
        
        return ans

