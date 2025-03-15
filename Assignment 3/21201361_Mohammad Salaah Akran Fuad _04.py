import math
import random


#strength Function

def stregnth(x):
    return (math.log2( x +1 ) + x / 10)


#Utility Function

def utility(maxV , minV):
  i= random.choice([0,1])
  return stregnth(maxV) - stregnth(minV) + ((-1) ** i) * random.randint(1, 10) / 10



def chessmaster(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = (-10)**9
        for i in range(2):  # Two possible moves
            val = chessmaster(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break   #breaks traverse to the immediate branch(pruning)
        return best
    else:
        best = 10**9
        for i in range(2):  # Two possible moves
            val = chessmaster(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  #breaks traverse to the immediate branch(pruning)
        return best

#Creating the tree and values
def play_game(maxV, minV, is_max_start):
    max_depth = 5
    num_leaf_nodes = 2 ** max_depth  # number of leaves on power of 2 since 2 player only

    end_values = []
    for i in range(num_leaf_nodes):
      end_values.append(utility(maxV, minV))

    # initiate the game
    result = chessmaster(0, 0, is_max_start, end_values, (-10)**9, (10)**9, max_depth)
    return result

def problem_1():

    start_player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
    maxV = float(input("Enter base strength for Carlsen: "))
    minV = float(input("Enter base strength for Caruana: "))


    players = ["Magnus Carlsen", "Fabiano Caruana"]
    max_wins, min_wins, draws = 0, 0, 0


    for game in range(4):

        current_start_player = (start_player + game) % 2

        if current_start_player == 0:
            max_player = players[0]
            min_player = players[1]
            result = play_game(maxV, minV, True)
            max = True
        else:
            max_player = players[1]
            min_player = players[0]
            result = play_game(minV, maxV, True)
            max=False


        if result > 0:
            max_wins += 1
            winner = max_player

        elif result < 0:
            min_wins += 1
            winner = min_player

        else:
            draws += 1
            winner = 'Draw'

        # Print the result of the current game
        print(f"Game {game + 1} Winner: {winner} ({'Max' if max else 'Min'}) (Utility value: {result:.2f})")

    # Print overall results
    print("\nOverall Results:")
    print(f"{players[0]} Wins: {max_wins if start_player == 0 else min_wins}")
    print(f"{players[1]} Wins: {min_wins if start_player == 0 else max_wins}")
    print(f"Draws: {draws}")

    # Determine the overall winner
    if max_wins > min_wins:
        print(f"Overall Winner: {players[0] if start_player == 0 else players[1]}")
    elif min_wins > max_wins:
        print(f"Overall Winner: {players[1] if start_player == 0 else players[0]}")
    else:
        print("Overall Winner: Draw")

problem_1()