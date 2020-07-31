class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        # If t2 is empty, return t1 and if t1 is empty, return t2
        if not(t2):
            return t1
        elif not(t1):
            return t2
        
        # A queue for FIFO operations
        queue = [[t1, t2]]
        
        while queue:
            len_queue = len(queue) 
            
            for _ in range(len_queue):
                n1, n2 = queue.pop(0)
                n2.val += n2.val
                
                if not(n1.left) and n2.left:
                    n1.left = n2.left
                elif n1.left and n2.left:
                    queue.append([n1.left, n2.left])

                if not(n1.right) and n2.right:
                    n1.right = n2.right
                elif n1.right and n2.right:
                    queue.append([n1.right, n2.right])
            
        return t1