import sys
import copy
from queue import Queue
from queue import PriorityQueue
from queue import LifoQueue


file_input = ""
file_goal = ""
approach_choosen = "a*"
dump_flag = "false"
goal_puzzle_state = [[1,2,3], [4,5,6], [7,8,0]]

def print_puzzle_board(regular_board_state):
    list1 = [ str(x) for x in regular_board_state[0]]
    print("\t".join(list1))
    list2 = [ str(x) for x in regular_board_state[1]]
    print("\t".join(list2))
    list3 = [ str(x) for x in regular_board_state[2]]
    print("\t".join(list3))

def find_blank(board):
    for temp_var_i in range(3):
        for temp_var_j in range(3):
            board_state= board[temp_var_i][temp_var_j]
            if board_state == 0:
                return temp_var_i, temp_var_j
            
class Class_State_Puzzle:
    def __init__(self, current_state, parnt_node=None, taken_action=None, cost_of_state=0):
        self.current_state = current_state
        self.parnt_node = parnt_node
        self.taken_action = taken_action
        self.depth = 0
        self.cost_of_state = cost_of_state
        if parnt_node:
            self.depth = parnt_node.depth + 1
    def is_goal(self):
        return self.current_state == goal_puzzle_state
    def look_all_possible_steps(self):
        actions = []
        current_row, current_column = self.find(0)
        if current_row > 0:
            actions.append('Up')
        if current_row < 2:
            actions.append('Down')
        if current_column > 0:
            actions.append('Left')
        if current_column < 2:
            actions.append('Right')
        return actions
    def make_move(self, taken_action):
        current_row, current_column = self.find(0)
        new_state = copy.deepcopy(self.current_state)
        if taken_action == 'Up':
            new_state[current_row][current_column], new_state[current_row-1][current_column] = new_state[current_row-1][current_column], new_state[current_row][current_column]
        elif taken_action == 'Down':
            new_state[current_row][current_column], new_state[current_row+1][current_column] = new_state[current_row+1][current_column], new_state[current_row][current_column]
        elif taken_action == 'Left':
            new_state[current_row][current_column], new_state[current_row][current_column-1] = new_state[current_row][current_column-1], new_state[current_row][current_column]
        elif taken_action == 'Right':
            new_state[current_row][current_column], new_state[current_row][current_column+1] = new_state[current_row][current_column+1], new_state[current_row][current_column]
        return Class_State_Puzzle(new_state, parnt_node=self, taken_action=taken_action, cost_of_state=self.cost_of_state+1)
    def find(self, value):
        for temp_var_i in range(3):
            for temp_var_j in range(3):
                if self.current_state[temp_var_i][temp_var_j] == value:
                    return temp_var_i, temp_var_j
    def __str__(self):
        return '\n'.join([' '.join([str(cell) for cell in current_row]) for current_row in self.current_state])
    def __lt__(self, other):
        return self.cost_of_state < other.cost_of_state
    def calculate_heuristic(self):
        final_dist = 0
        for temp_var_i in range(3):
            for temp_var_j in range(3):
                if self.current_state[temp_var_i][temp_var_j] != 0:
                    current_row, current_column = self.find(self.current_state[temp_var_i][temp_var_j])
                    final_dist += abs(temp_var_i - current_row) + abs(temp_var_j - current_column)
        return final_dist

def path_printing(temp_initial_puzzle, solution, temp_goal_puzzle):
    total_cost = 0
    for each in solution:
        each = each.title().strip()
        position_of_zero = find_blank(temp_initial_puzzle)
        if each == "Left":
            total_cost = total_cost + int(temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]-1])
            print("Move",int(temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]-1]),"Right")
            temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]], temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]-1] = temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]-1], temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]]
            print_puzzle_board(temp_initial_puzzle)
        elif each == "Right":
            total_cost = total_cost + int(temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]+1])
            print("Move",int(temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]+1]),"Left")
            temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]], temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]+1] = temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]+1], temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]]
            print_puzzle_board(temp_initial_puzzle)
        elif each == "Up":
            total_cost = total_cost + int(temp_initial_puzzle[position_of_zero[0]-1][position_of_zero[1]])
            print("Move",int(temp_initial_puzzle[position_of_zero[0]-1][position_of_zero[1]]),"Down")
            temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]], temp_initial_puzzle[position_of_zero[0]-1][position_of_zero[1]] = temp_initial_puzzle[position_of_zero[0]-1][position_of_zero[1]], temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]]
            print_puzzle_board(temp_initial_puzzle)
        elif each == "Down":
            total_cost = total_cost + int(temp_initial_puzzle[position_of_zero[0]+1][position_of_zero[1]])
            print("Move",int(temp_initial_puzzle[position_of_zero[0]+1][position_of_zero[1]]),"Up")
            temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]], temp_initial_puzzle[position_of_zero[0]+1][position_of_zero[1]] = temp_initial_puzzle[position_of_zero[0]+1][position_of_zero[1]], temp_initial_puzzle[position_of_zero[0]][position_of_zero[1]]
            print_puzzle_board(temp_initial_puzzle)
    print("Final total_cost :", total_cost)

