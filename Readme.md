Title: Uninformed & Informed Search

Name: Siva Srinivasa Sameer Miriyala
UTA ID: 1002024871

Programming Language used: Python

Code Structure:
- The Main function is defined in Main.py file where we accept 3 arguments 
For Example: Main.py start.txt goal.txt <algorithm> true
- For each of the algorithm specified there is a separate function defined. They are:
    function_b_f_s -  Breadth First Search
    function_u_c_s -  Uniform Cost Search
    function_d_f_s -  Depth First Search
    function_d_l_s -  Depth Limited Search
    function_i_d_s -  Iterative Deepening Search
    function_g_s   -  Greedy Seach
    function_a_s   -  A* Search
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





                                