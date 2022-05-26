# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p == None and q ==None):
            return True
        if(p != None and q == None):
            return False
        if(p == None and q != None):
            return False
        truthValue = False
        if(p.val == q.val):
            truthValue = self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
        return truthValue
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root == None):
            return False
        if(self.isSameTree(root,subRoot)):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
            
            
            
        
        