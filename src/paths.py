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
            
def get_paths(root):
    paths_array = []
    def print_paths(root, path):
        new_path = path + [root.value]
        if not root.left and not root.right:
            paths_array.append(new_path)
        # print(new_path)
        # if you can go left, recurse left
        if root.left:
            print_paths(root.left, new_path.copy())

        if root.right:
            print_paths(root.right, new_path.copy())

    print(root, [])
    return paths_array

def depth_first_traversal(root):
    paths_array = []
    # non recursive?
    stack = []
    # add the first item to the stack
    stack.append((root, []))

    # process items in the stack
    while len(stack) != 0:
        # stack an item
        node, path = stack.pop()

        new_path = path + [node.value]
        print(new_path)

        if node.right:
            stack.append((node.right, new_path.copy()))

        if node.left:
            stack.append((node.left, new_path.copy()))
    
    return paths_array


root = BSTNode(8)
root.insert(5)
root.insert(4)
root.insert(7)
root.insert(12)
root.insert(11)
root.insert(13)

# print_paths(root, [])
# print(paths_array)

depth_first_traversal(root)