# Python: Flatten a list of lists

## Logic

```python
forest = [[1, 2, 3], [4, 5, 6]]
flattened = []
for tree in forest:
	for leaf in tree:
		flattened.append(leaf)
```

## Nested list comprehension

```python
flattened = [leaf for tree in forest for leaf in tree]
```

Perhaps counterintuitively, the `for ... in` statements follow the same order as in the nested `for` version, which ensures that all variables are defined before being referenced.

## `itertools` functions

See <https://stackoverflow.com/questions/5239856/asterisk-in-function-call>.

### `itertools.chain()`

```python
import itertools
flattened = itertools.chain(*forest)
```

`flattened` is an interator. If necessary, expand it with `list(flattened)`.

The splat takes a list as input and expands it into positional arguments in a function call.

### `itertools.chain.from_iterable()`

```python
flattened = itertools.chain.from_iterable(forest)
```

Also produces an iterator, as above.

