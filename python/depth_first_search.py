from logging import root


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == None:
            self.data = data
        else: 
            if data

def sum_roots(root):
    if root == None:
        return 0
    return root.data + sum_roots(root.left)+ sum_roots(root.right)


# let structure of tree be this:
#         2
#       /   \
#      3     4
#     / \
#    5   6
node2= Node(2) 
node3= Node(3)
node4= Node(4)
node5= Node(5)
node6= Node(6)

node2.left = node3
node2.right = node5
node3.left = node4
node3.right = node5

print('The total sum of the tree starts from 2 is:', sum_roots(node2))

# now we can perform a depth first search and print all the nodes that we had visited
def dfs(tree):
    if tree == None:
        return
    else:
        if tree.left:
            dfs(tree.left)
        print(tree.data, end = '')
        
        if tree.right:
            dfs(tree.right)
        
print(dfs())



    