# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        ret = []
        
        def traversal(node):
            nonlocal ret
            if node is None:
                return 
            traversal(node.left)
            ret.append(node.val)            
            traversal(node.right)
        
        traversal(root1)
        traversal(root2)
        return sorted(ret)
            
        
