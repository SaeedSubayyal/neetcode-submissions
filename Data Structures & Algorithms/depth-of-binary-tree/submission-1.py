class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        stack = [(root,1)]
        max_depth = float('-inf')

        while stack:

            curr, depth = stack.pop()

            max_depth = max(depth, max_depth)
            
            if curr.left:
                stack.append((curr.left,depth+1))

            
            if curr.right:
                stack.append((curr.right,depth+1))

        
        return max_depth










        