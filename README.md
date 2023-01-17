# Tris_AI
Tic-Tac-Toe implementation based on artificial intelligence, consisting of a neural network that can be trained using data collected while playing. Run main.py to use it.

network.py contains the network class, with the backpropagation and train methods. Between the input and output layers, the network has two middle layers, the size of which can be specified in main.py together with other parameters.

data.txt stores data from games that is used to train the network.

main.py creates the GUI. The 'Load Data' button loads the data from data.txt. The data is also automatically loaded when main.py is launched, but the user may want to update it. The Clear Data button clears data.txt. The 'Train' button trains the network, for a number of iterations specified in main.py. The 'Play' button starts the game. Use the checkmarks to indicate if you want to play against the network (or another player), if the neural network should play first, and if you want to save the moves in data.txt. The Check Move button can be used to check the explicit output of the neural net, by inserting the state of the game grid in the entry: 0s for empty squares, 1 for crosses, and 2 for circles, in reading order.

game.py contains the game function that launches the tic-tac-toe window.

utilities.py contains some small functions used throughout the script.
