from typing import List, Dict, Tuple, Set
from collections import deque
from generate_succeessors import create_successors, print_board
from Node import Node

init_board = [
              1,2,3,
              4,5,6,
              7,0,8
                    ]
final_state =  [
              1,2,3,
              4,5,6,
              7,8,0
                    ]

root = Node(init_board, None, None)

def bfs(node: Node):
  if node.state == final_state:
    return
  fronteira = deque()
  fronteira.append(node)
  explorados = set()
  # Expandir fronteira
  new_states = create_successors(node.state)
  while fronteira:
    actual_node = fronteira.popleft()
    if actual_node is not explorados:
      if actual_node.state == final_state:
        return
    explorados.add(actual_node)
      
if __name__ == "__main__":
  bfs(root)
  



