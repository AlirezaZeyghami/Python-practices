# Python OOP – Lambda, Map & Filter

## Lambda Functions
- **Lambda** functions are disposable (one-time use) and anonymous.
- Syntax:

lambda arguments: expression
```python
# Example
my_func = lambda x: x * 2
print(my_func(5))  # Output: 10
```
# Sorting with Lambda

Use lambda as a key function in sorting.
```python
a = [(3, 4), (7, 1), (5, 9), (2, 2)]
a.sort(key=lambda x: x[1])
print(a)  # Output: [(7, 1), (2, 2), (3, 4), (5, 9)]
```

# Map

Applies a function to each item of an iterable.
```python
my_list = [1, 3, 4, 2, 0.5]
result = list(map(lambda x: x * 2, my_list))
print(result)  # Output: [2, 6, 8, 4, 1.0]
```

Conditional Example
```python
numbers = [10, 11, 8, 7, 100, 9, 24, 6]
result = list(map(lambda x: 'big' if x > 10 else 'small', numbers))
print(result)
# Output: ['small', 'big', 'small', 'small', 'big', 'small', 'big', 'small']
```

# Filter

Returns elements that satisfy a condition.
```python
my_another_list = [1, 5, 6, 8, 10, 11]
result = list(filter(lambda x: x % 2 == 0, my_another_list))
print(result)  # Output: [6, 8, 10]
```

# ✅ Key Points:
Lambda: Quick anonymous function.

Map: Transform all elements.

Filter: Select elements based on condition.
