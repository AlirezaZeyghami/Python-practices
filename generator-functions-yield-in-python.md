# Python Generators

## Why Generators?
- **Functions with `return`** store the whole result in memory → not efficient for large datasets.
- **Generators with `yield`**:
  - Use less memory (lazy evaluation).
  - Return values **one by one** as you iterate.
  - Useful for working with big data.

---

## Basic Example
```python
def firstn():
    yield 1
    yield 2
    yield 3

for i in firstn():
    print(i)

Output:
1
2
3
```
# Generator with Parameters
```python
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

for i in firstn(10):
    print(i)

Output:
0
1
2
3
4
5
6
7
8
9
```
# Key Points

yield pauses the function and saves its state.

On the next call, execution continues from where it left off.

Generators are memory-efficient for streams, logs, big datasets.

# ✅ Rule of Thumb:
If you don’t need all results at once → use a generator.
