class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        hashmap = {}
        less, equal, greater = [], [], []
        ans = []
        for num in nums:
            if num < pivot:  
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)

        print(less, greater, equal)
        for l in less:
            ans.append(l)
        for e in equal:
            ans.append(e)
        for g in greater:
            ans.append(g)
        return ans