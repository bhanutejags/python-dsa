# Greedy Method
A common strategy used to solve problems.
Useful in solving optimization problems, the problems which require minimum or maximum result.

Optimizations problems can be solved using the below approaches:
* Greedy Method
* Dynamic Programming
* Branch and Bound

## Greedy Method
* While looping over stuff, check if it is feasible solution to the problem.

```
n = 5
a = [a1, a2, a3, a4, a5]
algo greedy(a, n)
{
  for i = 1 to n do
  {
    x = select(a);
    if is_feasible(x) then
    {
      solution = solution + x;
    }
  }
}
```

```python
n = 5
a = [a1, a2, a3, a4, a5]
def greedy(a, n):
  for i in range(1, n  + 1):
    x = select(a)
    if is_feasible(x):
      solution = solution + x;
```
