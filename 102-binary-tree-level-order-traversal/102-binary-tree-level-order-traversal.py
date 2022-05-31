# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = collections.deque([root,])
        level = 0
        levels =[]
        while queue:
            #start the current level
            levels.append([])
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                levels[level].append(node.val)      
                # print(queue[0].val)
                #add values in queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return levels
    
        

            
        