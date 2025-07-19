class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        n = len(time)
        if n == 0:
            return 0
        ans = 0

        hashmap = [0] * 60
        for tim in time:
            mod_value = tim % 60
            hashmap[mod_value] += 1
        
        ans += (hashmap[0] * (hashmap[0] - 1)) // 2
        ans += (hashmap[30] * (hashmap[30] - 1)) // 2

        for i in range(1, 30):
            ans += (hashmap[i] * hashmap[60-i])

        return ans
