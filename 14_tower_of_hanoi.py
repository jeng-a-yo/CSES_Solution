def hanoi(n, source, target, auxiliary, moves):
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi(n - 1, auxiliary, target, source, moves)

n = int(input())
moves = []
hanoi(n, 1, 3, 2, moves)

# Output the total number of moves
print(len(moves))
# Output the sequence of moves
for move in moves:
    print(move[0], move[1])
