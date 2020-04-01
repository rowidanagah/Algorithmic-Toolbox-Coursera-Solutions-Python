class Node :
    def __init__(self , data):
        self.data = data 
        self.rightchild = None
        self.leftchild = None
    

class Tree: ## binary search tree<<<<<BST>>>>
    def __init__(self):
        self.root = None
    def insert(self , data):
        node =  Node(data)
        if not self.root : ## it's an empty tree
            self.root = node
        else :
            curr = self.root
            parent = None ### to keep track of the following root
            while True :
                parent = curr 
                if parent.data > data:
                    curr = curr.leftchild
                    if not curr :
                        parent.leftchild = node
                        return
                else :
                    curr = curr.rightchild
                    if not curr:
                        parent.rightchild = node
                        return
        
    def get_parent_with_node(self , data): ### tp detect which node and parent we gonna paly with
        curr = self.root 
        parent = None
        if not curr: ###en empty tree
            return parent , None
        while True :
            if curr.data == data :
                return (parent , curr)
            elif curr.data > data :
                parent = curr
                curr =  curr.leftchild
            else :
                parent = curr
                curr = curr.righthild
        return (parent , curr)
    
    def delet(self , data):
        parent , node = self.get_parent_with_node(data)
        if not node and not parent :
            return False
        ## to determine with case we are in 
        child_no = 0
        if node.rightchild and node.leftchild:
            child_no = 2
        elif not node.rightchild or not node.leftchil :
            child_no = 1
        else :
            child_no = 0
#---------------------<<<case1>>>>><<<no child>>>>--------------
        if child_no == 0 :
            if parent : ### not root
                if parent.leftchild == node :
                    parent.rightchild = None
                else :
                    parent.rightchild = None
            else :
                self.root = None
#---------------------<<<case2>>>>><<<one child>>>>--------------
        elif child_no == 1 :
            next_node = None
            if node.leftchild :
                next_node = node.leftchild
            else :
                next_node = node.rightchild
            if parent :
                if parent.leftchild == node:
                    parent.leftchild = next_node
                else :
                    parenct.rightchild = next_node
            else:
                self.root = next_node
#---------------------<<<case3>>>>><<<2 children>>>>--------------
       ### else :
        ###not yet
    
    def inorder(self):
        curr = self.root
        if not curr :
            return 
        self.inorder(curr.leftchild)
        print(curr.data)
        self.inorder(curr.rightchild)
    def preorder(self):
        curr = self.root
        if not curr :
            return 
        print(curr.data)
        self.inorder(curr.leftchild)
        self.inorder(curr.rightchild)
    def postorder(self):
        curr = self.root
        if not curr :
            return
        print(curr.data)
        self.inorder(curr.leftchild)
        self.inorder(curr.rightchild)
    def BFS(self):
        Q = [self.root]
        list_of_nodes = []
        while Q :
            node = Q.pop(0)
            list_of_nodes.append(node.data)
            if node.leftchild :
                list_of_nodes.append(node.leftchild)
            if node.rightchild :
                list_of_nodes.append(node.rightchild)
        return list_of_nodes
    def find_min(self):
        curr = self.root
        while curr.leftchild:
            curr = curr.leftchild

        return curr
    def find_max(self):
        curr = self.root
        while curr.rightchild :
            curr = curr.rightchild
        return curr
    def search(self , data):
        curr = self.root
        while True :
            if not curr :
                return False
            elif curr.data == data :
                return data
            elif curr.data > data :
                curr = curr.leftchild
            else :
                curr = curr.rightchild
        return -1
    
    