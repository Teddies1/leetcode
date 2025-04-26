class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        idea is we have a list of candidates
        each time we choose a number, and then recursively choose the same number
        at each recursion step, we check if the current path == target
        if yes
            append path to answer
        if path > target
            exceeded target, return and choose another path
        
        for all elements in candidates
            add this element to path
            recurse
            backtrack
    
        '''
        ans = []
        
        self.recurse(candidates, ans, target, [], 0, [])

        return ans

    def recurse(self, candidates, ans, target, path, path_val, counter_array):
        if path_val == target and not Counter(path) in counter_array:
            counter_array.append(Counter(path))
            ans.append(path[:])
        if path_val > target:
            return

        for candidate in candidates:
            path.append(candidate)
            self.recurse(candidates, ans, target, path, path_val + candidate, counter_array)
            path.pop()

        