import networkx as nx
import numpy as np
import bisect
import random

# TODO: You may just copy and past your search.py or romania.py files here. Make sure you remove any lines of code under
#  "main" or not included in a certain class. You will design the program in 'pddl_parser/PDDL.py' file.

class NavigationProblem:
    def __init__(self, initial, goal, connections, locations=None, directed=False):
        self.initial = initial
        self.goal = goal
        self.locations = locations
        self.graph = nx.DiGraph() if directed else nx.Graph()
        for cityA, cityB, distance in connections:
            self.graph.add_edge(cityA, cityB, cost=distance)            
    def successors(self, state):
        ## Exactly as defined in Lecture slides, 
        return [("go to %s" % city, connection['cost'], city) for city, connection in self.graph[state].items()]
    def goal_test(self, state):
        return state == self.goal

class Node:
    def __init__(self, state=None, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost        
    def getPath(self):
        """getting the path of parents up to the root"""
        currentNode = self
        path = [self]
        while currentNode.parent: ## stops when parent is None, ie root
            path.append(currentNode.parent)
            currentNode = currentNode.parent
        path.reverse() #from root to this node
        return path
    def expand(self, problem):
        successors = problem.successors(self.state)
        return [Node(newState, self, action, self.path_cost+cost) for (action, cost, newState) in successors]
    def __gt__(self, other): ## needed for tie breaks in priority queues
        return True
    def __repr__(self):
        return (self.state, self.action, self.path_cost)
    
class FIFO:
    # TODO: Paste your work from assignment 1.
    pass

class LIFO:  ## TODO: fill out yourself! 
    # TODO: Paste your work from assignment 1.
    pass

class PriorityQueue:
    def __init__(self, f):
        self.list = []
        self.f = f
    def push(self, item):
        priority = self.f(item)
        bisect.insort(self.list, (priority, random.random(), item))
    def pop(self):
        return self.list.pop(0)[-1]
        
def graph_search(problem, frontier):
    # TODO: Paste your work from assignment 1.
    pass
    
def breadth_first_graph_search(problem):
    return graph_search(problem, FIFO())
def depth_first_graph_search(problem):
    return graph_search(problem, LIFO())
def astar_graph_search(problem, f):
    return graph_search(problem, PriorityQueue(f))

#%%
# priority functions for Priority Queues used in UCS and A*, resp., if you are unfamiliar with lambda calc.

def ucs(node):
    return node.path_cost

def f(node):
    return node.path_cost + h[node.state]


