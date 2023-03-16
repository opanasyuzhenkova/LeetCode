# 106. Construct Binary Tree from Inorder and Postorder Traversal

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right

    def __repr__(self):
        if not self.left and not self.right:
            return "{}".format(self.val)
        else:
            return "{} {} {}".format(self.val, self.left, self.right)


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        root_val = postorder.pop()      
        root = TreeNode(root_val)
        separating_index = inorder.index(root_val)
        root.right = self.buildTree(inorder[separating_index + 1:], postorder)
        root.left = self.buildTree(inorder[:separating_index], postorder)
        return root


test = Solution()
print(test.buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]))
