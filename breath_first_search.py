from collections import deque

if __name__ == "__main__":
  fila = deque()
  for i in range(6, 0, -1):
    fila.append(i)
    
  print(fila)
  fila.pop()
  print(fila)  