import random


class Player:
    """Represents a player in the game.

    Attributes:
        letter (str): A string representing the player's letter ('X' or 'O').

    Methods:
        get_move(game): Get the player's next move given the current game state.
    """

    def __init__(self, letter):
        """Initializes a new instance of the Player class.

        Args:
            letter (str): A string representing the player's letter ('X' or 'O').
        """
        self.letter = letter

    def get_move(self, game):
        """Get the player's next move given the current game state.

        This method must be implemented by all subclasses of the Player class.

        Args:
            game (TicTacToe): The current TicTacToe game instance.

        Returns:
            int: The index of the square the player has chosen to mark on the board.
        """
        pass


class RandomComputerPlayer(Player):
    """Represents a computer player that makes random moves.

    Inherits from the Player class.

    Attributes:
        letter (str): A string representing the player's letter ('X' or 'O').

    Methods:
        get_move(game): Get the computer player's next move given the current game state.
    """

    def __init__(self, letter):
        """Initializes a new instance of the RandomComputerPlayer class.

        Args:
            letter (str): A string representing the player's letter ('X' or 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """Get the computer player's next move given the current game state.

        Args:
            game (TicTacToe): The current TicTacToe game instance.

        Returns:
            int: The index of a randomly chosen square that is available on the board.
        """
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    """Represents a human player that gets moves from user input.

    Inherits from the Player class.

    Attributes:
        letter (str): A string representing the player's letter ('X' or 'O').

    Methods:
        get_move(game): Get the human player's next move given the current game state.
    """

    def __init__(self, letter):
        """Initializes a new instance of the HumanPlayer class.

        Args:
            letter (str): A string representing the player's letter ('X' or 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """Get the human player's next move given the current game state.

        Prompts the user to input a square to mark on the board, validates the input,
        and returns the index of the chosen square.

        Args:
            game (TicTacToe): The current TicTacToe game instance.

        Returns:
            int: The index of the square the user has chosen to mark on the board.
        """
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val
