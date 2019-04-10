flat = [("d", "b"), ("c", "a"), ("b", "r"), ("a", "r"), ("e", "b"), ("r", None)]


class Node(object):
    def __init__(self, id, pid):
        self.id = id
        self.pid = pid
        self.parent = None
        self.children = []
        self.ancestors = None
        self.level = None

    def __str__(self):
        s = f"{self.id}:{'.'.join([n.id for n in self.ancestors])}({self.level})"
        if self.children:
            s += f" -> ({[str(c) for c in self.children]})"
        return s


def make_tree(a):
    r = None
    nodes = {nid: Node(id=nid, pid=pid) for nid, pid in a}
    for n in nodes.values():
        p = nodes.get(n.pid)
        n.parent = p
        if p:
            p.children.append(n)
        else:
            r = n
    return r


def update_ancestors(node, anc=[]):
    for c in node.children:
        anc_new = anc.copy() + [node]
        update_ancestors(c, anc_new)
    node.ancestors = anc
    node.level = len(anc)


root = make_tree(flat)
update_ancestors(root)
print(root)
