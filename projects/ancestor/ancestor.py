from collections import deque

def earliest_ancestor(ancestors, starting_node):
    #child node is the key, parent node is the value
    child_to_parent_graph = dict()
    
    # mapping the ancestors list to the hashtable
    # child is the key, a list containing the parent(s) is the value
    for pc in ancestors:
        child = pc[1]
        parent = pc[0]
        if child not in child_to_parent_graph:
            child_to_parent_graph[child] = [parent]
        else:
            child_to_parent_graph[child] = [*child_to_parent_graph[child], parent]

    current_node = starting_node
    que = deque()
    que.append(current_node)

    while len(que) > 0:
        current_node = que.popleft()
        if current_node in child_to_parent_graph:
            # sorting the arr of parent values in descending order, so the greatest valued parent will get popped first, leaving the lesser value as the last current_node
            child_to_parent_graph[current_node].sort(reverse=True)

            # adding the parents to the que
            for next_node in child_to_parent_graph[current_node]:
                que.append(next_node)

    if current_node == starting_node: # Check to see if the starting node had a parent
        return -1
    else:
        return current_node

# Notes;
#   -No need to tag visited nodes/worry about cycles, the instructions claified that condition





# breakdown of what i could do with the info provided
# ancestors is an array of tuples that contain two values
# the first value represents the parent node of a graph
# the second represents a child
# the starting_node is the value of the node
## most notably it would be the child node since we are looking at the most distant ancestor

