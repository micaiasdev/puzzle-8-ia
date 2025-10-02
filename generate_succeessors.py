from typing import List, Dict, Tuple, Set
init_board = [
              1,2,3,
              4,5,6,
              7,0,8
                    ]
     
def create_successors(board: List[int] = init_board):
  list_valid_boards = list()
  valid_positions = {0:(1,3), 
                     1:(0,2,4), 
                     2:(1,6), 
                     3:(0,4,6), 
                     4:(1,3,5,7), 
                     5:(4,2,8), 
                     6:(3,7), 
                     7:(6,4,8), 
                     8:(5,7)}
  current_pos = init_board.index(0)
  for pos in valid_positions[current_pos]:
    new_board = board.copy()
    aux = new_board[pos]
    new_board[pos] = new_board[current_pos]
    new_board[current_pos] = aux
    list_valid_boards.append(new_board)
  return list_valid_boards

def print_board(board: List[int]) -> None:
    """Imprime um tabuleiro em formato de matriz 3x3"""
    for linha in range(3):
        for coluna in range(3):
            index = linha * 3 + coluna
            valor = board[index]
            # Exibe 0 como espaço vazio para melhor visualização
            if valor == 0:
                print("  ", end=" ")
            else:
                print(f"{valor:2}", end=" ")
        print()  # Nova linha após cada linha da matriz

""" # Exemplo de uso
if __name__ == "__main__":
    sucessores = create_successors()
    print(f"Foram gerados {len(sucessores)} tabuleiros sucessores:\n")
    exibir_tabuleiros_matriz(sucessores) """