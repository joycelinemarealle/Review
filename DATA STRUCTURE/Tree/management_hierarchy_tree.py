class TreeNode:

    #each node has name, designation , maybe children and parents
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    #add child to node
    def add_child(self, child):
        #each child node has parent attribute whether present or absent
        child.parent = self
        self.children.append(child)

    def print_tree(self, choice):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""  # if root no print out

        if choice == "name":
            print(prefix + self.name)
        elif choice == 'designation':
            print(prefix + self.designation)
        else:
            print(prefix + self.name + '' + self.designation)


        #if node has children, recursively loop through all children
        #while array not empty
        if len(self.children )> 0:
            for child in self.children:
                child.print_tree(choice)

    def get_level(self):
        level = 0
        p = self.parent
        while p: #while there is a parent
            level +=1
            p = p.parent #parent has a parent
        return level


def build_management_tree():
    #Level 0
    root = TreeNode("Nilupul", "(CEO")

    #Level 1.py
    CTO = TreeNode("ChinMay", "(CTO)")
    HR = TreeNode ("Gel", "(HR Head)")
    root.add_child(CTO)
    root.add_child(HR)

    #Level 2
    InfraHead = TreeNode("Vishwa", "(Infrastructure Head")
    AppHead = TreeNode("Aamir", "(Application Head")
    RecruMgr = TreeNode("Peter", "(Recruitment Manager")
    PoliMgr = TreeNode("Waqas", "(Policy Manager")
    CTO.add_child(InfraHead)
    CTO.add_child(AppHead)
    HR.add_child(RecruMgr)
    HR.add_child(PoliMgr)

    #Level 3
    CloMgr = TreeNode("Dhaval", "Cloud Manager")
    AppMgr = TreeNode("Abhijit", "App Manager")
    InfraHead.add_child(CloMgr)
    InfraHead.add_child(AppMgr)

    return root



if __name__ == '__main__':
    root = build_management_tree()

    print('Name Tree')
    root.print_tree("name")

    print("\nDesignation Tree")
    root.print_tree("designation")

    print("\nName and Designation Tree")
    root.print_tree("both")