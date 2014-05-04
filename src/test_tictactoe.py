#TicTacToe classes and runtime
from mock import MagicMock, patch
import tictactoe
import runpy

def test_tictactoe():
    with patch('__builtin__.raw_input', MagicMock(side_effect = ['0 0', '0 1', '1 1', '0 2', '2 2', '1 0'])) as mock_raw_input:
        tictactoe.tictactoe()
    with patch('__builtin__.raw_input', MagicMock(side_effect = ['2 0', '0 1', '1 1', '1 0', '0 2', '1 0'])) as mock_raw_input:
        tictactoe.tictactoe()
    with patch('__builtin__.raw_input', MagicMock(side_effect = ['2 0', '1 1', '2 1', '1 2', '2 2', '1 0'])) as mock_raw_input:
        tictactoe.tictactoe()
    with patch('__builtin__.raw_input', MagicMock(side_effect = ['0 2', '0 1', '1 2', 'xxxx', 'ads233 j33j3j', '-1 -1', '500 2', '0 0', '0 0', '2 2', '1 0'])) as mock_raw_input:
        with patch('__builtin__.exit', MagicMock()):
            #tictactoe.tictactoe()
            runpy.run_module('tictactoe', run_name='__main__')

    try:
        tictactoe.TicTacToeBoard(1,0,'_')
    except Exception as e:
        pass

    try:
        tictactoe.HumanPlayer('Josh', tictactoe.TicTacToeBoard.EMPTY_SPOT)
    except Exception as e:
        pass


