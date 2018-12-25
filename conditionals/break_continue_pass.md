# Looping with conditionals in Python

`for` and `while` loops are normally straightforward, but when we want to treat an item within a loop differently depending on its properties, `pass`, `continue`, and `break` affect the flow.

Imagine:

```python
for x in y:
	if x in a:
		print(x)
	else:
		print('not found')
```

## `break`

The keyword `break` terminates the _entire loop_, which means that it will not examine any remaining values. For example:

```python
for x in ['a', 'b', 'c']:
	if x == 'b':
		break
	else:
		print(x)
```

The output is just `a`; the `break` instruction means that the loop never sees the `c`.

## `continue`

The keyword `continue` terminates the current pass through the loop, which then resumes with the next value. If we replace `break` in the preceding example with `continue`:

```python
for x in ['a', 'b', 'c']:
	if x == 'b':
		continue
	else:
		print(x)
```

The output is (on separate lines) `a c`. 

## `pass`

The keyword `pass` is ignored. It may be useful as a placeholder during development in situations where indentation rules require a block to have content, such as when you want to declare a method without writing the code for it. Don’t use pass in `for` or `while` loops.

## In practice

While processing a list of tuples like:

```python
[('1859', 0, 3), ('1860', 2, 3)]
```

I want to skip over values I have already seen, which I am tracking elsewhere. The pseudo-code is:

```python
for location in locations:
	if location in alreadySeen:
		continue
	do something
	do something else
```

This causes a single location to be ignored. Using `break` instead of `continue` would have caused the entire loop to be aborted, so that no further locations would be seen, which isn’t what I want. Using `pass` would have no effect, as if the `if` clause weren’t there, which also isn’t what I want.