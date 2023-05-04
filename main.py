from collections import defaultdict
from typing import Tuple


class Graph():
    def __init__(self, columns: int, rows: int):
        # Initialize class variables
        self.columns = columns
        self.rows = rows
        self.start = (0, 1)
        self.end = (3,2)

        # Create 2D list
        self.A = [['.' for i in range(rows)] for j in range(columns)]

        # Fill 2D list with walls, objectives
        self.A[0][1] = 'P'
        self.A[1][1:4] = ['#'] * (4-1)
        self.A[3][2] = 'Q'

        # Build graph, represented as a dictionary {NODE: NEIGHBORS}
        self.graph = self.build_graph()

    def shortestPath(self, graph: dict, start: Tuple[int, int], end: Tuple[int, int]):
        """Finds the shortest path from start to end using breadth first search.

        Args:
            graph (dict): the graph represented as a dictionary (NODE: NEIGHBORS)
            start (tuple): the start coordinate as a tuple (x,y)
            end (tuple): the end coordinate as a tuple (x,y)

        Returns:
            path_length (int): the shortest path length from start to end
        """

        # List to hold all visited nodes
        visited = [[start]]

        # List which contains nodes which have not been visited yet
        queue = [[start]]
        
        # If the start (x,y) == end (x,y)
        if start == end:
            return 0
        
        # While queue is not empty
        while queue:
            # Explore first node in queue
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                neighbors = graph[node]             # Get all neighbors of current node
                
                # print(f"{node} -> {neighbors}")

                # Explore neighbor by neighbor
                for neighbor in neighbors:
                    new_path = list(path)           # Copy & ensure path is a list
                    new_path.append(neighbor)       # Add current neighbor to list
                    
                    # Add the new path to the queue e.g. [[start -> neighbor1], [start -> neighbor2],...]
                    queue.append(new_path)
                    
                    # Check if neighbor is the end
                    if neighbor == end:
                        print("Shortest path: ", *new_path)
                        
                        # Length of path - 1 due to start/end
                        path_length = len(new_path) - 1
                        
                        # Return path length
                        return path_length
                
                # Add current node to visited nodes 
                visited.append(node)
                
        # Return -1 if no path found
        return -1


    def build_graph(self):
        """Creates a graph represented as a dictionary 
        
        {
            (x,y) : [(x-1,y), (x,y+1), ...],
            ...
        }

        Returns:
           dict: dictionary representation of graph
        """
        
        # Init dict
        graph = defaultdict(list)

        # Add all possible adjacent nodes from starting coordinate to graph
        graph[self.start] = self.adjacent(self.start[0], self.start[1])

        # Add all possible adjacent nodes for each coordinate in 2D list
        for x in range(self.rows):
            for y in range(self.columns):
                # Add possible moves to each coordinate in 2D list
                # i.e. (x,y) -> [(x+1, y), (x, y+1)]
                graph[(x,y)] = self.adjacent(x, y)

        # Return graph dict
        return graph

    # Get possible adjacent nodes for a given node
    def adjacent(self, x: int, y: int):
        """Finds the possible adjacent moves from given coordinate

        Args:
            x (int): integer representing the row of the 2D list
            y (int): integer representing the column of the 2D list

        Returns:
            list: list of all possible (x,y) adjacent moves; e.g. [(x+1, y), (x, y+1)]
        """
        # List of all 4 moves (up, down, left, right)
        surrounding = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

        # Check which moves are possible / within bounds
        surrounding = [(x, y) for x, y in surrounding if self.isPassable(x,y)]

        # Return all possible moves
        return surrounding

    def print(self):
        """Prints the entire 2D list row by row
        """
        for row in self.A:
            print(row)
    
    def isPassable(self, x: int, y: int):
        """Checks if given coordinate is passable

        Args:
            x (int): integer representing the row of the 2D list
            y (int): integer representing the column of the 2D list

        Returns:
            boolean: returns true if coordinate is passable or the end, false otherwise
        """
        # Check if within bounds of 2D list
        if x not in range(self.rows) or y not in range(self.columns):
            return False
        
        # If within bounds
        if self.A[x][y] == '.' or self.A[x][y] == 'Q':
            # Passable
            return True
        else: 
            # Blocked
            return False
        
## To test from here uncomment the code below 
# g = Graph(5, 5)
# print(g.shortestPath(g.graph, g.start, g.end))