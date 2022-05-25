# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if the current element is same if yes then check if left tree and right tree are same other wise
        return false
        """
        if (p == None and  q == None):
            return True
        if (p == None and q != None):
            return False
        if (p != None and q == None):
            return False
        truthValue = False
        if(p.val == q.val):
            truthValue = self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        return truthValue
            
        