# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ''
        if not root: return s
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    s += str(node.val)+','
                else:
                    s += '*,'
                if node:
                    q.append(node.left)
                    q.append(node.right)
        return s
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.split(',')
        root = None
        if s == ['']: return root
        height = 0
        root = TreeNode(s[0], None, None)
        q = deque([root])
        i = 1
        while q and i < len(s):
            for _ in range(len(q)):
                node = q.popleft()
                if s[i] != '*':
                    node.left = TreeNode(s[i], None, None)
                    q.append(node.left)
                i += 1
                if s[i] != '*':
                    node.right = TreeNode(s[i], None, None)
                    q.append(node.right)
                i += 1
        return root    


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))