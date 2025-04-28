class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        idea is to construct a graph from the courses
        use adj list
        adj list map prerequisites to the courses

        # [[1,0],[2,0],[3,1],[3,2]]

        we have adj list
        [0] => [1, 2]
        [1] => [3]
        [2] => [3]
        
        from adj list, can construct a list of indegrees
        each index of the list i represents the number of prerequisites course i requires

        using indegree list, perform topological sort

        add nodes with no indegrees to queue (no indegree = no prerequisites so must take this course first)
        pop from queue
        add to course order

        remove all outdegrees of this node
        check indegree list if any new nodes have 0 indegrees
            if yes add to queue
        repeat until no more nodes

        '''
        adj_list = {}
        indegree = [0] * numCourses
        course_ordering = []

        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        # build adj_list
        for course, prerequisite in prerequisites:
            if prerequisite in adj_list:
                adj_list[prerequisite].append(course)
            else:
                adj_list[prerequisite] = [course]
        
        for prereq, outdegrees in adj_list.items():
            for outdegree in outdegrees:
                indegree[outdegree] += 1

        # perform topological sort
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            course = queue.pop()
            course_ordering.append(course)
            if course in adj_list:
                for c in adj_list[course]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        queue.append(c)

        return course_ordering if len(course_ordering) == numCourses else []