def function_read_file(Input_File):
    File_data = open(Input_File, 'r')
    file_reading = File_data.readlines()
    file_reading = [ x.replace("\n","").strip().split(" ") for x in file_reading ]
    file_reading = file_reading[:-1]
    file_reading = [ [ int(y) for y in x] for x in file_reading]
    return file_reading

def bfs(puzzle_ini_board):
    active_que = Queue()
    active_que.put(puzzle_ini_board)
    count_node_visits = set()
    maximum_fring_size = 0
    while not active_que.empty():
        current_state = active_que.get()
        if current_state.is_goal():
            built_path = []
            cost_of_state = 0
            while current_state.parnt_node:
                built_path.append(current_state.taken_action)
                cost_of_state += 1
                current_state = current_state.parnt_node
            built_path.reverse()
            return built_path, cost_of_state, count_node_visits, maximum_fring_size
        count_node_visits.add(str(current_state))
        for taken_action in current_state.look_all_possible_steps():
            active_child = current_state.make_move(taken_action)
            if str(active_child) not in count_node_visits:
                active_que.put(active_child)
        if active_que.qsize() > maximum_fring_size:
            maximum_fring_size = active_que.qsize()
    return None, None, count_node_visits, maximum_fring_size

def function_b_f_s(Initial_Board_State, goal_puzzle, dump_flag):
    print('Run -> Breadth First Search')
    puzzle_ini_board = Class_State_Puzzle(Initial_Board_State)
    built_path, cost_of_state, count_node_visits, maximum_fring_size = bfs(puzzle_ini_board)
    print("Nodes Popped:", len(count_node_visits))
    print("Nodes Expanded:", len(count_node_visits)+1)
    print("Nodes Generated:", len(count_node_visits) + maximum_fring_size)
    print("Max Fringe Size:", maximum_fring_size)
    if built_path:
        print("Solution Found at depth", len(built_path))
        path_printing(Initial_Board_State, built_path, goal_puzzle)
    else:
        print("No solution found.")

def uniform_cost_search(puzzle_ini_board):
    front_node = PriorityQueue()
    front_node.put((0, puzzle_ini_board))
    count_node_visits = set()
    maximum_fring_size = 0
    while not front_node.empty():
        current_state = front_node.get()[1]
        if current_state.is_goal():
            built_path = []
            cost_of_state = current_state.cost_of_state
            while current_state.parnt_node:
                built_path.append(current_state.taken_action)
                current_state = current_state.parnt_node
            built_path.reverse()
            return built_path, cost_of_state, count_node_visits, maximum_fring_size
        count_node_visits.add(str(current_state))
        for taken_action in current_state.look_all_possible_steps():
            active_child = current_state.make_move(taken_action)
            if str(active_child) not in count_node_visits:
                front_node.put((active_child.cost_of_state, active_child))
        if front_node.qsize() > maximum_fring_size:
            maximum_fring_size = front_node.qsize()
    return None, None, count_node_visits, maximum_fring_size

def function_u_c_s(arg_ip_data, arg_goal_data, dump_flag):
    print('Run -> Uniform Cost Search')
    puzzle_ini_board = Class_State_Puzzle(arg_ip_data)
    built_path, cost_of_state, count_node_visits, maximum_fring_size = uniform_cost_search(puzzle_ini_board)
    print("Nodes Popped:", len(count_node_visits))
    print("Nodes Expanded:", len(count_node_visits)+1)
    print("Nodes Generated:", len(count_node_visits) + maximum_fring_size)
    print("Max Fringe Size:", maximum_fring_size)
    if built_path:
        print("Solution Found at depth", len(built_path))
        path_printing(arg_ip_data, built_path, arg_goal_data)
    else:
        print("No solution found.")

