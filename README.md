# Advent_of_Code_2024
This repository the code I wrote to overcome AoC 2024 problems

I'll try to detail later in the readme what was the approach day per day and the different traps I avoided/fell into.

## Day 16

### Part 1

I just took a A* algorithm implementation (https://www.geeksforgeeks.org/a-search-algorithm-in-python/) and changed the heuristic to put a penality depending on the number of rotation that will be needed to go to the final destination. I also added the rotation as a coordinate, so a position was defined (x, y, rotation).

It worked pretty well and fast enough however I did not find a way to change it in a way to solve part 2 so far. 


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