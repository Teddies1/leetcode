class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        if not plants:
            return 0
        curr_cap = capacity
        total_steps = 0
        n = len(plants)
        if n == 0:
            return 0

        for i in range(n):
            required_water = plants[i]
            total_steps += 1
            curr_cap -= required_water

            if i + 1 < n and plants[i+1] > curr_cap:
                total_steps += ((i+1) * 2)
                curr_cap = capacity
    

        return total_steps