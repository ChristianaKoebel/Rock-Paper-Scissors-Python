import check # see check.py for the 'check' module
    
# fib(n) produces the nth Fibonacci number
# fib: Nat -> Nat
# Examples: 
#   fib(0) => 0
#   fib(1) => 1
#   fib(2) => 1
#   fib(3) => 2
#   fib(4) => 3
#   fib(10) => 55
    
def fib(n):
    fib_seq = [0, 1, 1]
    for i in range(3, n + 1):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq[n]

# rps() produces None and prints a game of rock, paper, scissors played
#    between the computer and a human player, who plays their next move after
#    reading a printed prompt asking them how they want to proceed (either r, p, s, or q).

# rps: None -> None

# Effects: prints a welcome message and a prompt asking the player what they
#    want to play next, and reads in the choice. Each round, a line is 
#    printed indicating what was played and who won. At the end of the game,
#    total game statistics are printed.

# Examples:
# If the player chooses q right away, there will be zero tied games, zero player
#    wins, and zero computer wins.
# If the game lasts four rounds, with the player's choices: r, s, p, s, q (in that
#    order), there will be zero tied games, one player win, and three computer wins.

welcome_message = "Welcome to the Rock-Paper-Scissors game!"
prompt = "How would you like to play next? Type r, p, s, or q\n"
goodbye_message = "Thank you for playing! Total game statistics:"

def rps():
    print(welcome_message)
    player_move = input(prompt)
    tied_stats = 0
    player_win = 0
    computer_win = 0
    n = 1
    while player_move != "q":
        if player_move not in ["r", "p", "s", "q"]:
            print("Invalid move. Enter r, p, s, or q.")
            player_move = input(prompt)
            continue
        fibo_n = fib(n)
        if fibo_n % 3 == 0:
            computer_move = "r"
        if fibo_n % 3 == 1:
            computer_move = "p"
        if fibo_n % 3 == 2:
            computer_move = "s"
        general_message = "Player plays:" + " " + player_move + "." + " Computer plays:" + " " + computer_move + "." + " "
        if player_move == computer_move:
            print(general_message + "Tied.")
            tied_stats = tied_stats + 1
            n = n + 1
            player_move = input(prompt)
            continue
        if player_move == "r":
            if computer_move == "s":
                print(general_message + "Player won.")
                player_win = player_win + 1
            if computer_move == "p":
                print(general_message + "Computer won.")
                computer_win = computer_win + 1
            n = n + 1
            player_move = input(prompt)
            continue
        if player_move == "p":
            if computer_move == "r":
                print(general_message + "Player won.")
                player_win = player_win + 1
            if computer_move == "s":
                print(general_message + "Computer won.")
                computer_win = computer_win + 1
            n = n + 1
            player_move = input(prompt)
            continue
        if player_move == "s":
            if computer_move == "p":
                print(general_message + "Player won.")
                player_win = player_win + 1
            if computer_move == "r":
                print(general_message + "Computer won.")
                computer_win = computer_win + 1
            n = n + 1
            player_move = input(prompt)
            continue
    print(goodbye_message)
    print("Tied games:" + " " + str(tied_stats) + ".")
    print("Player won" + " " + str(player_win) + " " + "times.")
    print("Computer won" + " " + str(computer_win) + " " + "times.") 
    
# Testing

# Test 1: Player enters "q" right away
check.set_input(["q"])
check.set_screen("0 tied games, 0 player wins, 0 computer wins")
check.expect("T1", rps(), None)

# Test 2: One round, tie game
check.set_input(["p","q"])
check.set_screen("1 tie game, 0 player wins, 0 computer wins")
check.expect("T2", rps(), None)

# Test 3: One round, player wins
check.set_input(["s","q"])
check.set_screen("0 tied games, 1 player win, 0 computer wins")
check.expect("T3", rps(), None)

# Test 4: One round, computer wins
check.set_input(["r","q"])
check.set_screen("0 tied games, 0 player wins, 1 computer win")
check.expect("T4", rps(), None)

# Test 5: Two rounds, all ties
check.set_input(["p","p","q"])
check.set_screen("2 tied games, 0 player wins, 0 computer wins")
check.expect("T5", rps(), None)

# Test 6: Two rounds, 2 player wins
check.set_input(["s","s","q"])
check.set_screen("0 ties, 2 player wins, 0 computer wins")
check.expect("T6", rps(), None)

# Test 7: Two rounds, 2 computer wins
check.set_input(["r","r","q"])
check.set_screen("0 ties, 0 player wins, 2 computer wins")
check.expect("T7", rps(), None)

# Test 8: Two rounds, one win each
check.set_input(["s","r","q"])
check.set_screen("0 ties, 1 player win, 1 computer win")
check.expect("T8", rps(), None)

# Test 9: Three rounds, all ties
check.set_input(["p","p","s","q"])
check.set_screen("3 ties, 0 player wins, 0 computer wins")
check.expect("T9", rps(), None)

# Test 10: Three rounds, all player wins
check.set_input(["s","s","r","q"])
check.set_screen("0 ties, 3 player wins, 0 computer wins")
check.expect("T10", rps(), None)

# Test 11: Three rounds, all computer wins
check.set_input(["r","r","p","q"])
check.set_screen("0 ties, 0 player wins, 3 computer wins")
check.expect("T11", rps(), None)

# Test 12: Three rounds, one tie, one player win, one computer win
check.set_input(["p","r","r","q"])
check.set_screen("1 tie, 1 player win, 1 computer win")
check.expect("T12", rps(), None)

# Test 13: Four rounds, all ties
check.set_input(["p","p","s","r","q"])
check.set_screen("4 ties, 0 player wins, 0 computer wins")
check.expect("T13", rps(), None)

# Test 14: Four rounds, all player wins
check.set_input(["s","s","r","p","q"])
check.set_screen("0 ties, 4 player wins, 0 computer wins")
check.expect("T14", rps(), None)

# Test 15: Four rounds, all computer wins
check.set_input(["r","r","p","s","q"])
check.set_screen("0 ties, 0 player wins, 4 computer wins")
check.expect("T15", rps(), None)

# Test 16: Four rounds, 1 tie, 1 player win, 2 computer wins
check.set_input(["p","s","p","s","q"])
check.set_screen("1 tie, 1 player win, 2 computer wins")
check.expect("T16", rps(), None)

# Test 17: Four rounds, 0 ties, 1 player win, 3 computer wins
check.set_input(["r","s","p","s","q"])
check.set_screen("0 ties, 1 player win, 3 computer wins")
check.expect("T17", rps(), None)