def dfs(puzzle_ini_board, goal_puzzle_state):
    active_stack = [puzzle_ini_board]
    count_node_visits = set()
    maximum_fring_size = 0

    while active_stack:
        current_state = active_stack.pop()
        if current_state.is_goal():
            built_path = []
            cost_of_state = 0
            while current_state.parnt_node:
                built_path.append(current_state.taken_action)
                cost_of_state += 1
                current_state = current_state.parnt_node
            built_path.reverse()
            return built_path, cost_of_state, count_node_visits, maximum_fring_size
        count_node_visits.add(str(current_state.current_state))
        for taken_action in current_state.look_all_possible_steps():
            active_child = current_state.make_move(taken_action)
            if str(active_child.current_state) not in count_node_visits:
                active_stack.append(active_child)
        if len(active_stack) > maximum_fring_size:
            maximum_fring_size = len(active_stack)
    return None, None, count_node_visits, maximum_fring_size

def function_d_f_s(arg_ip_data, arg_goal_data, dump_flag):
    print('Run -> Depth First Search')
    puzzle_ini_board = Class_State_Puzzle(arg_ip_data)
    goal_puzzle_state = [[1,2,3], [4,5,6], [7,8,0]]
    built_path, cost_of_state, count_node_visits, maximum_fring_size = dfs(puzzle_ini_board, goal_puzzle_state)
    print("Nodes Popped:", len(count_node_visits))
    print("Nodes Expanded:", len(count_node_visits)+1)
    print("Nodes Generated:", len(count_node_visits) + maximum_fring_size)
    print("Max Fringe Size:", maximum_fring_size)
    if built_path:
        print("Solution Found at depth", len(built_path))
        path_printing(arg_ip_data, built_path, arg_goal_data)
    else:
        print("No solution found.")

def make_move(board, look_direction):
    temp_var_i, temp_var_j = find_blank(board)
    if look_direction == 'up' and temp_var_i > 0:
        board[temp_var_i][temp_var_j], board[temp_var_i-1][temp_var_j] = board[temp_var_i-1][temp_var_j], board[temp_var_i][temp_var_j]
    elif look_direction == 'down' and temp_var_i < 2:
        board[temp_var_i][temp_var_j], board[temp_var_i+1][temp_var_j] = board[temp_var_i+1][temp_var_j], board[temp_var_i][temp_var_j]
    elif look_direction == 'left' and temp_var_j > 0:
        board[temp_var_i][temp_var_j], board[temp_var_i][temp_var_j-1] = board[temp_var_i][temp_var_j-1], board[temp_var_i][temp_var_j]
    elif look_direction == 'right' and temp_var_j < 2:
        board[temp_var_i][temp_var_j], board[temp_var_i][temp_var_j+1] = board[temp_var_i][temp_var_j+1], board[temp_var_i][temp_var_j]

def generate_moves(board):
    moves = []
    temp_var_i, temp_var_j = find_blank(board)
    if temp_var_i > 0:
        moves.append('up')
    if temp_var_i < 2:
        moves.append('down')
    if temp_var_j > 0:
        moves.append('left')
    if temp_var_j < 2:
        moves.append('right')
    return moves

def heuristic(board):
    cost_of_state = 0
    for temp_var_i in range(3):
        for temp_var_j in range(3):
            if board[temp_var_i][temp_var_j] != 0:
                goal_i = (board[temp_var_i][temp_var_j] - 1) // 3
                goal_j = (board[temp_var_i][temp_var_j] - 1) % 3
                cost_of_state += abs(temp_var_i - goal_i) + abs(temp_var_j - goal_j)
    return cost_of_state

def print_board(board):
    for temp_var_i in range(3):
        for temp_var_j in range(3):
            print(board[temp_var_i][temp_var_j], end=' ')
        print()

def dfs_limited(board, limit):
    count_nodes_poppp = 0
    count_nodes_expandedd = 0
    nodes_generated = 1
    maximum_fring_size = 1
    front_node = LifoQueue()
    front_node.put((board, [], 0, heuristic(board)))
    explored = set()
    while not front_node.empty():
        cNode, built_path, cost_of_state, h = front_node.get()
        count_nodes_poppp += 1
        if cost_of_state > limit:
            continue
        explored.add(str(cNode))
        if cNode == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            print(f"Nodes Popped: {count_nodes_poppp}")
            print(f"Nodes Expanded: {count_nodes_expandedd}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {maximum_fring_size}")
            print(f"Solution Found at depth {cost_of_state}.")
            path_printing(arg_ip_data, built_path, arg_goal_data)
            return True
        look_direction = generate_moves(cNode)
        count_nodes_expandedd += 1
        for look_direction in look_direction:
            active_child = [current_row[:] for current_row in cNode]
            make_move(active_child, look_direction)
            if str(active_child) not in explored:
                nodes_generated += 1
                front_node.put((active_child, built_path + [look_direction], cost_of_state+1, heuristic(active_child)))
                maximum_fring_size = max(maximum_fring_size, front_node.qsize())
    return False

