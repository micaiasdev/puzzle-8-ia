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
def bfs(node: Node):
  fronteira = deque()
  fronteira.append(node)
  explorados = set()
  
  while fronteira:
    actual_node = fronteira.popleft()
    explorados.add(actual_node)
    if actual_node.state == final_board:
      return
    new_states = create_successors(actual_node.state)
    for state in new_states:
      new_node = Node(state, None, node)
      fronteira.append(new_node)
      
if __name__ == "__main__":
  bfs(root)
  



