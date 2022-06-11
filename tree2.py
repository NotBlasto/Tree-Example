class Node:
        def __init__(self, name):
                self.name = name
                self.children = []

        def add_child(self, child_name):
                child_node = Node(child_name)
                self.children.append(child_node)

        def find_child(self, child_name):
                for child in self.children:
                        if child.name == child_name:
                                return child
                else:
                        return None

class Tree:
    def __init__(self):
        self.root = Node('root')

    def find(self, node_path):
        current_node = self.root
        tokens = node_path.split('.')
        # print(f"FINDING: {tokens}")
    
        for token in tokens:
            next_node = current_node.find_child(token)
            if next_node is None:
                raise NameError(f"Cannot find node {token} on {current_node.name}")
            # print(next_node.name)
            current_node = next_node

        return current_node

    def add(self, new_child, on_node=None):
        # If no parent node is specified, put child on root
        if on_node is None:
            parent = self.root
        else:
            tokens = on_node.split('.')
            # the specified parent must exist
            parent = self.find(on_node)
        parent.add_child(new_child)


# EXAMPLE
tree = Tree()

print("<find|add> node  (or quit)")
while True:
    raw = input(">> ")
    if raw == 'quit':
        break

    command, target = raw.split(' ')
    if command == 'find':
        try:
            found = tree.find(target)
            print(f"Found {found.name}")
        except NameError as e:
            print(e)
    elif command == 'add':
        # get the name of the new item (last part of path)
        new_node = target.split('.')[-1]
        # get the rest of the path
        path = '.'.join(target.split('.')[:-1])
        if not path:
            path = None
        try:
            tree.add(new_node, path)
        except NameError as e:
            print(e)
    else:
        print(f"Unknown command {command}")