def function_d_l_s(arg_ip_data, arg_goal_data, dump_flag):
    print('Run -> Depth Limited Search')
    limit = 12
    found = dfs_limited(arg_ip_data, limit)
    if not found:
        print(f"Solution not found within depth limit of {limit}.")

def get_moves(current_state):
    moves = []
    zero_index = current_state.index(0)
    if zero_index % 3 != 0:
        new_state = copy.deepcopy(current_state)
        new_state[zero_index], new_state[zero_index - 1] = new_state[zero_index - 1], new_state[zero_index]
        moves.append(new_state)
    if zero_index % 3 != 2:
        new_state = copy.deepcopy(current_state)
        new_state[zero_index], new_state[zero_index + 1] = new_state[zero_index + 1], new_state[zero_index]
        moves.append(new_state)
    if zero_index // 3 != 0:
        new_state = copy.deepcopy(current_state)
        new_state[zero_index], new_state[zero_index - 3] = new_state[zero_index - 3], new_state[zero_index]
        moves.append(new_state)
    if zero_index // 3 != 2:
        new_state = copy.deepcopy(current_state)
        new_state[zero_index], new_state[zero_index + 3] = new_state[zero_index + 3], new_state[zero_index]
        moves.append(new_state)
    return moves

def iterative_deepening_search(start_state, goal_state_a):
    # print(start_state, goal_state_a)
    ins_max_depth = 0
    count_nodes_poppp = 0
    count_nodes_expandedd = 0
    nodes_generated = 0
    maximum_fring_size = 0
    while True:
        count_node_visits = set()
        depth_limit = ins_max_depth + 1
        fringe = [(start_state, 0, [])]
        while fringe:
            current_state, cost_of_state, built_path = fringe.pop(0)
            count_nodes_poppp += 1
            if tuple(current_state) == tuple(goal_state_a):
                print("Nodes Popped:", count_nodes_poppp)
                print("Nodes Expanded:", count_nodes_expandedd)
                print("Nodes Generated:", nodes_generated)
                print("Max Fringe Size:", maximum_fring_size)
                print("Solution Found at depth", len(built_path))
                built_path = [ [x[:3],x[3:6],x[6:]] for x in built_path ]
                built_path.insert(0, [start_state[:3],start_state[3:6], start_state[6:]])
                trace_fibal_print_path(built_path)
                return
            if tuple(current_state) in count_node_visits:
                continue
            count_node_visits.add(tuple(current_state))
            count_nodes_expandedd += 1
            if len(built_path) < depth_limit:
                for make_move in get_moves(current_state):
                    if tuple(make_move) not in count_node_visits:
                        nodes_generated += 1
                        fringe.append((make_move, cost_of_state + 1, built_path + [make_move]))
            maximum_fring_size = max(maximum_fring_size, len(fringe))
        ins_max_depth += 1

def trace_fibal_print_path(solution, total_cost = 0):
    count_step = 1
    for Temp_Index_value in range(len(solution)-1):
        print("Step ->", count_step)
        first_zer_pos = find_blank(solution[Temp_Index_value])
        second_zer_pos = find_blank(solution[Temp_Index_value + 1])
        Temp_Cost = solution[Temp_Index_value][second_zer_pos[0]][second_zer_pos[1]]
        total_cost = total_cost + Temp_Cost
        if first_zer_pos[0] == second_zer_pos[0]:
            if first_zer_pos[1] > second_zer_pos[1]:
                print("Move", Temp_Cost, "Right")
                print_puzzle_board(solution[Temp_Index_value+1])
            else:
                print("Move", Temp_Cost, "Left")
                print_puzzle_board(solution[Temp_Index_value+1])
        else:
            if first_zer_pos[0] > second_zer_pos[0]:
                print("Move", Temp_Cost, "Down")
                print_puzzle_board(solution[Temp_Index_value+1])
            else:
                print("Move", Temp_Cost, "Up")
                print_puzzle_board(solution[Temp_Index_value+1])
        count_step = count_step + 1
    print("Final total_cost :", total_cost)

def function_i_d_s(arg_ip_data, arg_goal_data, dump_flag):
    print('Run -> Iterative Deepening Search')
    start_state = []
    for x in arg_ip_data:
        start_state.extend(x)
    goal_state_a = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    iterative_deepening_search(start_state, goal_state_a)

