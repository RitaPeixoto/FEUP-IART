**a) Formulate this problem as a search problem by defining the state representation, initial state, operators (their name, preconditions, effects, and cost), and objective test.**

**State Representation**
This problem representation can be a tuple with three variables: m and c, representing the number of missionaries and cannibals on the initial bank of the river, respectively and d, a number representing where the boat is at, being 1 the initial side and -1 for the other side. Each state is defined as (m,c), where 0 <= m <= 3 and 0 <= c <= 3 and c <= m  and 3-c <= 3-m and 0 <= m + c <= 1.

**Initial State**
The initial state is when the are all in the initial bank of the river and, for that, is represented as (3, 3, 1).



**Operators**

In this problem all operators have the same cost, it can be 1.

| Operator                                                     | Initial State and Preconditions | Final State  | 
| ------------------------------------------------------------ | ------------------------------- | ------------ | 
| Move one cannibal from the initial bank to the final         | (m, c, b)     | b = 1      | ((m1, c1 -1, m2, c2 + 1), -b)  | 1    |
| Move one cannibal from the final bank to the initial         | (m, c, b)     | b = -1     | ((m1, c1+1, m2, c2-1), -b)     | 1    |
| Move one missionary from the initial bank to the final       | (m, c, b)     | b = 1      | ((m1-1, c1, m2+1, c2), -b)     | 1    |
| Move one missionary from the final bank to the initial       | (m, c, b)     | b = -1     | ((m1+1, c1, m2-1, c2), -b)     | 1    |
| Move two missionaries from the initial bank to the final     | (m, c, b)     | b = 1      | ((m1-2, c1, m2+2, c2), -b)     | 1    |
| Move two missionaries from the final bank to the initial     | (m, c, b)     | b = -1     | ((m1+2, c1, m2-2, c2), -b)     | 1    |
| Move two cannibals from the initial bank to the final        | (m, c, b)     | b = 1      | ((m1, c1-2, m2, c2+2), -b)     | 1    |
| Move two cannibals from the final bank to the initial        | (m, c, b)     | b = -1     | ((m1, c1+2, m2, c2-2), -b)     | 1    |
| Move one cannibal and one missionary from the initial bank to the final | (m, c, b)     | b = 1      | ((m1-1, c1-1, m2+1, c2+1), -b) | 1    |
| Move one cannibal and one missionary from the final bank to the initial | (m, c, b)     | b = -1     | ((m1+1, c1+1, m2-1, c2-1), -b) | 1    |


**Objective Test**

The goal is to find a way to get the six to the other bank of the river without ever leaving more cannibals than missionaries on one of the banks (even at the instant they leave/join the boat) during the process.
The goal state will be (0, 0, -1), not minding where the boat is at the end, but it is obvious that it will be on the other side of the river which is -1.


**b) Solve the problem, by hand, using tree search.**