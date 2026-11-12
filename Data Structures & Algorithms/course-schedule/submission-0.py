class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = []
        state = []

        def build_graph():

            for _ in range(numCourses):
                graph.append([])

            for a, b in prerequisites:
                graph[b].append(a)

            # 
            for i in range(numCourses):
                state.append(0)



        def has_cycle(course):

            if state[course] == 1: # ongoing 
                return True
            
            if state[course] == 2: # completed
                return 

            state[course] = 1

            for next_course in graph[course]:
                if has_cycle(next_course):
                    return True

            state[course] = 2


        build_graph()

        for course in range(numCourses):

            if has_cycle(course):

                return False

       

        return True
