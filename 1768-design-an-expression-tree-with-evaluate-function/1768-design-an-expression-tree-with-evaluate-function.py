import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class CreateTree(Node):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def evaluate(self):
        if self.val == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == '/':
            return self.left.evaluate() // self.right.evaluate()
        else:
            return self.val
        


"""     
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for e in postfix:
            if not e.isnumeric():
                right = stack.pop()
                left = stack.pop()
                node = CreateTree(e, left, right)
                stack.append(node)
            else:
                node = CreateTree(int(e))
                stack.append(node)
        
        return stack[0]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        