# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        else:
            if p is None or q is None:
                return False
            

        stack_p = [p]
        stack_q = [q]


        res_p = []
        res_q = []

        res_p.append(p.val)
        res_q.append(q.val)
        while stack_p:

            curr = stack_p.pop()

            if curr.left:
                stack_p.append(curr.left)
                res_p.append(curr.left.val)
            else:
                res_p.append(None)

            if curr.right:
                stack_p.append(curr.right)
                res_p.append(curr.right.val)
            else:
                res_p.append(None)
        

        while stack_q:

            curr = stack_q.pop()

            if curr.left:
                stack_q.append(curr.left)
                res_q.append(curr.left.val)
            else:
                res_q.append(None)

            if curr.right:
                stack_q.append(curr.right)
                res_q.append(curr.right.val)
            else:
                res_q.append(None)
    

        if res_p == res_q:
            return True
        else:
            return False


