class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
         

        nodes = []


        def build_graph():
            
            for _ in range(n):
                nodes.append([])

            for a, b in edges:

                nodes[a].append(b)
                nodes[b].append(a)


        def dfs(node, visited):

            stack = [node]
            visited.add(node)

            while stack:

                curr = stack.pop()

                for neighbour in nodes[curr]:

                    if neighbour in visited:
                        continue
                    else:
                        visited.add(neighbour)
                        stack.append(neighbour)


        def connected_components():

            visited = set()
            count = 0

            for node in range(n):

                if node not in visited:

                    count += 1
                    dfs(node, visited)
                    visited.add(node)

            return count
        
        build_graph()
        print(nodes)
        return connected_components()

