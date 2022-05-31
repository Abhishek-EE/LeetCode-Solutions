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
        queue = [root]
        """
        SLR
        Rule of thumb is if you are using a stack it is DFS
        so any recursive traversal usually will be DFS if you use a queue in the traversal it will be BFS
        so you need two loops
        while not a leaf node
        
        """
        level = 0
        levels =[]
        while len(queue)!=0:
            #start the current level
            levels.append([])
            level_len = len(queue)
            for i in range(level_len):
                levels[level].append(queue[0].val)        
                # print(queue[0].val)
                #add values in queue for next level
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
            level += 1
        
        return levels
    
        

            
        