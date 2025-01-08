# Advent_of_Code_2024
This repository contains the code I wrote to solve the AoC 2024 puzzles.

I will detail here my approach for each day, including the different challenges I encountered and how I overcame them.

## Day 1-2

Nothing to declare

## Day 3

Used RegEx to find the correct multiplications in the input.

## Day 4

The puzzle involved identifying patterns of "XMAS" in a 2D string grid. For part 1, the algorithm iterates through each element of the grid. If an element is "X", it checks all possible directions (horizontally forward/backward, vertically, diagonally) to determine if the "X" is the start of "XMAS". This results in a time complexity of O(n²).

For part 2, the approach is similar, with the exception that only two directions are checked: the diagonal (to the right and down) and the opposite diagonal (forming an "X" with the first diagonal). The time complexity remains O(n²). Initially, a separate code was written for this part (available in `day04/script_part2.py`), but it was later realized that the `check_direction()` function from part 1 could be reused for part 2. This optimized solution has been added to `day04/script.py`.

## Day 5

The problem of the day involved identifying lines that adhere to a specific order within a list of lines composed of sequences of two-digit numbers. For the first part, I iterated through each element (i.e., two-digit number) in a line and verified that every preceding number in the line was not recorded in the rules as needing to come after the current element.

In the second part, the task was to reorder the incorrect lines. To achieve this, I placed each number in the reordered list based on the number of elements that should follow it. The practical approach was to first create a new line filled with zero elements. Then, for each element in the original line, I counted the number of elements that should come after it and placed the element in the k-th empty position in the new line (counting from the end), where k is the number of elements that should follow it.

After review of this solution, I think it could be possible to optimize it by not creating the new line but finding the element that should in the middle using the same method that helped creating a new line.

## Day 6

The problem of the day involved identifying all positions occupied by a moving point in a 2D puzzle and determining what changes would create a loop in the moving point's path.

### Part 1

This part was straightforward. We could emulate the path by iterating over the guard's position (i.e., the moving point) and return the length of the path.

### Part 2

In this part, the objective was to find all obstacle locations that would create a loop in the guard's path. Initially, I tested every location in the 2D puzzle and reran the part 1 solution to see if it created a loop. However, this resulted in a large number of candidates to test (~20,000). Two optimizations helped speed up the process:

