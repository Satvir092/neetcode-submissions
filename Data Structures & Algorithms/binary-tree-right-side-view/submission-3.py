# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:

            return []

        output = []

        queue = deque()

        queue.append(root)

        output.append(root.val)

        while queue:

            trav = []

            for i in range(len(queue)):

                node = queue.popleft()

                if node.left:

                    trav.append(node.left.val)
                    queue.append(node.left)

                if node.right:

                    trav.append(node.right.val)
                    queue.append(node.right)

            if trav:

                output.append(trav[-1])

        return output


