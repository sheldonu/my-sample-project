# Tic-Tac-Toe Assignment -- Sheldon Uchytil

def print_tic_tac_toe(values):
	print("{}|{}|{}".format(values[0], values[1], values[2]))
	print('-+-+-')

	print("{}|{}|{}".format(values[3], values[4], values[5]))
	print('-+-+-')

	print("{}|{}|{}".format(values[6], values[7], values[8]))
	print('-+-+-')

def check_win(player_pos, cur_player):

	# All possible winning combinations
	winner = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

	# Loop to check if any winning combination is satisfied
	for x in winner:
		if all(y in player_pos[cur_player] for y in x):

			# Return True if any winning combination satisfies
			return True
	# Return False if no combination is satisfied		
	return False

def check_draw(player_pos):
	if len(player_pos['x']) + len(player_pos['o']) == 9:
		return True
	return False

def single_game(cur_player):

	# Represents the Tic Tac Toe
	values = [' ' for x in range(9)]
	
	# Stores the positions occupied by X and O
	player_pos = {'x':[], 'o':[]}
	
	# Game Loop for a single game of Tic Tac Toe
	while True:
		print_tic_tac_toe(values)
		
		# Try exception block for MOVE input
		try:
			print("Player ", cur_player, " turn. Which box? : ", end="")
			move = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again")
			continue

		# Sanity check for MOVE inout
		if move < 1 or move > 9:
			print("Wrong Input!!! Try Again")
			continue

		# Check if the box is not occupied already
		if values[move-1] != ' ':
			print("Place already filled. Try again!!")
			continue

		# Updating grid status 
		values[move-1] = cur_player

		# Updating player positions
		player_pos[cur_player].append(move)

		# Function call for checking win
		if check_win(player_pos, cur_player):
			print_tic_tac_toe(values)
			print("Player ", cur_player, " has won the game!!")		
			print("\n")
			return cur_player

		# Function call for checking draw game
		if check_draw(player_pos):
			print_tic_tac_toe(values)
			print("Game Drawn")
			print("\n")
			return 'D'

		# Switch player moves
		if cur_player == 'x':
			cur_player = 'o'
		else:
			cur_player = 'x'

if __name__ == "__main__":

	print("Player 1")
	player1 = input("Enter the name : ")
	print("\n")

	print("Player 2")
	player2 = input("Enter the name : ")
	print("\n")
	
	# Stores the player who chooses X and O
	cur_player = player1

	# Stores the choice of players
	player_choice = {'x' : "", 'o' : ""}

	# Stores the options
	options = ['x', 'o']

	# Game Loop for a series of Tic Tac Toe
	# The loop runs until the players quit 
	while True:

		# Player choice Menu
		print("Turn to choose for", cur_player)
		print("Enter 1 for x")
		print("Enter 2 for o")
		print("Enter 3 to Quit")

		# Try exception for CHOICE input
		try:
			choice = int(input())	
		except ValueError:
			print("Wrong Input!!! Try Again\n")
			continue

		# Conditions for player choice	
		if choice == 1:
			player_choice['x'] = cur_player
			if cur_player == player1:
				player_choice['o'] = player2
			else:
				player_choice['o'] = player1

		elif choice == 2:
			player_choice['o'] = cur_player
			if cur_player == player1:
				player_choice['x'] = player2
			else:
				player_choice['x'] = player1

		else:
			print("Wrong Choice!!!! Try Again\n")

		# Stores the winner in a single game of Tic Tac Toe
		winner = single_game(options[choice-1])

		# Switch player who chooses X or O
		if cur_player == player1:
			cur_player = player2
		else:
			cur_player = player1