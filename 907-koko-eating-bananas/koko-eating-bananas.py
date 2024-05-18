class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        ans = max_speed
        sum = 0
        while min_speed <= max_speed:
            mid = ((max_speed - min_speed) // 2) + min_speed
            sum = 0
            for pile in piles:  
                hours = ceil(pile / mid)
                sum += hours
            if sum > h:
                min_speed = mid + 1
            else:
                max_speed = mid - 1
                
        return min_speed
    