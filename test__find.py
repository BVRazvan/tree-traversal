from node import Node
from tree import Tree


def test__find():
    tree = Tree()

    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)

    assert tree._find(5, tree.getRoot()) is None
    assert tree._find(2, tree.getRoot()) is not None