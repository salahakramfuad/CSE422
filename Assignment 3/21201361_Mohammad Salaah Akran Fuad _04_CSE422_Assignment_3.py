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


    print("\nOverall Results:")
    print(f"{players[0]} Wins: {max_wins if start_player == 0 else min_wins}")
    print(f"{players[1]} Wins: {min_wins if start_player == 0 else max_wins}")
    print(f"Draws: {draws}")

    # Final result
    if max_wins > min_wins:
        print(f"Overall Winner: {players[0] if start_player == 0 else players[1]}")
    elif min_wins > max_wins:
        print(f"Overall Winner: {players[1] if start_player == 0 else players[0]}")
    else:
        print("Overall Winner: Draw")




#Problem 2 starts here

def mind_control(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = (-10)**9
        for i in range(2):
            val = mind_control(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:

        val1 = mind_control(depth + 1, node_index * 2, True, values, alpha, beta, max_depth)
        val2 = mind_control(depth + 1, node_index * 2 + 1, True, values, alpha, beta, max_depth)
        best = max(val1, val2)
        return best


#game simulation with and without mind control

def game(maxV, minV):
    max_depth = 5
    num_leaf_nodes = 2 ** max_depth


    leaf_values = []
    for i in range(num_leaf_nodes):
      leaf_values.append(utility(maxV, minV))


    result_without_magic = chessmaster(0, 0, True, leaf_values, -10**9, 10*9, max_depth)


    result_with_magic = mind_control(0, 0, True, leaf_values, -10**9, 10**9, max_depth)

    return result_without_magic, result_with_magic



def problem_2():


    start_player = int(input("Enter who goes first (0 for Light, 1 for L): "))
    mind_control_cost = float(input("Enter the cost of using Mind Control: "))
    maxV = float(input("Enter base strength for Light: "))
    minV = float(input("Enter base strength for L: "))

    players = ["Light", "L"]


    if start_player == 0:
        max_player, min_player = players[0], players[1]
    else:
        max_player, min_player = players[1], players[0]


    result_without_magic, result_with_magic = game(maxV, minV)


    result_with_magic_after_cost = result_with_magic - mind_control_cost


    print(f"\nMinimax value without Mind Control: {result_without_magic:.2f}")
    print(f"Minimax value with Mind Control: {result_with_magic:.2f}")
    print(f"Minimax value with Mind Control after incurring the cost: {result_with_magic_after_cost:.2f}")

    # Decision making
    if result_with_magic_after_cost > result_without_magic:
        print(f"{max_player} should use Mind Control.")
    else:
        print(f"{max_player} should NOT use Mind Control as the position is {'already winning' if result_without_magic > 0 else 'losing either way'}.")






problem_2()