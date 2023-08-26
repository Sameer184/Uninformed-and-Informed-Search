Title: Uninformed & Informed Search

Description: Task is to build an agent to solve a modifed version of the 8 puzzle problem (called the Expense 8 puzzle problem). The task is still to take a 3X3 grid on which 8 tiles have been placed, where you can only move one tile at a time to an adjacent location (as long as it is blank) and figure out the order in which to move the tiles to get it to a desired configuration. However now the number on the tile now also represents the cot of moving that tile (moving the tile marked 6 costs 6)

Programming Language used: Python

Code Structure:
- The Main function is defined in Main.py file where we accept 3 arguments 
For Example: Main.py start.txt goal.txt <algorithm> true
- For each of the algorithm specified there is a separate function defined. They are:
    - function_b_f_s -  Breadth First Search
    - function_u_c_s -  Uniform Cost Search
    - function_d_f_s -  Depth First Search
    - function_d_l_s -  Depth Limited Search
    - function_i_d_s -  Iterative Deepening Search
    - function_g_s   -  Greedy Seach
    - function_a_s   -  A* Search
- As the Greedy method always selects the path that expands the nearest node first and estimates the closest cost, it combines both dfs and bfs.
It has been defined in a separate .py file named mainGreedy.py
- By utilizing the function print_puzzle_board, we are printing the 8-puzzle matrix for each move as well.

Steps to run the code:
1. Navigate the current working directory where all the project files have been extracted.
2. Open the command prompt in the same current path.
3. The start.txt file should be set as necessary for the 8-puzzle problem.
4. Run the following command for Breadth-First Search
> python Main.py start.txt goal.txt bfs true

Similarly the same for any algorithm:
Uniform Cost Search
> python Main.py start.txt goal.txt ucs true

Depth First Search
> python Main.py start.txt goal.txt dfs true 

Depth Limited Search
> python Main.py start.txt goal.txt dls true 

Iterative Deepening Search
> python Main.py start.txt goal.txt ids true 

Greedy Seach
> python Main.py start.txt goal.txt greedy true

A* Search
> python Main.py start.txt goal.txt a* true





                                
