# Binary Search Challenge

Coding challenge for the HyperionDev Graduate Program (Level 2, Task 8), from the Software Engineer Bootcamp Grad list.

**Challenge:** Implement the binary search algorithm on a sorted array.

## How it works

Binary search keeps track of the part of the list that could still hold the target, using a `low` and a `high` index. Each step it checks the middle item:

- if the middle item is the target, it returns that index
- if the middle item is smaller than the target, the target can only be to the right, so `low` moves past the middle
- if the middle item is bigger, the target can only be to the left, so `high` moves before the middle

When `low` passes `high` the search space is empty and the function returns `-1`.

## Efficiency

Each step halves the search space, so the search takes O(log n) time and O(1) extra memory. A linear search checks items one by one and takes O(n). For a list of 1,000,000 items, binary search needs at most about 20 checks, where a linear search could need 1,000,000. The trade-off is that the list must already be sorted.

## Files

- `binary_search.py`: the `binary_search(numbers, target)` function and a small demo
- `test_binary_search.py`: 10 unit tests covering the first, middle and last items, missing values, an empty list, a one-item list, negative numbers and a large list checked against `list.index`

## Running it

```
python binary_search.py
python -m unittest -v test_binary_search
```

## Result

```
Ran 10 tests in 0.001s

OK
```
