class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        idea is to iterate through the list, and check if current path == target
        if current path == target:
            append to answer
        if current path > target:
            return and backtrack
        
        '''
        ans = []
        candidates.sort()
        self.recurse(candidates, 0, ans, target, [], 0)

        return ans

    def recurse(self, candidates, index, ans, target, path, path_val):
        if path_val == target and not path in ans:
            ans.append(path[:])
        if path_val > target:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.recurse(candidates, i+1, ans, target, path, path_val + candidates[i])
            path.pop()