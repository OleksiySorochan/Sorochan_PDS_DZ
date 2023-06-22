import pytest
from tree import Node, bild

tree = [8, 3, 10, 1, 6, None, 154, None, None, 4, 7, None, None, 13, None]
t = bild(tree)

def test_find_min():
    assert t.find_min() == 1

def test_find_max():
    assert t.find_max() == 154

def test_insert():
    t.insert(200)
    assert t.find_max() == 200

def test_del_node():
    t.del_node(200)
    assert t.find_max() == 154