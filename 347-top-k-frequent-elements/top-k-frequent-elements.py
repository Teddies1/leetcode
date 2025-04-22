class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        hashmap = dict(sorted(hashmap.items(), key=lambda x: x[1], reverse=True))
        ans = []

        for key, val in hashmap.items():
            if k == 0:
                return ans
            ans.append(key)
            k -= 1

        return ans