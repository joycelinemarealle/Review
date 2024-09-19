class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        #assign parent
        child.parent = self
        #add child which is also a node to array
        self.children.append(child)

    def print_tree(self):
        #get level to determine space. space times level
        spaces = ' ' * self.get_level() *3
        prefix = spaces + "|__" if self.parent else""

        #search every node in list and print data with space based on level
        print(prefix + self.data)
        #if node has children then recursively call print_tree
        if len(self.children) >0:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        # count number of ancestors to get levels'
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level



def build_product_tree():
    root = TreeNode('Electronics')
    # node after root
    laptop = TreeNode('Laptop')
    #children of node laptop
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    #node after root
    cellphone = TreeNode ("Cell Phone")
    #add children to cellphone
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    #node
    tv = TreeNode("TV")
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    #add the three children to root electronics
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass