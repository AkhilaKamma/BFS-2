#------------------BFS Approach -----------------------
#Time Complexity: O(N)
#Space Complexity: O(N)
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            temp_list = []
            for i in range(size):
                node = queue.popleft()
                temp_list.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(temp_list[-1])  
        return result

#------------DFS Approach-----------------
#Time Complexity: O(N)
#Space Complexity: O(1) + O(H) is the recursive stack space
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.result = []
        self.helper(root,0)
        return self.result
        
    def helper(self,root, level):

        if root is None:
            return
        if len(self.result) == level:
            self.result.append(root.val)

        self.helper(root.right, level + 1)
        self.helper(root.left, level + 1)
        
