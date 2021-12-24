---
tags:
   - algorithms
---
# Analysis of Algorithms

## Key characteristics of algorithms
* Input
* Output
* Definiteness -> Clear and Unambiguous
* Finiteness ->
* Effectiveness -> Nothing superfluous 

## Important Metrics of Algorithm performance
* Time
* Space
* Network Consumption
* Power Consumption

???+ note "CPU registers" 
    For device drivers and other low-level algorithms, another metric of analyses could be the number of CPU registers the algorithm utilizes.

* Datatypes are decided at Program time, we don’t usually care when we write pseudocode.
* Every simple statement, we assume takes 1 unit of time,
    * Of course, this is really shallow, at machine-code this can change
    * How deep we would want to go in an analysis is up to us.

???+ example "Example 1: Calculating Time and Space Complexity"
    ```python
    {
      temp = a;
      a = b;
      b = temp;
    }
    ```
    $f(n) = 3$

## Frequency Count Method
??? example "Sum of all elements in an array."
    ```python
    sum (A, n) {
        s = 0;
        for (i = 0; i < n; i++){
           s = s + A[i]
        }
        return s;
    }
    ```
    _Analyses_:
    === "Time Complexity"
        * `i` changes n+1 times,  inside the loop the statements executed for n times. The first and return statement add 2 more the time complexity.
        * $f(n) = 2n + 3 = O(n)$ -> Order of n.
    === "Space Complexity"
        * A, n, s, I
        * Just 3 variables, each is one word, and one array of size n.
        * $S(n) = n + 3 = O(n)$ -> Order of n.

??? example "Sum of two matrices"
    ```python
    add(A, B, n) {
        for(i = 0; i < n; i++) { # -> n + 1
            for (j = 0; j < n; j++) { # -> n x (n + 1)
                C[i,j] = A[i,j] + B[i,j]; # -> n x n
            }
        }
    }
    ```
    _Analyses_
    === "Time Complexity"
        * $f(n) = n + 1 + n^2 + n + n^2 = 2*n^2 + 2*n + 1 = O(n^2)$ -> Order of $n^2$.
    === "Space Complexity"
        * $A$ -> $n^2$, $B$ -> $n^2$, $C$ -> $n^2$, $n$ -> $1$, $I$ -> $1$, $j$ -> $1$
        * Total: $2*n^2 + 3 = O(n^2)$ -> Order of $n^2$.

## Time Complexity
* Ceil of non-integer count
* Conditional statements -> Worst and Best case statements

### Class of Time Functions
* $O(1)$ -> Constant
* $O(log n)$ -> Logarithmic
* $O(n)$ -> Linear
* $O(n^2)$ -> Quadratic
* $O(n^3)$ -> Cubix
* $O(2^n)$ -> Exponential

???+ note "Class of Time Functions"
    $1 < log n < root(n) < n < n * (log n) < n^2 < n^3 ... < 2^n < 3^n < ... < n^n$

### Asymptotic Notation
* Comes from Mathematics
* O -> big-oh -> Upper Bound of a Function
* Ω -> big—omega -> Lower Bound of function
* θ -> theta -> Average Bound

### Best and Average 


## Recurrence Relations - Recursive Algorithms
### Master Theorem
$T(n) = aT(b/n) + f(n)$
[Brilliant - Master Theorem](https://brilliant.org/wiki/master-theorem/)
