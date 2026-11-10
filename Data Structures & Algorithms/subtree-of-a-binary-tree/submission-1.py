# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  

    def sameTree(self,root,subroot):

        stack = [(root, subroot)]
        while stack:
            a, b = stack.pop()
            if a is None and b is None:
                continue

            if a is None or b is None:
                return False

            if a.val != b.val:
                return False 
            
            stack.append((a.left,b.left))
            stack.append((a.right,b.right))
        
        return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        stack = [root]


        while stack:
            curr = stack.pop()
            
            if curr.val == subRoot.val:
               flag =  self.sameTree(curr,subRoot)
               if flag == True:
                return True

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return False
