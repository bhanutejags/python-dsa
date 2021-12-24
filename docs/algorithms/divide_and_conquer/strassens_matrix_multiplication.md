# Strassen's Matrix Multiplication
Time Complexity of naive way of implementing this would be $O(n^3)$.

???+ example "Matrix Multiplication"
    For example, here `[1, 2, 3, 4, 5, 6, 7]`, if `4` is chosen as a pivot element, it is also the median of the array.
    The array would be partitioned in two equal half for the next recursion.
    
    \begin{bmatrix}
    a_{11} & a_{12} \\
    a_{21} & a_{22} \\
    \end{bmatrix}
    
    \begin{bmatrix}
    b_{11} & b_{12} \\
    b_{21} & b_{22} \\
    \end{bmatrix}
    
    \begin{bmatrix}
    c_{11} & c_{12} \\
    c_{21} & c_{22} \\
    \end{bmatrix}
    
    $A * B = C$
    
    $c_{11} = a_{11}*b_{11} + a_{12}*b_{21}$


## Algorithm
```
func mm(A, B, n):
    if (n <= 2):
        perform normal matrix multiplication
    else:
        mid = n // 2
        mm(A11,B11,mid) + md(A12,B21,mid)
        mm(A11,B12,mid) + md(A12,B22,mid)
        mm(A21,B11,mid) + md(A22,B21,mid)
        mm(A21,B12,mid) + md(A22,B22,mid)
```

### Time Complexity
This is recursive algorithm.

f(n) =
\begin{cases}
n/2,  & \text{if $n$ is even} \\
3n+1, & \text{if $n$ is odd}
\end{cases}

\left.
\begin{array}{l}
\text{if $n$ is even:}&n/2\\
\text{if $n$ is odd:}&3n+1
\end{array}
\right\}
=T(n)


$T(n) = 8*T(n/2) + n^2 $.

Time Complexity is $\theta(n^3)$.


#### Strassen's Matrix M 
Time Complexity is $O(n^{2.81})$.

