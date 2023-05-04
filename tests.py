import pytest
from main import Graph

g = Graph(5, 5)

def test_passable():
    # 2D array:
    # ['.', 'P', '.', '.', '.']
    # ['.', '#', '#', '#', '.']
    # ['.', '.', '.', '.', '.']
    # ['.', '.', 'Q', '.', '.']
    # ['.', '.', '.', '.', '.']
    assert g.isPassable(0,0) == True

def test_unpassable():
    assert g.isPassable(-1,0) == False

def test_adjacent():
    # Test that adjacents work correctly

    # Type check 
    with pytest.raises(TypeError):
        g.adjacent('a','b')
        g.adjacent(1.0,4.1)

    # Out of bounds check
    assert g.adjacent(-2,-2) == []
    assert g.adjacent(4,0) != [(4,-1), (3,0), (4,1)]

    # 1 direction available
    assert g.adjacent(0,0) == [(1,0)]
    assert g.adjacent(3,1) != [(1,0),(0,1)]
    # As P can't be passed and . can there is only one allowed coordinate 

    # 2 directions available
    assert g.adjacent(4,0) == [(4,1), (3,0)]

    # 3 directions available
    assert set(g.adjacent(2,3)) == set([(2, 2), (3, 3), (2, 4)])

    # All 4 directions available
    assert g.adjacent(3,1) == [(4, 1), (3, 2), (2, 1), (3, 0)]

def test_shortest_path():

    # Type check - should only pass Tuple[int, int]
    with pytest.raises(TypeError):
        g.shortestPath(g.graph, [0,0], [1,1])
        g.shortestPath(g.graph, (1.0, 4.1), (5.0, -2.0))
        assert True

    assert g.shortestPath(g.graph, (0,1), (3,2)) == 6
    # Path can be seen in @s
    # ['@', 'P', '.', '.', '.']
    # ['@', '#', '#', '#', '.']
    # ['@', '.', '.', '.', '.']
    # ['@', '@', 'Q', '.', '.']
    # ['.', '.', '.', '.', '.']
    
    assert g.shortestPath(g.graph, (0,0), (3,0)) == 3
    # Path can be seen in @s, start and end in **
    # [*@*, 'P', '.', '.', '.']
    # ['@', '#', '#', '#', '.']
    # ['@', '.', '.', '.', '.']
    # ['@', '.', 'Q', '.', '.']
    # [*@*, '.', '.', '.', '.']

    assert g.shortestPath(g.graph, (0,0), (0,0)) == 0
