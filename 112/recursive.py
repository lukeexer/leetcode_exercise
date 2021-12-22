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
        
        targetSum = targetSum - root.val
        
        if root.left is None and root.right is None:
            if targetSum == 0:
                return True
            else:
                return False

        if root.left is None:
            return self.hasPathSum(root.right, targetSum)
            
        elif root.right is None:
            return self.hasPathSum(root.left, targetSum)
        
        else:
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
