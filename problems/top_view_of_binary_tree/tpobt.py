class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return '{} -> ({}, {})'.format(
            str(self.val),
            str(self.left),
            str(self.right)
        )


def top_view(root):
    x_to_y_node = {}

    def traverse(nd, x=0, y=0):
        if not nd:
            return
        if x not in x_to_y_node or y < x_to_y_node[x][0]:
            x_to_y_node[x] = (y, nd)
        traverse(nd.left, x - 1, y + 1)
        traverse(nd.right, x + 1, y + 1)

    traverse(root)
    xs = sorted(x_to_y_node.keys())
    result = [x_to_y_node[x][1].val for x in xs]  
    return result


if __name__ == '__main__':
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.right = Node(10)
    root.right.left = Node(7) 

    print(str(root))
    # 5 -> (3 -> (1 -> (None, None), 4 -> (None, None)), 10 -> (7 -> (None, None), None))  # noqa: E501

    print(top_view(root))
    # [1, 3, 5, 10]
