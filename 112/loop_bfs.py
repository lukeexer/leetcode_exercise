# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        
        queue = [(root, targetSum)]
        
        while queue:
            node, sum = queue.pop(0)
            
            if node.left is None and node.right is None:
                if (sum - node.val) == 0:
                    return True
                
            if node.left:
                queue.append((node.left, sum - node.val))
                
            if node.right:
                queue.append((node.right, sum - node.val))
                
        return False
       
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