def function_g_s(arg_ip_data, arg_goal_data, dump_flag):
    from mainGreedy import solve as solve_g
    print('Run -> Greedy Search')
    start_state = []
    for x in arg_ip_data:
        start_state.extend(x)
    goal_puzzle_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    depth, cost_of_state, steps, count_nodes_poppp, count_nodes_expandedd, nodes_generated, maximum_fring_size = solve_g(start_state, goal_puzzle_state)
    print(f"Nodes Popped - {count_nodes_poppp}")
    print(f"Nodes Expanded - {count_nodes_expandedd}")
    print(f"Nodes Generated - {nodes_generated}")
    print(f"Max Fringe Size - {maximum_fring_size}")
    if depth is not None:
        print(f"Solution Found at depth {depth}")
        path_printing(arg_ip_data, steps, arg_goal_data)
    else:
        print("No solution found.")

def h(current_state):
    final_dist = 0
    for temp_var_i in range(3):
        for temp_var_j in range(3):
            value = current_state.current_state[temp_var_i][temp_var_j]
            if value != 0:
                current_row, current_column = divmod(value-1, 3)
                final_dist += abs(current_row - temp_var_i) + abs(current_column - temp_var_j)
    return final_dist

def astar(puzzle_ini_board):
    front_node = PriorityQueue()
    front_node.put((0, puzzle_ini_board))
    count_node_visits = set()
    maximum_fring_size = 0
    while not front_node.empty():
        cNode = front_node.get()
        current_state = cNode[1]
        if current_state.is_goal():
            built_path = []
            cost_of_state = 0
            while current_state.parnt_node:
                built_path.append(current_state.taken_action)
                cost_of_state += 1
                current_state = current_state.parnt_node
            built_path.reverse()
            return built_path, cost_of_state, count_node_visits, maximum_fring_size
        count_node_visits.add(str(current_state))
        for taken_action in current_state.look_all_possible_steps():
            active_child = current_state.make_move(taken_action)
            if str(active_child) not in count_node_visits:
                priority = h(active_child) + active_child.depth
                front_node.put((priority, active_child))
        if front_node.qsize() > maximum_fring_size:
            maximum_fring_size = front_node.qsize()
    return None, None, count_node_visits, maximum_fring_size

def function_a_s(arg_ip_data, arg_goal_data, dump_flag):
    print('Run -> A Star Search')
    puzzle_ini_board = Class_State_Puzzle(arg_ip_data)
    built_path, cost_of_state, count_node_visits, maximum_fring_size = astar(puzzle_ini_board)
    print("Nodes Popped -", len(count_node_visits))
    print("Nodes Expanded -", len(count_node_visits)+1)
    print("Nodes Generated -", len(count_node_visits) + maximum_fring_size)
    print("Max Fringe Size -", maximum_fring_size)
    if built_path:
        print("Solution Found at depth", len(built_path))
        path_printing(arg_ip_data, built_path, arg_goal_data)
    else:
        print("No solution found.")

Command_Line_Arguments = sys.argv
Length_Command_Line_Arguments = len(Command_Line_Arguments)

if Length_Command_Line_Arguments >= 3:
    
    file_input = Command_Line_Arguments[1]
    file_goal = Command_Line_Arguments[2]
    
    if Length_Command_Line_Arguments >= 4:
        approach_choosen = Command_Line_Arguments[3].lower()
    if Length_Command_Line_Arguments == 5:
        dump_flag = Command_Line_Arguments[4]
    
    arg_ip_data = function_read_file(file_input)
    arg_goal_data = function_read_file(file_goal) 

    if approach_choosen == "bfs":
        function_b_f_s(arg_ip_data, arg_goal_data, dump_flag)
    elif approach_choosen == "ucs":
        function_u_c_s(arg_ip_data, arg_goal_data, dump_flag)
    elif approach_choosen == "dfs":
        function_d_f_s(arg_ip_data, arg_goal_data, dump_flag)
    elif approach_choosen == "dls":
        function_d_l_s(arg_ip_data, arg_goal_data, dump_flag)
    elif approach_choosen == "ids":
        function_i_d_s(arg_ip_data, arg_goal_data, dump_flag)
    elif approach_choosen == "greedy":
        function_g_s(arg_ip_data, arg_goal_data, dump_flag)
    else:
        function_a_s(arg_ip_data, arg_goal_data, dump_flag)
else:
    print("Give correct number of command line arguments!")
    sys.exit()


