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
        self.recurse(candidates, 0, ans, target, [], 0)

        return ans

    def recurse(self, candidates, index, ans, target, path, path_val):
        if path_val == target:
            ans.append(path[:])
            return
        if path_val > target:
            return

        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.recurse(candidates, i, ans, target, path, path_val + candidates[i])
            path.pop()

        