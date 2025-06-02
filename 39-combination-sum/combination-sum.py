class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        idea is to maintain some value, and keep adding candidates until we meet or exceed target
        if exceed, then remove candidates and try other candidates 

        use backtracking + recursion to do this
        
        '''
        ans = []
        # perform recursion
        def recurse(candidates, target, current_value, index, path, ans):
            # index to keep track of which candidate we are processing
            # base case, current_value > target, then return
            if current_value > target:
                return
            if current_value == target:
                ans.append(path[:])
            n = len(candidates)

            # iterate through the candidates and add it to path
            for i in range(index, n):
                path.append(candidates[i])
                recurse(candidates, target, current_value + candidates[i], i, path, ans)
                path.pop()
        
        recurse(candidates, target, 0, 0, [], ans)
        return ans