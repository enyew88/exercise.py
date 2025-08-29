#1
for i in range(1, 11):
    print(i)
#2
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1
#3
n = 3
for i in range(1, n+1):
    print("*" * i)
#3
n = 20
for num in range(2, n+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
#4
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))
#5
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))
#6
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
#7
for i in range(1, 11):
    if i == 7:
        break
    print(i)
#8
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')
#9
board = [" "] * 9

def print_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-+-+-")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-+-+-")
    print(board[6]+"|"+board[7]+"|"+board[8])

player = "X"
for i in range(9):
    print_board()
    move = int(input(f"Player {player}, enter position (0-8): "))
    if board[move] == " ":
        board[move] = player
        player = "O" if player == "X" else "X"
    else:
        print("Invalid move!")
