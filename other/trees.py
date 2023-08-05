class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left_child = None
        self.right_child = None

    @staticmethod
    def check_node(node):
        return node is None

    def insert_left(self, newNode):
        if self.check_node(newNode):
            self.left_child = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, newNode):
        if self.check_node(newNode):
            self.right_child = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_value(self):
        return self.key

    def set_roo_value(self, new_obj):
        self.key = new_obj



