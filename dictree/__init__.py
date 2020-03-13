import typing


class Node(object):
    def __init__(self, name: str, parent_name: str, *_, **__):
        self.name: str = name
        self.parent_name: str = parent_name

        self.sub_nodes: typing.List[Node] = []


class Compiler(object):
    NODE_KLS: typing.Type[Node] = Node
    ROOT_NODE_NAME: str = "root"

    def compile(self, data: dict) -> Node:
        def _compile(cur_data: dict, cur_name: str, parent_name: str = None) -> Node:
            cur_node = self.NODE_KLS(cur_name, parent_name)
            for k, v in cur_data.items():
                # node
                if isinstance(v, dict):
                    sub_node = _compile(v, k, cur_name)
                    cur_node.sub_nodes.append(sub_node)
                # kwargs
                else:
                    cur_node.__dict__[k] = v
            return cur_node

        return _compile(data, self.ROOT_NODE_NAME, None)


if __name__ == "__main__":
    d = {
        "a": {
            "b": {
                "e": 1
            },
            "c": "d"
        },
        "g": "h",
        "i": {
            "j": "k",
        }
    }
    c = Compiler()
    ret = c.compile(d)
    print(ret.sub_nodes)
