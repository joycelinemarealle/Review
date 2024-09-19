class TreeNode :
    def __init__(self, location):
        self.location = location
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)


    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.location)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

def build_location_tree():
    root = TreeNode("Global")

    #India Hierarchy
    India = TreeNode("India")
    Gujarat = TreeNode("Gujarat")
    Karnataka  = TreeNode("Karnataka")

    root.add_child(India)
    India.add_child(Gujarat)
    India.add_child(Karnataka)
    Gujarat.add_child(TreeNode("Ahmedabad"))
    Gujarat.add_child(TreeNode("Baroda"))
    Karnataka.add_child(TreeNode("Bangluru"))
    Karnataka.add_child(TreeNode("Mysore"))


     #USA Hierarchy
    USA = TreeNode("USA)")
    NJ = TreeNode("NJ")
    CA = TreeNode("CA")

    root.add_child(USA)
    USA.add_child(NJ)
    USA.add_child(CA)
    NJ.add_child(TreeNode("Princeton"))
    NJ.add_child(TreeNode("Trenton"))
    CA.add_child(TreeNode("SF"))
    CA.add_child(TreeNode("Mountain view"))
    CA.add_child(TreeNode("Palo Alto"))

    return root

if __name__ == '__main':
    root_node = build_location_tree()
    root_node.print_tree(3)

