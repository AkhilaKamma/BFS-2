#Time Complexity: O(N)
#Space Complexity: O(N)

from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False

        queue = deque([(root, None)])  # (node, parent)

        while queue:
            size = len(queue)
            x_parent = y_parent = None

            for _ in range(size):
                node, parent = queue.popleft()

                if node.val == x:
                    x_parent = parent
                elif node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            # After processing one level
            if x_parent and y_parent:
                return x_parent != y_parent  # Same depth, different parents
            if x_parent or y_parent:
                return False  # One found without the other -> not same depth

        return False