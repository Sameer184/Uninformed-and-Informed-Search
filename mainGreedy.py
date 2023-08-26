import heapq
final_goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
class class_node:
    def __init__(self, active_state, parent=None, actions_ateken=None, current_cost=0):
        self.active_state = active_state
        self.parent = parent
        self.actions_ateken = actions_ateken
        self.current_cost = current_cost
        self.h = self.heuritic(active_state)
        self.f = self.current_cost + self.h
    def __lt__(self, other):
        return self.f < other.f
    def heuritic(self, active_state):
        distance = 0
        for i in range(9):
            if active_state[i] != 0:
                distance += abs(i // 3 - (active_state[i] - 1) // 3) + abs(i % 3 - (active_state[i] - 1) % 3)
        return distance
    def get_actions(self, active_state):
        list_of_action = []
        zero_index = active_state.index(0)
        if zero_index not in [0, 1, 2]:
            list_of_action.append('Up')
        if zero_index not in [6, 7, 8]:
            list_of_action.append('Down')
        if zero_index not in [0, 3, 6]:
            list_of_action.append('Left')
        if zero_index not in [2, 5, 8]:
            list_of_action.append('Right')
        return list_of_action
    def apply_action(self, active_state, actions_ateken):
        zero_index = active_state.index(0)
        if actions_ateken == 'Up':
            new_index = zero_index - 3
        elif actions_ateken == 'Down':
            new_index = zero_index + 3
        elif actions_ateken == 'Left':
            new_index = zero_index - 1
        elif actions_ateken == 'Right':
            new_index = zero_index + 1
        new_state = active_state[:]
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        return new_state
    def is_goal_state(self, active_state):
        return active_state == final_goal_state

def solve(starting_board, final_goal_state):
    front_end = []
    explored = set()
    initial_node = class_node(starting_board)
    heapq.heappush(front_end, initial_node)
    nodes_popping = 0
    nodes_expanding = 0
    nodes_generating = 1
    maxi_fring_siz = 1
    while front_end:
        current_Node = heapq.heappop(front_end)
        nodes_popping += 1
        if initial_node.is_goal_state(current_Node.active_state):
            current_depth = current_Node.current_cost
            current_cost = current_Node.f
            total_allover_steps = []
            while current_Node.parent is not None:
                total_allover_steps.append(current_Node.actions_ateken)
                current_Node = current_Node.parent
            total_allover_steps.reverse()
            return current_depth, current_cost, total_allover_steps, nodes_popping, nodes_expanding, nodes_generating, maxi_fring_siz
        explored.add(tuple(current_Node.active_state))
        list_of_action = initial_node.get_actions(current_Node.active_state)
        for actions_ateken in list_of_action:
            new_state = initial_node.apply_action(current_Node.active_state, actions_ateken)
            if tuple(new_state) not in explored:
                new_node = class_node(new_state, current_Node, actions_ateken, current_Node.current_cost + 1)
                heapq.heappush(front_end, new_node)
                nodes_generating += 1
        nodes_expanding += 1
        maxi_fring_siz = max(maxi_fring_siz, len(front_end))
    return None
if __name__=="__main__":
    starting_board = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    final_goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    current_depth, current_cost, total_allover_steps, nodes_popping, nodes_expanding, nodes_generating, maxi_fring_siz = solve(starting_board, final_goal_state)
    print(f"Nodes Popped: {nodes_popping}")
    print(f"Nodes Expanded: {nodes_expanding}")
    print(f"Nodes Generated: {nodes_generating}")
    print(f"Max Fringe Size: {maxi_fring_siz}")
    if current_depth is not None:
        print(f"Solution Found at current_depth {current_depth} with current_cost of {current_cost}.")
        print("Steps:")
        for step in total_allover_steps:
            print(f"\t{step}")
    else:
        print("No solution found.")

