class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1

        hashmap = defaultdict(int)
        max_fruits = 0
        n = len(fruits)
        left = 0
        for right in range(n):
            hashmap[fruits[right]] += 1
            if len(hashmap) <= 2:
                max_len = right - left + 1
                max_fruits = max(max_fruits, max_len)
            
            while len(hashmap) > 2:
                hashmap[fruits[left]] -= 1
                if hashmap[fruits[left]] == 0:
                    hashmap.pop(fruits[left])
                left += 1

        return max_fruits