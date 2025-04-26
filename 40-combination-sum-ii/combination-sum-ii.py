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
            return
        if path_val > target:
            return

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.recurse(candidates, i+1, ans, target, path, path_val + candidates[i])
            path.pop()

    '''
    [1,1,2,5,6,7,10]
    dry run:
    recurse:
        index = 0, target = 8, path = [], pathval = 0
    for i in range(0, len(candidates))
    path = [1]
    recurse:
        index = 1, path = [1], pathval = 1
    for i in range(1, len(candidates))
        candidates[1] == candidates[0]
        continue
        path = [1, 2]
    recurse:
        index = 3, path = [1, 2], pathval = 3
    for i in range(3, len(candidates))
        path = [1, 2, 5]
    recurse:
        index = 4, path = [1, 2, 5], pathval = 8
    pathval == target
    ans = [[1,2,5]]
    return



    
    '''