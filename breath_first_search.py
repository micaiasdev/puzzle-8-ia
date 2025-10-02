from typing import List, Dict, Tuple, Set
from collections import deque
from generate_succeessors import create_successors, print_board
from Node import Node

init_board = [
              1,2,3,
              4,5,6,
              7,0,8
                    ]
final_board =  [
              1,2,3,
              4,5,6,
              7,8,0
                    ]

root = Node(init_board, None, None)
def bfs(root: Node):
  fronteira = deque(root)
  explorados = set()
  
  while fronteira:
    node = fronteira.popleft()
    explorados.add(node)
    if node.state == final_board:
      return
    new_states = create_successors(node)
    for states in new_states:
  
  

bfs(root)
  



