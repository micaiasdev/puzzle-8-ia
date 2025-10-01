class Node: 
  def __init__(self, state, action, parent):
    self.state = state
    self.action = action
    self.parent = parent
    if parent is not None:
      self.cost = parent.cost + 1
    else:
      self.cost = 0
    
    
if __name__ == "__main__":
  raiz = Node([1,2,3,0,4,5,6,7,8], None, None)
  filho = Node([1,2,3,4,0,5,6,7,8], "right", raiz)
   
  print(filho.parent.cost)