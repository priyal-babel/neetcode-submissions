# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def max_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
                
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            return 1 + max(left_depth, right_depth)
            
        max_depth(root)
        
        return self.max_diameter