from typing import List, Dict, Tuple, Set
from collections import deque
from generate_succeessors import create_successors
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
  while(1):
    actual_level_nodes = list()
    while fronteira:
      actual_node = fronteira.popleft()
      if actual_node in explorados:
        continue
      if actual_node.state == final_state:
        return actual_node
      actual_level_nodes.append(actual_node)
      explorados.add(actual_node)
    for explo_node in actual_level_nodes:
       expand_nodes = create_successors(explo_node)
       fronteira.append(expand_nodes)

if __name__ == "__main__":
  bfs(root)
  



