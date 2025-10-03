from typing import List, Dict, Tuple, Set
from collections import deque
from generate_succeessors import create_successors
from Node import Node

init_board = [6,4,7,8,5,0,3,2,1]
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
  explorados = set(node.state)
  while True:
    actual_level_nodes = list()
    if not fronteira:
      return None
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
  while node:
    if not node.parent:
      break
    print(node.state, node.action)
    node = node.parent
  print(f"Nós visitados: {visit_nodes}")
    



