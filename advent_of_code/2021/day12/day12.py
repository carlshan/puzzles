"""
Advent of Code 2021
Author: Carl Shan
Day 12: Passage Pathing
"""

import networkx as nx
from collections import Counter, deque, defaultdict

data = open('/Users/cshan/dev/puzzles/advent_of_code/2021/day12/day12.in', 'r').read().split('\n')

def build_graph(data):
    G = nx.Graph()
    nodes = [node.split('-')[0] for node in data] + [node.split('-')[1] for node in data]
    # Adding nodes
    for node in nodes:
        G.add_node(node, is_large = node[0].isupper())

    # Adding edges between nodes
    for line in data:
        n1, n2 = line.split('-')
        G.add_edge(n1, n2)
    return G

# My first attempt was below, but it was unsucessful
# def get_paths_helper(G, curr, end, path_so_far, visited, all_paths):
#     """
#     This function recursively explores from curr until it either:
#         1. Reaches the end, at which point it will return path_so_far
#         2. Reaches a node that is already in visited and that is also not is_large
#     """
#     # Base case: reached the end
#     if curr == end:
#         all_paths.append(path_so_far)
#         return True

#     # Base case: reached a node that is already in visited and that is also not is_large
#     # if curr in visited and not G.nodes[curr]['is_large']:
#     #    return False

#     # Recursive case: explore all neighbors

#     for neighbor in G.neighbors(curr):
#         if neighbor not in visited: # if the neighbor has not been visited
#             if not G.nodes[neighbor]['is_large']: # if the neighbor is not is_large
#                 visited.append(neighbor)
#             is_valid_path = get_paths_helper(G, neighbor, end, path_so_far + [neighbor], visited, all_paths)
#             if is_valid_path:
#                 while visited[-1] != neighbor:
#                     visited.pop()
#         else:
#             continue

# def get_paths(G, start, end):
#     """
#     This returns a list of all paths in the graph G from start until end.

#     A path can visit a node that is_large more than once.

#     However, it cannot visit a node that not is_large more than once.
#     """
#     all_paths = []
#     visited = [start]
#     path_so_far = [start]
#     get_paths_helper(G, start, end, path_so_far, visited, all_paths)

#     return all_paths

# The below solution came from https://www.reddit.com/r/adventofcode/comments/rehj2r/2021_day_12_solutions/?sort=confidence by user mcpower_
def paths(G, curr, visited):
    """
        This function returns the total number of possible paths from curr to end.
    """
    if curr == 'end':
        return 1
    if curr.islower() and curr in visited:
        return 0

    visited = visited | {curr}

    paths_sum = 0
    for neighbor in G.neighbors(curr):
        paths_sum += paths(G, neighbor, visited)

    return paths_sum

# Trying to improve my solution above using the knowledge from the reddit post
def paths2(G, curr, visited, path_so_far, all_paths):
    if curr == 'end':
        all_paths.append(path_so_far)
        return

    if curr.islower() and curr in visited:
        return

    visited = visited | {curr} # creates a copy of visited and adds curr to it

    for neighbor in G.neighbors(curr):
        paths2(G, neighbor, visited, path_so_far + [neighbor], all_paths)

def paths_part2(G, curr, dup, visited, path_so_far, all_paths):
    if curr == 'end':
        all_paths.append(path_so_far)
        return

    if curr == 'start' and visited:
        return

    if curr.islower() and curr in visited:
        if dup is None:
            dup = curr
        else:
            return

    visited = visited | {curr} # creates a copy of visited and adds curr to it

    for neighbor in G.neighbors(curr):
        paths_part2(G, neighbor, dup, visited, path_so_far + [neighbor], all_paths)

graph = build_graph(data)
all_paths = []
paths_part2(graph, 'start', None, set(), ['start'], all_paths)
num_paths = len(all_paths)
# paths = get_paths(graph, 'start', 'end')
