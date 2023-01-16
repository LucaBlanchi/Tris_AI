from tkinter import *
import os

def replace2(x):
    if x == 2:
        return -1
    return x

def game(network, save_data, vs_ai, ai_starts):
    sq_coord =  {
        "1": "00",
        "2": "01",
        "3": "02",
        "4": "10",
        "5": "11",
        "6": "12",
        "7": "20",
        "8": "21",
        "9": "22"
    }

    def create_squares():
        square_1.grid(row=0, column=0, ipadx=20, ipady=20)
        square_2.grid(row=0, column=1, ipadx=20, ipady=20)
        square_3.grid(row=0, column=2, ipadx=20, ipady=20)
        square_4.grid(row=1, column=0, ipadx=20, ipady=20)
        square_5.grid(row=1, column=1, ipadx=20, ipady=20)
        square_6.grid(row=1, column=2, ipadx=20, ipady=20)
        square_7.grid(row=2, column=0, ipadx=20, ipady=20)
        square_8.grid(row=2, column=1, ipadx=20, ipady=20)
        square_9.grid(row=2, column=2, ipadx=20, ipady=20)

    def new_game():
        global game_grid
        global turn
        turn = 0
        for i in range(9):
            labels[i].grid_remove()
            squares[i]["state"]="active"
        label_win_X.grid_remove()
        label_win_O.grid_remove()
        label_draw.grid_remove()
        create_squares()
        game_grid = [0]*9
        new_game_button.grid_remove()
        if ai_starts:
            ai_moves(network)

    def win(player):
        if player == "X":
            label_win_X.grid(row=3, column=0, columnspan=3)
        else:
            label_win_O.grid(row=3, column=0, columnspan=3)
        new_game_button.grid(row=4, column=0, columnspan=3)
        for i in range(9):
            squares[i]["state"] = "disabled"

    def draw():
        new_game_button.grid(row=4, column=0, columnspan=3)
        label_draw.grid(row=3, column=0, columnspan=3)

    def check_win():
        global game_grid
        if ((game_grid[0] == 1 and game_grid[1] == 1 and game_grid[2] == 1)
            or (game_grid[3] == 1 and game_grid[4] == 1 and game_grid[5] == 1)
            or (game_grid[6] == 1 and game_grid[7] == 1 and game_grid[8] == 1)
            or (game_grid[0] == 1 and game_grid[3] == 1 and game_grid[6] == 1)
            or (game_grid[1] == 1 and game_grid[4] == 1 and game_grid[7] == 1)
            or (game_grid[2] == 1 and game_grid[5] == 1 and game_grid[8] == 1)
            or (game_grid[0] == 1 and game_grid[4] == 1 and game_grid[8] == 1)
            or (game_grid[2] == 1 and game_grid[4] == 1 and game_grid[6] == 1)):
            win("X")
            return True
        elif ((game_grid[0] == 2 and game_grid[1] == 2 and game_grid[2] == 2)
            or (game_grid[3] == 2 and game_grid[4] == 2 and game_grid[5] == 2)
            or (game_grid[6] == 2 and game_grid[7] == 2 and game_grid[8] == 2)
            or (game_grid[0] == 2 and game_grid[3] == 2 and game_grid[6] == 2)
            or (game_grid[1] == 2 and game_grid[4] == 2 and game_grid[7] == 2)
            or (game_grid[2] == 2 and game_grid[5] == 2 and game_grid[8] == 2)
            or (game_grid[0] == 2 and game_grid[4] == 2 and game_grid[8] == 2)
            or (game_grid[2] == 2 and game_grid[4] == 2 and game_grid[6] == 2)):
            win("O")
            return True
        else:
            for i in range(9):
                if game_grid[i] == 0:
                    break
                if i == 8:
                    draw()
                    return True
        return False

    def add_data(game_grid, sq):
        s = ["0","0","0","0","0","0","0","0","0"]
        s[sq-1] = "1"
        s = "".join(s)
        d = ''.join(str(number) for number in game_grid)
        path = os.path.dirname(os.path.realpath(__file__)) + "/data"
        f = open(path,'a')
        f.write(d + ","+ s + "\n")
    
    def ai_moves(network):
        global game_grid
        global turn
        input = game_grid
        input = list(map(replace2, input))
        input = list(map(int, input))
        network.input_layer = input
        network.compute_network()
        l = sorted(range(len(network.output_layer)), key=lambda k: network.output_layer[k])
        l.reverse()
        l = [x+1 for x in l]
        for i in range(len(l)):
            if game_grid[l[i]-1] == 0:
                label_square(l[i])
                turn = turn + 1
                break
        check_win()

    def label_square(sq):
        global game_grid
        squares[sq-1].grid_remove()
        labels[turn].grid(row=sq_coord[str(sq)][0], column=sq_coord[str(sq)][1])
        game_grid[sq-1] = (turn%2)+1

    def click_square(sq):
        global turn
        global game_grid
        if save_data:
            add_data(game_grid, sq)
        label_square(sq)
        turn = turn + 1
        if not check_win() and vs_ai:
            ai_moves(network)

    root = Tk()

    global turn
    turn = 0

    global game_grid
    game_grid = [0]*9

    root.title("Tris")

    label_1 = Label(root, text="X", padx=25, pady=25)
    label_2 = Label(root, text="O", padx=25, pady=25)
    label_3 = Label(root, text="X", padx=25, pady=25)
    label_4 = Label(root, text="O", padx=25, pady=25)
    label_5 = Label(root, text="X", padx=25, pady=25)
    label_6 = Label(root, text="O", padx=25, pady=25)
    label_7 = Label(root, text="X", padx=25, pady=25)
    label_8 = Label(root, text="O", padx=25, pady=25)
    label_9 = Label(root, text="X", padx=25, pady=25)

    labels = [label_1, label_2, label_3, 
                label_4, label_5, label_6,
                label_7, label_8, label_9]

    square_1 = Button(root, command=lambda: click_square(1))
    square_2 = Button(root, command=lambda: click_square(2))
    square_3 = Button(root, command=lambda: click_square(3))
    square_4 = Button(root, command=lambda: click_square(4))
    square_5 = Button(root, command=lambda: click_square(5))
    square_6 = Button(root, command=lambda: click_square(6))
    square_7 = Button(root, command=lambda: click_square(7))
    square_8 = Button(root, command=lambda: click_square(8))
    square_9 = Button(root, command=lambda: click_square(9))

    squares = [square_1, square_2, square_3,
                square_4, square_5, square_6,
                square_7, square_8, square_9]

    create_squares()

    label_win_X = Label(root, text="Player X wins!")
    label_win_O = Label(root, text="Player O wins!")
    label_draw = Label(root, text="It's a draw!")

    new_game_button = Button(master=root, text="New Game", command=new_game)

    if vs_ai and ai_starts:
        ai_moves(network)

    root.mainloop() 