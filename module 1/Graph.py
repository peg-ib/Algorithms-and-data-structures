import fileinput
import re
from collections import deque
import sys

sys.setrecursionlimit(20000)


class Graph:
    def __init__(self, graph_type):
        self._graph = {}
        self._graph_type = graph_type

    def add_vertex(self, key, value):
        if key not in self._graph.keys():
            self._graph[key] = set()
            self._graph[key].add(value)
        else:
            self._graph[key].add(value)
        if self._graph_type == 'u':
            if value not in self._graph.keys():
                self._graph[value] = set()
                self._graph[value].add(key)
            else:
                self._graph[value].add(key)
        elif self._graph_type == 'd' and value not in self._graph.keys():
            self._graph[value] = set()

    def bfs(self, start_vertex):
        queue = deque({start_vertex})
        used = set()
        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in used:
                print(current_vertex)
            used.add(current_vertex)
            sorting_neighbors = sorted(self._graph[current_vertex])
            for neighbor in sorting_neighbors:
                if neighbor not in used:
                    queue.append(neighbor)

    def dfs(self, start_vertex, used=None):
        print(start_vertex)
        used = used or set()
        used.add(start_vertex)
        sorting_neighbors = sorted(self._graph[start_vertex])
        for neighbor in sorting_neighbors:
            if neighbor not in used:
                self.dfs(neighbor, used)


def parse_string(command_string):
    graph = None
    graph_type, start_vertex, search_type = None, None, None
    for line in command_string.input():
        line = line.strip('\n')
        if line == '':
            continue
        elif re.search(r'[ud] [^ ]+ [bd]', line) is not None and graph is None:
            graph_type, start_vertex, search_type = line.split()
            graph = Graph(graph_type)
        elif re.search(r'[^ ]+ [^ ]+', line) is not None and graph is not None:
            first_vertex, second_vertex = line.split()
            graph.add_vertex(first_vertex, second_vertex)
    if search_type == 'b':
        graph.bfs(start_vertex)
    elif search_type == 'd':
        graph.dfs(start_vertex)


if __name__ == '__main__':
    parse_string(fileinput)
