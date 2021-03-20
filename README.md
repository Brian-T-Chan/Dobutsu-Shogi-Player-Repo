# Dobutsu-Shogi-Player-Repo
This repository contains a computer program that plays Dobutsu Shogi. It uses alpha-beta pruning and it has five levels of difficulty (ranging from 3 ply to 7 ply). It uses a command-line style user interface. To run the program, run main.py. In addition to the licensing file and (this) readme file, the repository contains the following six files.

alphabeta.py : Runs the alpha-beta pruning algorithm to determine moves.

board.py : Constructs the game board along with all pieces, and provides essential functionality such as determining when one player has won the game.

board_display.py : Displays the pieces and the game board.

board_hardware.py : Is a program that allows the internal state of the game board to change after a player makes a move.

board_input.py : Translates user input for "player actions" (a move or a drop by a player) to commands understood by board_hardware.py then uses board_input.py to execute such commands.

main.py : The user-interface.