1. Candidates will only be on the original path (otherwise, the guard won't have the opportunity to cross the location).
2. The path from the initial position to the added obstacle will be the same as the original path. Therefore, we do not need to emulate this part of the path.

These two optimizations reduced the script's runtime to approximately 1.5 minutes (both part solutions can be executed using `day06/script_part2.py`) on my laptop, while a single iteration takes 0.1 seconds (can be executed separately using `day06/script.py`).

## Day 7

The problem of the day involved determining if a target number could be obtained using a set of numbers and operations. To solve this, I generated all possible combinations using recursion and tested if any combination matched the target number.

The only issue I encountered was initially thinking that I needed to apply operations in a specific order (multiplications before additions). The implementation I made in this regard is still available in `day07/script_with_order.py`.

## Day 8

Not a lot to describe for today's problem. we first evaluate the horizontal and vertical distance between to antenas and then check the location obtained when we apply again the distance. For the part 2, we just have to apply k time the distance until we reach the border of the puzzle.

## Day 9

Today's problem involved allocating files in empty spaces from a line giving file locations. The main idea was to traverse the line of locations both in the forward and reverse directions. In the forward direction, we traverse the line until we find an empty space. Then, in the reverse direction, we move files into the found empty spaces.

A crucial aspect of making this solution memory efficient is understanding that we only need a checksum of the reorganized locations, not a line giving the new locations. Therefore, we compute the checksum at each step and only store an integer rather than a list.

For part 2, we apply the same idea but add a condition on the empty space and file size. For better clarity, I have separated both parts (part 2 can be executed using `day09/script_part2.py`).

## Day 10

Today's problem was a pathfinding problem. I implemented a custom depth-first algorithm and iterated over all elements of the 2D puzzle that were equal to 0.

## Day 11

Today's problem involved applying rules to a list of integers a certain number of times (25 for part 1, 75 for part 2). The issue here is that those integers could eventually create new integers in the list, increasing the list length and therefore the number of operations to apply per epoch.

This is very similar to the 2021 day 6 problem with lanternfish, where the trick is to count the number of elements of a certain level (i.e., the number of occurences of an integer in the list) rather than storing all of them, as the result of the operation will be the same for all of them. This makes the code memory and time efficient. However, as the rules do not change at each iteration, we could make the solution even more efficient by finding a formula that would directly give the number of integers produced by an integer after k iterations rather than performing each iteration. Another solution would be to use memoization, as many integers are recurrent (e.g., 0 and 1).

## Day 12

This day was significant for me as it was the first time I encountered a problem directly related to image processing, specifically shape attributes, which I studied during my second Master's degree. The task involved finding areas and perimeters of regions in a 2D grid of letters.

I treated each letter as a grey level in an image and applied a connected component labeling method (two-pass algorithm) to distinguish each region. Then, I counted all "minimal edges" and vertices that each pixel adds to the shape of a region, corresponding to how the perimeter is considered in part 1 and part 2, respectively.

The final code can be executed by running `day12/script.py`. Additionally, I have included the initial "naive" code (`day12/script_naive.py` for part 1 and `day12/script_naive_part2.py` for part 2), which was an attempt to create a more efficient variant of the two-pass algorithm for this specific problem. Interestingly, the final (more general) implementation runs twice as fast.

## Day 13

Today's problem involved determining the number of times we needed to press two buttons to move a point in a 2-dimensional space to a target location. This can be translated into a linear equation: a * (x1, y1) + b * (x2, y2) = (x3, y3), where A = (x1, y1) represents the translation caused by pressing button A, B = (x2, y2) represents the translation caused by pressing button B, and (x3, y3) is the target.

This equation has a unique solution if the determinant of the matrix formed by A and B is non-zero. Therefore, the problem reduces to solving a linear equation. If the determinant is zero, there is either no solution or an infinite number of solutions. In the latter case, an optimization method would be required, but this scenario did not occur in the provided input.

## Day 14

### Part 1

Today's part 1 challenge was relatively straightforward. We were given the locations of robots along with their movement patterns, which remain consistent across iterations. The task was to determine the locations of the robots after 100 iterations. Since each robot's movement pattern is independent of the others and remains unchanged, the location after k iterations can be calculated using a simple formula: x_initial + k * x_movement, y_initial + k * y_movement (with a minor exception when the robot moves out of the grid).

### Part 2

The second part was more subtle. We needed to determine the number of iterations required for the robots' locations to form a Christmas tree shape. Without a clear description of what a Christmas tree should look like, I initially decided to generate an image for each iteration. This approach presented two main problems:
1. It did not utilize the observation from part 1, which saved time by considering each robot independently.
2. It required a large number of iterations, making image generation time-consuming.

After generating approximately 7000 images, I discovered on the AoC subreddit that the correct iteration could be found by checking if no robots were overlapping. I added this solution to the code in `day14/script.py`, but it is not the only working solution. For example, measuring the image variance also works well. I find this method of solving the puzzle quite clever!

## Day 15

Today's problem involved simulating moving objects due to a robot moving on a 2D puzzle with movement instructions and obstacles. For part 1 (`day15/script.py`), I emulated the robot's path and added a function to check all boxes moved by the robot's movement. This was done using a recursive function that checking boxes from the robot to either the next empty spot or the next obstacle in the direction of the robot's movement, then moving all boxes encountered in the recursion.

Part 2 (`day15/script_part2.py`) involved a similar approach, but I had to distinguish between vertical and horizontal movements, as the modifications in part 2 only impacted vertical movements.

To run the code, please separate the input into two text files: `input_map.txt` (containing your grid input) and `input_moves.txt` (containing your list of movements).

## Day 16

### Part 1

I just took a A* algorithm implementation found [here](https://www.geeksforgeeks.org/a-search-algorithm-in-python/) and changed the heuristic to put a penality depending on the number of rotation that will be needed to go to the final destination. I also added the rotation as a coordinate, so a position was defined (x, y, rotation).

It worked pretty well and fast enough however it took me a lot of time to find a way to change it in a way to solve part 2. 

### Part 2

The script on part 1 was organised to function in 2 steps:
1. Find the shortest path and register tiles per tiles the next tile on the path. 
2. Start from the last tile (i.e. the targeted destination) and go back one tile at a time using the registered tiles on the path.

The issue with this way of registering paths is that only one path can be registered as each tile on the path will point to ONLY ONE next tile. Therefore, I decided to register all the tiles leading to one tile in a list. This way, if a tile can be reached by two paths with the same cost, it will be registered in the list.

Of course I had to change some parameters for the first step: The cost to current tile is directly computed as the f value, as we know after part 1 what is the cost of the shortest past, and the algorithm continue its search on a node if the cost value is equal to its currently registered one (if it is strictly lower than registered one, it means that the current complete path has a lower cost so we delete the paths previously registered one the next node). I also added a stop condition using the maximum cost (computed in part 1).

On the second step, we use the same protocol but when a node (tile) has more than one previous tile leading to it, we register all these tiles in a pending list and continue our path tracing until reaching the start point. After that we restart from the first tile in the pending list and so on. 

## Day 17

Please note that for this puzzle, I have directly written my input in the code as it was very short and because my solution is specifically tailored to my input.

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

At first I had elaborated a method to go from the value of the output and find the possible values of A creating this output, but it turns out that just trying every possible A of the current iteration and comparing the produced result with the expected output value is "fast enough" (around .005 second on my computer).

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

## Day 21

Today's problem involved finding the shortest sequence of movements on a directional keypad to encode a sequence that would type the correct code on a numerical keypad. This required navigating through multiple intermediate directional keypads.

To solve the problem, I wrote a recursive function that counts the number of movements needed to produce one movement from the first directional keypad to the last one. This was done by mapping a movement to the sequence of movements it would produce on the next keypad. Unfortunately, I have not yet written a method to get the sequence from the numerical keypad to the first keypad, so I had to write the initial sequence directly in the code.

Part 2 involved increasing the number of intermediate directional keypads, which significantly increased the execution time. To address this, I used memoization by storing the count of final movements for a given (keypad depth, movement) pair.

## Day 22

Today's problem involved generating sequences of integers and then finding a specific pattern in these sequences with an optimality condition. For part 1, I applied the rules for each iteration, which worked well. For part 2, after each iteration, I stored the current score of every pattern for each buyer (i.e., lines in the input) in a dictionary and extracted the maximum score at the end.

This process takes around 7 seconds to run on my laptop, which is not ideal, but I am pleased that I was able to reduce the runtime from approximately 2 minutes to 7 seconds. This improvement was achieved by optimizing the way I store the pattern scores and by applying the integer generation rules more efficiently (e.g., using the built-in bitwise XOR method rather than the one I initially implemented for day 17).

## Day 23

Today's puzzle can be translated into graph theory as finding [cliques](https://en.wikipedia.org/wiki/Clique_(graph_theory)) from a given [edge list](https://en.wikipedia.org/wiki/Edge_list) with specific conditions.

The naive approach is presented in `initial_script.py`. To summarize briefly, we use elements of the list of edges to create sets of three interconnected nodes by comparing the elements with incomplete and already created sets. The issue with this method is that the number of iterations needed to compare one element of the edge list with all created sets constantly increases. Therefore, I decided to look for existing algorithms in graph theory to solve this type of problem.

The final approach I decided to follow involved creating an [adjacency matrix](https://en.wikipedia.org/wiki/Adjacency_matrix) from the edge list, then applying a built-in function from the Networkx library (as I have only a basic understanding of graph theory), and finally applying some conditions (only cliques with exactly 3 nodes and one starting with "t", and taking the clique of maximum length).

## Day 24

Today's puzzle involved applying a set of operations (also referred to as gates) and then correcting the set so that it outputs the addition of two binary numbers.

For part 1, I applied all operations with a system of priority to operations where all elements already have a registered value.

For part 2, I had to find all resulting wires (i.e., results of operations) that were not well placed, causing the set of operations to not have the desired behavior. Since the puzzle stated that the set of operations should result in adding two binary numbers, I first determined what the set of operations should look like for each digit to produce the expected output. Then, I implemented a protocol to check if this is what the actual set is doing (for each digit) and registered any misplaced resulting wires. I simplified some of the conditions, assuming they would only cover edge cases that were unlikely to be in the puzzle input.

The code is quite long as it needs to check a number of conditions, but it runs 'fast enough' (less than .01 seconds on my laptop).

## Day 25

The last puzzle involved checking if pairs of patterns fit without overlapping. The main difficulty was that the format of the input was not optimal. Therefore, I first recorded each key/lock pin height,as it was suggested in the puzzle. Then, I applied a simple condition that the sum of two corresponding pin heights should not be greater than 5.