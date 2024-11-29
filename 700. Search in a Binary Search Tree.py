# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return False
        while (root):
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            else:
                return root
        return root
