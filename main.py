import network
import os
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
import game

it = 10000
step = 0.15
sizes = [4,4]

class window(Tk):
	def __init__(self):
		super().__init__()
		Style(theme="vapor")
		self.style = ttk.Style(self)

def replace2(x):
    if x == 2:
        return -1
    return x

def load_data():
        global data
        path = os.path.dirname(os.path.realpath(__file__)) + "/data"
        with open(path, 'r') as f:
                data_size = sum(1 for _ in f)
        data = [[[0 for _ in range (9)],[0 for _ in range (0,9)]] for _ in range (data_size)]

        with open(path, 'r') as f:
                f.seek(0)
                for i in range(data_size):
                        line = f.readline()
                        data[i][0] = line[:9]
                        data[i][1] = line[10:-1]
        f.close()

        for i in range(len(data)):
                data[i][0] = list(map(int, [*data[i][0]]))
                data[i][0] = list(map(replace2, data[i][0]))
                data[i][1] = list(map(int, [*data[i][1]]))
                data[i][1] = list(map(replace2, data[i][1]))

def clear_data():
        path = os.path.dirname(os.path.realpath(__file__)) + "/data"
        open(path, 'w').close()
        load_data()

def move():
        try:
                input = [*str(move_entry.get())]
                input = list(map(replace2, input))
                input = list(map(int, input))
                network.input_layer = input
                network.compute_network()
                l = sorted(range(len(network.output_layer)), key=lambda k: network.output_layer[k])
                l.reverse()
                l = [x+1 for x in l]
                print("\nOutput layer:\n", network.output_layer, "\n\nMoves in preferred order:\n", l, "\n")
        except:
                print("Error")

network = network.network(sizes)
global data
load_data()

main_window = window()

main_window.title("Tris AI")
main_window.geometry("450x200")

train_button = Button(main_window, text = "Train", command = lambda: network.train(it, data, step))
load_data_button = Button(main_window, text = "Load Data", command = load_data)
clear_data_button = Button(main_window, text = "Clear Data", command = clear_data)
game_button = Button(main_window, text = "Play", command = lambda:game.game(network, save_data.get(), vs_ai.get(), ai_starts.get()))
vs_ai = IntVar()
vs_ai_checkbutton = Checkbutton(main_window, text = "Vs AI", variable=vs_ai, onvalue=True, offvalue=False)
ai_starts = IntVar()
ai_starts_checkbutton = Checkbutton(main_window, text = "AI starts", variable=ai_starts, onvalue=True, offvalue=False)
save_data = IntVar()
save_data_checkbutton = Checkbutton(main_window, text = "Save Data", variable = save_data, onvalue = True, offvalue = False)
move_button = Button(main_window, text = "Check Move", command = move)
move_entry = Entry(main_window)

train_button.grid(row=0, column=0)
load_data_button.grid(row=0, column=1)
clear_data_button.grid(row=0, column=2)
game_button.grid(row=1, column=0)
save_data_checkbutton.grid(row=1, column=3)
ai_starts_checkbutton.grid(row=1, column=2)
vs_ai_checkbutton.grid(row=1, column=1)
move_button.grid(row=2, column=0)
move_entry.grid(row=2, column=1)

main_window.mainloop()