# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        '''
        perform level order traversal to retrieve all levels'
        for each level, check if it is sorted
        if yes, continue
        else, check for number of operations to make array sorted

        for ^, can perform cyclic sort to array, and keep track of nubmer of operations needed
        '''

        # level order traversal
        ans =  0
        queue, levels = [], []
        queue.append(root)

        while queue:
            level = []
            n = len(queue)
            for _ in range(n):
                curr_node = queue.pop(0)
                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            levels.append(level)

        def is_sorted(array):
            return array == sorted(array)

        def num_operations(array):
            '''
            maintain hashmap to keep track of array indices
            have a sorted version of array which contains correct index positions

            for each element, check if element is in correct position, if no then swap
            '''
            num_operations = 0
            hashmap = {}
            sorted_arr = sorted(array)
            for i, num in enumerate(array):
                hashmap[num] = i

            for desired_index, num in enumerate(sorted_arr):
                if array[desired_index] != sorted_arr[desired_index]:
                    current_index = hashmap[num]
                    array[desired_index], array[current_index] = array[current_index], array[desired_index]

                    hashmap[array[desired_index]] = desired_index
                    hashmap[array[current_index]] = current_index

                    num_operations += 1

            return num_operations

        # for each level
        for lev in levels:
            # check for sorted
            if not is_sorted(lev):
                # check operations if not sorted
                ans += num_operations(lev)

        return ans


