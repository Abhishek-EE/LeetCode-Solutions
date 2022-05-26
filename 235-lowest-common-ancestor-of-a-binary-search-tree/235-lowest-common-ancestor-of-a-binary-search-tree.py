# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isInTree(self,root:'TreeNode',p:'TreeNode'):
        if(root == None ):
            return False
        if(root == p):
            return True
        return self.isInTree(root.left,p) or self.isInTree(root.right,p)
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        find which side p is in 
        find which side q is in 
        if they are in the same side recursively look in that side
        else return root
        """
        if(root == None):
            return 
        if(root == p or root == q):
            return root
        p_in_left = self.isInTree(root.left,p)
        q_in_left = self.isInTree(root.left,q)
        if(p_in_left == q_in_left):
            if(p_in_left):
                return self.lowestCommonAncestor(root.left,p,q)
            else:
                return self.lowestCommonAncestor(root.right,p,q)
        return root
        
        