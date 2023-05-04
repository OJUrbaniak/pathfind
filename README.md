# Oxbury Pathfind

Imagine representing a grid-shaped game map as a 2-dimensional array. Each value of this array is
boolean `true` or `false` representing whether that part of the map is passable (a floor) or blocked
(a wall).

Write a function that takes such a 2-dimensional array `A` and 2 vectors `P` and `Q`, with `0,0` being the top left corner of the map and returns the distance of the shortest path between those points, respecting the walls in the map.

eg. Given the map (where `.` is passable - `true`, and `#` is blocked - `false`)

```
. P . . .
. # # # .
. . . . .
. . Q . .
. . . . .
```

then `pathfind(A, P, Q)` should return `6`.

_Please avoid using libraries to implement the algorithmic side of this challenge, other libraries (such as PHPUnit or Jest for testing) are welcome._

## What to do

1. Clone/Fork this repo or create your own
2. Implement the function described above in any mainstream language you wish
3. Provide unit tests for your submission
4. Fill in the section(s) below

## Comments Section

<!---
Please fill in the sections below after you complete the challenge.
--->

### What I'm Pleased With

Successful implementation of a breadth-first search, all contained in a thoroughly documented class. Plenty of tests to ensure type safety, out of bounds detection.

### What I Would Have Done With More Time

Implemented another type of search, such as dijkstra's algorithm in cases where the array is much larger as breadth-first search suffers from performance problems when the search space is large. This is due to it keeping track of each "path" through the problem.