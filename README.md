# Dobutsu-Shogi-Player-Repo
This repository contains a computer program that plays Dobutsu Shogi. Dobutsu Shogi, also known as Animal Shogi, is a popular board game for
programmers and hobbyists (mostly in Japan). The game was designed by a professional Shogi player and intended for children learning Shogi. Due to the relatively small size of this board game, I was thinking of applying the minimax algorithm to it as a first solo project on GitHub. Subsequently, I found that alpha-beta pruning dramatically sped up my program's performance and allowed me to increase search depth. I made small modifications to the standard alpha-beta pruning algorithm in order for my program to evaluate moves even more quickly and accurately.

My program has five levels of difficulty (ranging from 3 ply to 7 ply). The lowest level, Level 1, is
the easiest level and the program only looks three moves ahead (1 move = 1 player moves or drops one piece). The highest Level 5, is the hardest
level and the program looks seven moves ahead. The lower the level, the quicker the program will respond.

My program uses a command-line style user interface. To run the program, run main.py. In addition to the licensing file and (this) readme file, the repository contains the following six files.

alphabeta.py : Runs the alpha-beta pruning algorithm to determine moves.

board.py : Constructs the game board along with all pieces, and provides essential functionality such as determining when one player has won the game.

board_display.py : Displays the pieces and the game board.

board_hardware.py : Is a program that allows the internal state of the game board to change after a player makes a move.

board_input.py : Translates user input for "player actions" (a move or a drop by a player) to commands understood by board_hardware.py then uses board_input.py to execute such commands.

main.py : The user-interface.
