# planter

compile dict (json/yaml/toml/everything) to tree

## what is it?

Dictionary is quite a good data structure, but not programmable enough.

```python
data = {
    "a": {"b": {"e": {"x": {"y": {"z": "ok"}}}}, "c": "d"},
    "g": "h",
    "i": {"j": {"k": {"l": "m"}}},
}
```

and if i gonna call `z`, i need to:

```python
data["a"]["b"]["e"]["x"]["y"]["z"]
```

or loop:

```python
for k, v in data.items():
    for i, j in v.items():
        for k, l in j.items():
            # ...
```

looks very weird. However, with this repo:

```python
from planter import Compiler, Tree

c = Compiler()
# Node object
root_node = c.compile(data)
# Tree object
tree = Tree(root_node)
```

now you have already converted it into a `Tree` object which was built with some `Node`s.
and you can operate these nodes easily, eg: depth first search?

```python
for each_node in tree.dfs(root):
    print(each_node.name)

    # and its depth
    print(each_node.depth)
    # ...
```

output:

```text
root
0
a
1
b
2
e
3
x
4
y
5
i
1
j
2
k
3
```

it is flexible and extendable.

What's more, actually JSON/YAML or something like that, can be easily converted into python dictionary.

## License

[MIT](LICENSE)
