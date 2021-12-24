# Optimal Merge Pattern

* Merging is the process of combing two sorted array to form a single large array, this is more precisely called Two-way merge. 
* Merge has a time complexity of $\theta(n + m)$. 

* The discussion of optimal merge pattern comes up with, more than two array have to merged pairwise using only Two-way merge.
* The Greedy Method that should be followed here is that the smaller list must always be merged first, then only then move onto merging larger lists.


??? example "Merge"
    
    | List  | A   | B   | C   | D   |
    |-------|-----|-----|-----|-----|
    | Sizes | 6   | 5   | 3   | 2   |
    
    The best way to merge this would be to start with mergin the smaller lists first and then going ontowards the large one.

$\sum_1^n (d_{i} \times x_{i})$, where $d_{i}$ is the distance of each array and $x_{i}$ is the length of the $i^{th}$ array.
