#TicTacToe classes and runtime


class TicTacToeBoard():
    EMPTY_SPOT = '_'

    def __init__(self, x=3, y=3, win_length=3):
        self.__board = TicTacToeBoard.build_board(x, y, TicTacToeBoard.EMPTY_SPOT)
        self.win_length = win_length
        self.__last_error = None

    @classmethod
    def build_board(cls, x, y, symbol):
        if x < 1 or y < 1:
            raise 'Board dimensions must be greater than 0.'
        return [[symbol for second_param in range(y)] for first_param in range(x)]

    def max_x(self):
        return len(self.__board)-1

    def max_y(self):
        return len(self.__board[0])-1

    def next_column(self, x, y):
        x += 1
        x %= len(self.__board)
        return x, y, x==0

    def next_row(self, x, y):
        y += 1
        y %= len(self.__board[0])
        return x, y, y==0

    def prev_column(self, x, y):
        x -= 1
        x %= len(self.__board)
        return x, y, x==len(self.__board)

    def next_diagonal(self, x, y): #down and right
        x, y, overflow1 = self.next_column(x, y)
        x, y, overflow2 = self.next_row(x, y)
        return x, y, overflow1 or overflow2

    def next_alt_diagonal(self, x, y): #down and left
        x, y, overflow1 = self.prev_column(x, y)
        x, y, overflow2 = self.next_row(x, y)
        return x, y, overflow1 or overflow2

    def fill(self, x, y, symbol):
        retval = False
        try:
            if self.__board[x][y] == TicTacToeBoard.EMPTY_SPOT:
                self.__board[x][y] = symbol
                #self.__last_error = None 
                retval = True
            else:
                self.__last_error = '***Position (%d, %d) is already filled with %s.***' % (x, y, self.__board[x][y])
        except IndexError as e:
            self.__last_error = '***Position (%d, %d) is not a valid position***' % (x, y)
        return retval

    def get_unique_symbols(self):
        return set([item for column in self.__board for item in column]) #itertools.chain here perhaps

    #def clear_board #not necessary currently
    def get_winners(self, next, round_robin=False):
        #print(str(next))
        symbols = self.get_unique_symbols()
        if TicTacToeBoard.EMPTY_SPOT in symbols:
            symbols.remove(TicTacToeBoard.EMPTY_SPOT)
        symbol_count = dict(zip(symbols, [0]*len(symbols)))
        winners = set()
        for orig_y in range(len(self.__board[0])):
          for orig_x in range(len(self.__board)):
            max_repeat_count = 3
            if not round_robin:
                max_repeat_count = 1
            repeat_count = 0
            x = orig_x
            y = orig_y
            prev_symbol = self.__board[x][y]
            #next = TicTacToeBoard.next_column
            while repeat_count < max_repeat_count:
                prev_symbol = self.__board[x][y]
                #print('previous location (%d, %d)' % (x, y))
                x, y, overflow = next(x, y)
                #print('new location (%d, %d)' % (x, y))
                if overflow and not round_robin:
                    symbol_count = dict(zip(symbols, [0]*len(symbols)))
                    #skip check for comparison against prev_symbol, as it does not count
                else:
                    if self.__board[x][y] == prev_symbol and not prev_symbol == TicTacToeBoard.EMPTY_SPOT:
                        #print 'CHAIN for "%s" at (%d, %d)' % (prev_symbol, x, y)
                        symbol_count[prev_symbol] += 1
                    else:
                        symbol_count[prev_symbol] = 0
                    if symbol_count[prev_symbol] >= self.win_length - 1:
                        #print 'WINNER LOCATED!'
                        winners.add(prev_symbol)
                if x == orig_x and y == orig_y:
                    repeat_count += 1
        return winners

    def declare_winners(self, round_robin=False):
        #rows = self.get_rows(round_robin)
        #columns = self.get_columns(round_robin)
        #diagonals = self.get_diagonals(round_robin)
        #alt_diagonals = self.get_alt_diagonals(round_robin)
        winners1 = self.get_winners(self.next_column, round_robin)
        winners2 = self.get_winners(self.next_row, round_robin)
        winners3 = self.get_winners(self.next_diagonal, round_robin)
        winners4 = self.get_winners(self.next_alt_diagonal, round_robin)
        retval = set(winners1) | set(winners2) | set(winners3) | set(winners4)
        return retval

    def last_error(self):
        return str(self.__last_error)

    def __str__(self):
        height = len(self.__board[0])
        width = len(self.__board)
        line_separator = '\n' + '-' * width * 4 + '\n '
        item_separator = ' | '
        retval = ' ' + line_separator.join([item_separator.join([self.__board[x][y] for x in range(width)]) for y in range(height)])
        return retval



class HumanPlayer():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = str(symbol)[0]
        if self.symbol is TicTacToeBoard.EMPTY_SPOT:
            raise 'Cannot set HumanPlayer symbol to TicTacToeBoard.EMPTY_SPOT, "%s".' % TicTacToeBoard.EMPTY_SPOT
    
    @classmethod
    def get_move(cls):
        valid_integers = False
        x = None
        y = None
        while not valid_integers:
            s = raw_input('Enter two integers separated by a space: --> ')
            try:
                splits = s.split(' ')
                x = int(splits[0])
                y = int(splits[1])
                valid_integers = True
            except Exception as e:
                pass
        return x, y

    def take_turn(self, board):
        move_taken = False
        error_msg = ''
        #error_count = 0
        #max_error_count = 20
        while not move_taken:
            print('')
            print('')
            print(str(board))
            print(error_msg)
            print('What move for %s? (0,0) through (%d,%d)' % (self.name, board.max_x(), board.max_y()))
            x, y = HumanPlayer.get_move()
            if board.fill(x, y, self.symbol):
                move_taken = True
            else:
                error_msg = board.last_error() 
                #error_count += 1
                #if error_count > max_error_count:
                #    raise 'Too many errors on HumanPlayer input'

class TicTacToe(object):
    def __init__(self):
        player1 = HumanPlayer('Dave', 'X')
        player2 = HumanPlayer('Kris', 'O')
        player1.next = player2
        player2.next = player1
        self.players = [player1, player2]
        self.current_player = player1
        self.winner = None

    def play(self):
        self.introduction()
        board = TicTacToeBoard()
        game_over = False
        while not game_over:
            self.current_player.take_turn(board)
            winners = board.declare_winners()
            if self.current_player.symbol in winners:
                self.winner = self.current_player
                game_over = True
            else:
                self.current_player = self.current_player.next
        self.report_ending(board)

    def introduction(self):
        for index, player in enumerate(self.players):
            print('Player%d: %s, "%s"' % (index, player.name, player.symbol))

    def report_ending(self, board):
        print('')
        print('')
        print(str(board))
        print('')
        #print('Looks like we have a winner.')
        print('"%s", wielding "%s", wins in mortal tic-tac-combat. To the victor go the spoils!' % (self.winner.name, self.winner.symbol))
        print('Congratulations!')
            
def tictactoe():
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    tictactoe()
    exit(0)

       
