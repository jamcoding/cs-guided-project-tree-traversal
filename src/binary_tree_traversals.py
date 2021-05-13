class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value <= self.value:
            # the new value, must go left
            if self.left is None:
                # create a new node as a left child of current node
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        else:
            # the value must go right
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # let the right hand Node figure it out
                self.right.insert(value)

# pre-order traversal
def print_tree_pre_order(root):
    print(root.value)

    # if you can go left, recurse left
    if root.left:
        print_tree_pre_order(root.left)

    if root.right:
        print_tree_pre_order(root.right)

# Time -> O(n)   Space -> O(n)
def print_tree_in_order(root):
    if root.left:
        print_tree_in_order(root.left)

    print(root.value)

    if root.right:
        print_tree_in_order(root.right)

def print_tree_post_order(root):
    if root.left:
        print_tree_post_order(root.left)

    if root.right:
        print_tree_post_order(root.right)

    print(root.value)

# Time -> O(n)   Space -> O()
def breadth_first_traversal(root):
    # create the queue
    queue = []
    # add the first item to the queue
    queue.append(root)

    # if root is None:
    #     return []

    # result = []

    # process items in the queue
    while len(queue) != 0:
        # dequeue an item
        node = queue.pop(0)
        # result.append(node.val)

        print(node.value)

        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

    # return result

def depth_first_traversal(root):
    # non recursive?
    stack = []
    # add the first item to the stack
    stack.append(root)

    # process items in the stack
    while len(stack) != 0:
        # stack an item
        node = stack.pop()

        print(node.value)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

my_array = []
def generate_in_order_array(root):
    if root.left:
        generate_in_order_array(root.left)

    # print(root.value)
    my_array.append(root.value)

    if root.right:
        generate_in_order_array(root.right)

root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)

# print("---------Pre Order---------")
# print_tree_pre_order(root)

# print("---------In Order---------")
# print_tree_in_order(root)

# print("---------Post Order---------")
# print_tree_post_order(root)

# print("BFS")
# breadth_first_traversal(root)

# print("---------DFT Interative---------")
# depth_first_traversal(root)

generate_in_order_array(root)
print(my_array)