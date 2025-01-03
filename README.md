# Advent_of_Code_2024
This repository the code I wrote to overcome AoC 2024 problems

I'll try to detail later in the readme what was the approach day per day and the different traps I avoided/fell into.

## Day 1-2

Nothing to declare

## Day 3

Used RegEx to find the correct multiplications in the input.

## Day 16

### Part 1

I just took a A* algorithm implementation (https://www.geeksforgeeks.org/a-search-algorithm-in-python/) and changed the heuristic to put a penality depending on the number of rotation that will be needed to go to the final destination. I also added the rotation as a coordinate, so a position was defined (x, y, rotation).

It worked pretty well and fast enough however I did not find a way to change it in a way to solve part 2 so far. 

### Part 2

I am editing this part as I found where my mistake was. The script on part 1 was organised to function in 2 steps:
1. Find the shortest path and register tiles per tiles the next tile on the path. 
2. Start from the last tile (i.e. the targeted destination) and go back one tile at a time using the registered tiles on the path.

The issue with this way of registering paths is that only one path can be registered as each tile on the path will point to ONLY ONE next tile. Therefore, I decided to register all the tiles leading to one tile in a list. This way, if a tile can be reached by two paths with the same cost, it will be registered in the list.

Of course I had to change some parameters for the first step: The cost to current tile is directly computed as the f value, as we know after part 1 what is the cost of the shortest past, and the algorithm continue its search on a node if the cost value is equal to its currently registered one (if it is strictly lower than registered one, it means that the current complete path has a lower cost so we delete the paths previously registered one the next node). I also added a stop condition using the maximum cost (computed in part 1).

On the second step, we use the same protocol but when a node (tile) has more than one previous tile leading to it, we register all these tiles in a pending list and continue our path tracing until reaching the start point. After that we restart from the first tile in the pending list and so on. 

## Day 17

### Part 1

This part could be resolved using a quite straight forward method: implement the different instructions, create a mapping of operand and their associated combo, store the values of A, B, and C and apply the program with a pointer that is moving on the program 2 increment at a time (to avoid operands).

### Part 2

This part was a little bit more complicated and I had to rewrite the program explicitly on a paper sheet to understand its mecanism. Turns out that the program was tailored to do a loop until the value stored in A was equal to 0 (with the value of A being divided by 8 each iteration). 

The program I was given works as follow:

```
While A > 0:
    B -> A % 8
    B -> bitwiseXOR(B, 5)
    C -> floor(A/2^B)
    B -> bitwise(bitwiseXOR(B, 6), C)
    A -> floor(A/8)
    Output B % 8
``` 

At first I had elaborated a method to go from the value of the output and find the possible values of A creating this output, but it turns out that just trying every possible A of the current iteration and comparing the produced result with the expected output value is "fast enough" (less than a second on my computer).

The approach was as following:

* Each iteration A = A//8, meaning that if A of the current iteration is i, the A of the previous iteration is included in [i * 8; i * 8 - 1]
* At the end of the last iteration A = 0, meaning that A at the end of the previous iteration was included in [1; 7]
* We try every possible A in [1; 7] and check if the output generated correspond to the last one of the expected output. 
  * If yes, we add [A * 8; A * 8 - 1] to the list of potential A candidates in previous iteration
* We continue through each iterations until we reach the first iteration.

## Day 18

Yet another 2D puzzle! This time, it was much easier — a straightforward A* algorithm with the Euclidean distance (L2) heuristic worked perfectly.

For part 2, brute-forcing the problem by running an A* search for each new corrupted location turned out to be fast enough. A quick optimization could be skipping the search if the corrupted byte doesn’t fall on the previously discovered path. I should also clean up the code since it’s just a modified copy-paste from day 16.

## Day 19

### Part 1

In this problem we had to find if a pattern (e.g., 'abcba') could be built using given keys (e.g., 'ba' or 'abc') as many time as we wanted. The solution I wrote work as follow:

1. We start at the beginning of the pattern and look in the keys if some of them correspond to the beginning of the pattern.
-> For instance if keys = {'abc', 'a', 'ab', 'd'} and the pattern begins by 'abd', we can use two keys to start constructing the pattern.
2. We create a word using the found keys.
-> In the example we have 'a' and 'ab'
3. We reiterate from the first element of the pattern not included in the current word until we create the whole pattern or could not continue
-> In the example 'a' can not be completed to form 'abd' but we can add 'd' to 'ab' to form 'abd'
4. If we were able to form at least one complete pattern we count it as feasible

### Part 2 

This time we have to count every combination that would create a feasible pattern. We could reuse the exact same algorithm but it would take too much time as we go from ~200 combinations (1 per feasible pattern) to create to ~ 1.10**14 combinations. The good thing is that most of the valid combinations from a same pattern are very similar in the way it is formed. 

-> For instance if we use the keys {'ab', 'abc', 'c'}, 'ab' + 'c' will form 'abc' that is also an existing key. Therefore, if 'abc' is the beginning of a correct combination, so does 'ab' + 'c'. 

This way I decided not to form all combinations but to construct all combinations GIVEN A SAME ROOT and add the number of root that created this combination

-> In the example above, if 'abc' is the root of a correct combination, we don't had 1 but 2 to the total as we can achieve creating 'abc' in two ways.

This method made the algorithm find the solution in less than a second!

## Day 20

The script for today’s problem works for both part 1 and part 2, with the only difference being the maximum length of a cheat (```max_len_cheat``` variable). The approach is straightforward: first, find the path from start to end using an A* search (I choose to use A* as I already had the implementation from day 16 and day 18 available). Then, identify all possible shortcuts up to the specified maximum length that meet the criterion of minimum gained distance.

To calculate the gained distance, we use the following idea:
Since a shortcut (created by a cheat) can pass through any location on the grid, the shortest path between two points will always be a straight line. Therefore, the length of the shortest shortcut between two points on the original path is their L1 (Manhattan) distance. The gained distance is then the difference between the indexes of the two points in the original path and their L1 distance. The goal is to apply this formula to all pairs of points on the original path and select the ones that meet the minimum gained distance criterion.

To speed up the process, bad candidates can be discarded before applying the formula. For example, pairs of points whose indexes in the original path are too close together (i.e., not separated by at least the minimum gained distance) can be skipped. Even if the shortcut length is zero, such pairs would not meet the gained distance requirement.

With this optimization, the script runs in approximately 3.7 seconds on my laptop.

## Day 23

Today's puzzle can be translated into graph theory as finding [cliques](https://en.wikipedia.org/wiki/Clique_(graph_theory)) from a given [edge list](https://en.wikipedia.org/wiki/Edge_list) with specific conditions.

The naive approach is presented in `initial_script.py`. To summarize briefly, we use elements of the list of edges to create sets of three interconnected nodes by comparing the elements with incomplete and already created sets. The issue with this method is that the number of iterations needed to compare one element of the edge list with all created sets constantly increases. Therefore, I decided to look for existing algorithms in graph theory to solve this type of problem.

The final approach I decided to follow involved creating an [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix) from the edge list, then applying a built-in function from the Networkx library (as I have only a basic understanding of graph theory), and finally applying some conditions (only cliques with exactly 3 nodes and one starting with "t", and taking the clique of maximum length).