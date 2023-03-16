# 129. Sum Root to Leaf Numbers

from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, root, sum):
        if not root:
            return 0
        sum = sum * 10 + root.val
        if not root.left and not root.right:
            return sum
        return self.dfs(root.left, sum) + self.dfs(root.right, sum)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

result = Solution()
print(result.sumNumbers(root))