from typing import Optional
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        @cache
        def go(u):
            if u == None:
                return 0
            
            if u.left == None and u.right == None:
                return u.val
            
            x = go(u.left) + go(u.right)
            y = u.val
            if u.left != None:
                y += go(u.left.left) + go(u.left.right)
            if u.right != None:
                y += go(u.right.left) + go(u.right.right)
            
            nonlocal ans
            ans = max(ans, x, y)
            
            return max(x, y)
        
        ans = root.val
        go(root)
        
        return ans