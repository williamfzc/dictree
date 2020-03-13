import typing
import queue


class Node(object):
    def __init__(self, name: str, parent_name: str, depth: int, *_, **__):
        self.name: str = name
        self.parent_name: str = parent_name
        self.depth: int = depth

        self.sub_nodes: typing.List[Node] = []


class Compiler(object):
    NODE_KLS: typing.Type[Node] = Node
    ROOT_NODE_NAME: str = "root"

    def compile(self, data: dict) -> Node:
        def _compile(
            cur_data: dict, depth: int, cur_name: str, parent_name: str = None
        ) -> Node:
            cur_node = self.NODE_KLS(cur_name, parent_name, depth)
            for k, v in cur_data.items():
                # node
                if isinstance(v, dict):
                    sub_node = _compile(v, depth + 1, k, cur_name)
                    cur_node.sub_nodes.append(sub_node)
                # kwargs
                else:
                    cur_node.__dict__[k] = v
            return cur_node

        return _compile(data, 0, self.ROOT_NODE_NAME, None)


class Tree(object):
    def __init__(self, root: Node):
        self.root: Node = root

    def dfs(self, from_node: Node):
        # depth first
        def _loop(node: Node):
            yield node
            for each in node.sub_nodes:
                yield from _loop(each)

        return _loop(from_node)

    def bfs(self, from_node: Node):
        # init queue
        q = queue.Queue()
        q.put(from_node)

        def _clear(target_queue, output_queue):
            while not target_queue.empty():
                new_node = target_queue.get()
                yield new_node
                # and send its sub nodes to output
                for each in new_node.sub_nodes:
                    output_queue.put(each)

        while not q.empty():
            tmp = queue.Queue()
            yield from _clear(q, tmp)
            q = tmp
