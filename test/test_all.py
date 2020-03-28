from planter import Compiler, Tree


data = {
    "a": {"b": {"e": {"x": {"y": {"z": "ok"}}}}, "c": "d"},
    "g": "h",
    "i": {"j": {"k": {"l": "m"}, "y": [{"n": "ojbk"}, "kkk"]}},
}


def test_cov():
    c = Compiler()
    ret = c.compile(data)

    t = Tree(ret)
    for _ in t.bfs(t.root):
        pass
    for _ in t.loop_from_root():
        pass
    assert t.get_node("e")
    assert t.get_node("not existed") is None
    assert t.get_node_by_path(["root", "a", "b"])
    assert t.get_node_by_path(["a", "b"])
    assert t.get_nodes_by_name("b")
    assert isinstance(t.flatten(), list)
    assert not t.get_node_by_path(["unknown"])

    new_t = c.compile2tree(data)
    assert new_t.get_node("e").path == t.get_node("e").path
    assert t.get_node_by_name("a") is t.get_parent_node(t.get_node_by_name("b"))
