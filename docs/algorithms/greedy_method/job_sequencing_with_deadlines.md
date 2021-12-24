# Job Sequencing with Deadlines
Greedy method can be used to determine the order or priority of execution of jobs, 
where each job has an associated deadline and an associated profit, 
to maximise the total profit.

There also might be more jobs than are slots available for their execution, 
so only a particular combination of jobs which maximise profits must be run.

For the purposes of this problem, it is assumed each job takes 1 unit of time.

```python
from dataclasses import dataclass

@dataclass
class Job:
  job_id: int
  profit: int
  deadline: int
```

??? example "Example 1"
  
    | Jobs      | $J_1$ | $J_2$ | $J_3$ | $J_4$ | $J_5$ |
    |-----------|-------|-------|-------|-------|-------|
    | Profits   | 20    | 15    | 10    | 5     | 1     |
    | Deadlines | 2     | 2     | 1     | 3     | 3     |

    If the number of slots are 3, only 3 of the above jobs can be scheduled for execution.
    
    $0 -J_2-> 1 -J_1-> 2 -J_4-> 3$

    First select the jobs with the highest profits, and schedule as late their deadlines allow us.
    So the sequence of jobs is ${J_2, J_1, J_4}$, and total profit is 
