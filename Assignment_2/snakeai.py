from typing import Tuple
import random
import board
import direction


class SnakeAI:
    # Rewrite this to make it more intelligent.
    # The function should return a direction
    # Notice that the snake can't turn to the complete oposite direction
    # Going up right now, the snake can't suddenly go down without turning first
    def get_next_move(self, game_board: board.Board) -> tuple:

        options = [direction.DOWN, direction.UP,
                   direction.RIGHT, direction.LEFT]

        # Direct the snake in the direction of the apple. Check the coordinates of the head and
        # compare that to the coordinates of the apple. Make a turn accordingly if you need to.
        if game_board.snake.head()[0] <= game_board.apple[0]:
            if direction.LEFT in options:
                options.remove(direction.LEFT)
        if game_board.snake.head()[0] >= game_board.apple[0]:
            if direction.RIGHT in options:
                options.remove(direction.RIGHT)
        if game_board.snake.head()[1] <= game_board.apple[1]:
            if direction.UP in options:
                options.remove(direction.UP)
        if game_board.snake.head()[1] >= game_board.apple[1]:
            if direction.DOWN in options:
                options.remove(direction.DOWN)

       # If you are about to move outside of the board, pick another direction.
        if game_board.snake.head()[0] == 0:
            if direction.LEFT in options:
                options.remove(direction.LEFT)
        if game_board.snake.head()[0] == game_board.board_size_x - 1:
            if direction.RIGHT in options:
                options.remove(direction.RIGHT)
        if game_board.snake.head()[1] == 0:
            if direction.UP in options:
                options.remove(direction.UP)
        if game_board.snake.head()[1] == game_board.board_size_y - 1:
            if direction.DOWN in options:
                options.remove(direction.DOWN)

        # If  the  square  that  you  are  about  to  move  to  is  part  of  your  own  body,  try  another
        # square.  Checking  the  is_snake_crossing_itself  function  in  snake.py  could  be  a  good
        # inspiration for building this rule.
        if game_board.snake.is_snake_crossing_itself():
            if game_board.snake.last_direction == direction.UP:
                if direction.UP in options:
                    options.remove(direction.UP)
            if game_board.snake.last_direction == direction.DOWN:
                if direction.DOWN in options:
                    options.remove(direction.DOWN)
            if game_board.snake.last_direction == direction.LEFT:
                if direction.LEFT in options:
                    options.remove(direction.LEFT)
            if game_board.snake.last_direction == direction.RIGHT:
                if direction.RIGHT in options:
                    options.remove(direction.RIGHT)

        for option in options:
            # Taken from 180 turn.
            if option == tuple([p * -1 for p in game_board.snake.last_direction]):
                options.remove(option)
        # If no "good" options according to heuristc, do the same as last time.
        if not options:
            ai_decision = game_board.snake.last_direction
        # Take any "good" decision.
        else:
            ai_decision = random.choice(options)
        return ai_decision
