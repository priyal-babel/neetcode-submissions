from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        # While there are still nodes to process in the queue
        while queue:
            # Take a snapshot of how many nodes are on the current level
            level_size = len(queue)
            current_level = []
            
            # Process strictly that many nodes
            for _ in range(level_size):
                # Pop the node from the front of the line
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add its children to the back of the line for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # The level is finished, append the sublist to our final result
            result.append(current_level)
            
        return result