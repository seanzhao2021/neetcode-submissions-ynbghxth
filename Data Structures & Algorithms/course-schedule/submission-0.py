class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adj_list =[[] for _ in range(numCourses)]
        for edge in prerequisites:
            adj_list[edge[0]].append(edge[1])


        #valid dag
        checked = set()

        def dfs(course, path):
            #is course in path?
                #return false
            #is course in checked
                #return True
            if course in path:
                return False
            if course in checked:
                return True
            
            
            #add course to path
            path.add(course)

            #for each prereq in course list
                #dfs(prereq, path)
            for prereq in adj_list[course]:
                if not dfs(prereq, path):
                    return False
            
            #add course to checked
            path.remove(course)
            checked.add(course)
            #return True
            return True
  
        for i in range(numCourses):
            path = set()
            if not dfs(i, path):
                return False
        return True


        