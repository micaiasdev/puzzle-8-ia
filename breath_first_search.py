from typing import List, Dict, Tuple, Set
from collections import deque
from generate_succeessors import create_successors
from Node import Node

init_board =   [0,1,3,4,2,6,7,5,8]
final_state =  [
              1,2,3,
              4,5,6,
              7,8,0
                    ]

root = Node(init_board, None, None)

def bfs(node: Node):
  global visit_nodes
  visit_nodes = 0
  if node.state == final_state:
    return
  fronteira = deque()
  fronteira.append(node)
  explorados = set()
  while True:
    actual_level_nodes = list()
    while fronteira:
      actual_node = fronteira.popleft()
      if actual_node.state == final_state:
        return actual_node
      visit_nodes += 1
      actual_level_nodes.append(actual_node)
      #expand nodes
    for explo_node in actual_level_nodes:
       expand_nodes = create_successors(explo_node)
       for nodes in expand_nodes:
         node_state_tuple = tuple(nodes.state)
         if node_state_tuple not in explorados:
           fronteira.append(nodes)
           explorados.add(tuple(nodes.state))

if __name__ == "__main__":
  node = bfs(root)
  while (1):
    if not node.parent:
      break
    print(node.state, node.action)
    node = node.parent
  print(f"Nós visitados: {visit_nodes}")
    



