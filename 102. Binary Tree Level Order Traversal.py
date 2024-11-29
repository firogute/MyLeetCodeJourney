
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        if root:
            queue.append(root)

        level = 0
        while len(queue) > 0:
            cur = []
            for i in range(len(queue)):
                curNode = queue.popleft()
                if curNode:
                    cur.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            if cur:
                res.append(cur)
        return res
