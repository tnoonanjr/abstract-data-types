##################
##################          WORK IN PROGRESS
##################
class TreeNode:
    ''' 

    Each node in a binary tree has to initialize three instance variables:
        - its value
        - the node to its left 
        - the node to its right

                  
    To include the height of a node, you can recursively call the height of 
    the node's children with the base case that its child is none. If a 
    child is None, its height is considered -1. The function returns 1 plus 
    the maximum height of the children, representing the height of the 
    current node's subtree.


    In pre-order traversal:
        - Visit the current node.
        - Recursively traverse the current node's left subtree.
        - Recursively traverse the current node's right subtree.


    In in-order traversal:
        - Recursively traverse the current node's left subtree.
        - Visit the current node.
        - Recursively traverse the current node's right subtree.

        
    In post-order traversal: 
        - Recursively traverse the current node's left subtree.
        - Recursively traverse the current node's right subtree.
        - Visit the current node.
        
    '''
    def __init__(self, key):
        ''' Initialize the three main pieces of information '''
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        ''' Give the object a representation '''
        return f"key: {self.key} Left: {self.left} Right: {self.right}"

    def height(self):
        if self is None:
            return -1
        left_height = self.left.height()
        right_height = self.right.height()
        return 1 + max(left_height, right_height)
    
    def pre_order_trav(self):
        result = []
        self._pre_order_trav(result)
        return result

    def _pre_order_trav(self, result): 
        result.append(self.key)
        if self.left:
            self.left._pre_order_trav(result)
        if self.right:
            self.right._pre_order_trav(result)

    def in_order_trav(self):
        result = []
        self._in_order_trav(result)
        return result
    
    def _in_order_trav(self, result):
        if self.left:
            self.left._in_order_trav(result)
        result.append(self.key)
        if self.right:
            self.right._in_order_trav(result)
    
    def post_order_trav(self):
        result = []
        self._post_order_trav(result)
        return result
    
    def _post_order_trav(self, result):
        if self.left: 
            self.left._post_order_trav(result)
        if self.right:
            self.right._post_order_trav(result)
        result.append(self.key)
        
class BinarySearchTree:
    '''
    A binary search tree is a sorted binary tree in which the root node is 
    greater than all values in the right subtree and less than all values 
    in the left subtree.

    init

    First and foremost, to initialize the BST, you must define 
        - a root node, from which all nodes originate. 

    It is also helpful to define 
        - a size to keep track of number of nodes. 

    '''
    def __init__(self):
        ''' initialize root node '''
        self.root = None
        self._size = 0

    def recursive_search(self, x, key):
        ''' check for membership recursively '''
        if x == None or key == x.key:
            return x
        
        if key < x.key:
            # key is less than x
            return BinarySearchTree.recursive_search(x.left, key)
        else: 
            # key is greater than x 
            return BinarySearchTree.recursive_search(x.right, key)
    
    def iterative_search(self, x, key):
        ''' check for membership iteratively '''
        while x != None and x.key != key:
            if key < x.key:
                x = x.left
            else:
                x = x.right

    def tree_map(self):
        pass




if __name__ == '__main__':
    # Initialize a Node
    node = TreeNode(8)
    print(f"NODE:\n {node}")
    #
    #                      
    #          8           
    #         / \          
    #      None None       
    #                      
    #

    # Give the node left and right children
    print("Adding children...")
    node.left = TreeNode(6)
    node.right = TreeNode(9)
    print(f"TREE AT NODE:\n {node}")
    #
    #                      
    #          8           
    #         / \          
    #        6   9         
    #                      
    #



    # Initialize a binary tree of numbers one to five
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result_pre = root.pre_order_trav()
    result_in = root.in_order_trav()

 
    expected_result_pre = [1, 2, 4, 5, 3]
    expected_result_in = [4, 2, 5, 1, 3]
    # 
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    print(result_pre)
    print(result_in)
    assert result_pre == expected_result_pre
    assert result_in == expected_result_in