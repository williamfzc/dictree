from planter import Compiler, Tree


data = {
    "a": {"b": {"e": {"x": {"y": {"z": "ok"}}}}, "c": "d"},
    "g": "h",
    "i": {"j": {"k": {"l": "m"}}},
}


def test_cov():
    c = Compiler()
    ret = c.compile(data)

    t = Tree(ret)
    for _ in t.bfs(t.root):
        pass
    for _ in t.dfs(t.root):
        pass
    assert t.get_node("e")
    assert t.get_node("not existed") is None
