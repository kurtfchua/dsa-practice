from collections import deque

class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def traverse(self, node):
        if not node:
            return
        
        self.traverse(node.left)
        self.traverse(node.right)
        print(node.val)
    
    def find_bst(self, node, val):
        if not node: 
            return False 
        if val == node.val:
            return True
        elif val < node.val:
            return self.find_bst(node.left, val)
        else:
            return self.find_bst(node.right, val)
    
    def insert(self, node, val):
        # recursively call on either left or right child of root until we reach none
        # at none we create a new Tree node with val

        # base-case
        if not node:
            return TreeNode(val)
        
        # recursive calls
      
        if val < node.val:
            node.left = self.insert(node.left, val)
        elif val > node.val:
            node.right = self.insert(node.right, val)
        
        return node
    
    def remove(self, node, val):
        pass

    def dfs_inorder(self, node):
        if not node:
            return
        self.dfs_inorder(node.left)
        print(node.val)
        self.dfs_inorder(node.right)
    
    def dfs_preorder(self, node):
        if not node:
            return node

        print(node.val)
        self.dfs_preorder(node.left)
        self.dfs_preorder(node.right)
    
    def dfs_postorder(self, node):
        if not node:
            return node
        self.dfs_postorder(node.left)
        self.dfs_postorder(node.right)
        print(node.val)
    
    def bfs(self, node):
        queue = deque()

        if node:
            queue.append(node)

        while len(queue) > 0:
            for i in range(len(queue)):
                current = queue.popleft()
                print(current.val)
                # add children to queue
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)


    



root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
#root.traverse(root)

root = TreeNode(2)
root1 = TreeNode(1)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)

root.left = root1
root.right = root3
root3.right = root4
root4.right = root5
#root.traverse(root)
print(root.find_bst(root, 5)) # True
print(root.find_bst(root, 1)) # True
print(root.find_bst(root, 15)) # False
print(root.find_bst(root, 0)) # False
