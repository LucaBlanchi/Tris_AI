import numpy as np
from random import randrange
import utilities

class network():

    def __init__(self, sizes):
        self.sizes = sizes

        self.input_layer = [0 in range(9)]
        self.layer0 = [0 in range(sizes[0])]
        self.layer1 = [0 in range(sizes[1])]
        self.output_layer = [0 in range(9)]

        self.correct_output = [0 for i in range (9)]

        self.undistorted_layer0 = [0 for i in range (sizes[0])]
        self.undistorted_layer1 = [0 for i in range (sizes[1])]
        self.undistorted_ouput_layer = [0 for i in range (9)]

        self.weights_i_to_0 = [[0.5 for i in range (sizes[0])] for j in range (9)]
        self.weights_0_to_1 = [[0.5 for i in range (sizes[1])] for j in range (sizes[0])]
        self.weights_1_to_o = [[0.5 for i in range (9)] for j in range (sizes[1])]

        self.bias_layer0 = [0 for i in range (sizes[0])]
        self.bias_layer1 = [0 for i in range (sizes[1])]
        self.bias_output_layer = [0 for i in range (9)]
    
    def compute_network(self):
        self.undistorted_layer0 = np.dot(self.input_layer, self.weights_i_to_0) + self.bias_layer0
        self.layer0 = utilities.sigmoid(self.undistorted_layer0)
        self.undistorted_layer1 = np.dot(self.layer0, self.weights_0_to_1) + self.bias_layer1
        self.layer1 = utilities.sigmoid(self.undistorted_layer1)
        self.undistorted_ouput_layer = np.dot(self.layer1, self.weights_1_to_o) + self.bias_output_layer
        self.output_layer = utilities.sigmoid(self.undistorted_ouput_layer)

    def back_propagation(self, step):
        d_output = np.multiply((self.output_layer - self.correct_output), utilities.d_sigmoid(self.undistorted_ouput_layer))
        d_1 = np.multiply(np.dot(self.weights_1_to_o, d_output), utilities.d_sigmoid(self.undistorted_layer1))
        d_0 = np.multiply(np.dot(self.weights_0_to_1, d_1), utilities.d_sigmoid(self.undistorted_layer0))
            
        dc_bias0 = d_0
        dc_bias1 = d_1
        dc_bias_output = d_output
            
        self.bias_layer0 = self.bias_layer0 - step*dc_bias0
        self.bias_layer1 = self.bias_layer1 - step*dc_bias1
        self.bias_output_layer = self.bias_output_layer - step*dc_bias_output
            
        dc_weights_i_to_0 = [0 for i in range (9)]
        dc_weights_0_to_1 = [0 for i in range (self.sizes[0])]
        dc_weights_1_to_o = [0 for i in range (self.sizes[1])]
            
        for i in range (9):
            dc_weights_i_to_0[i] = self.input_layer[i]*d_0
            self.weights_i_to_0[i] = self.weights_i_to_0[i] - step*self.input_layer[i]*d_0
            
        for i in range (self.sizes[0]):
            dc_weights_0_to_1[i] = self.layer0[i]*d_1
            self.weights_0_to_1[i] = self.weights_0_to_1[i] - step*self.layer0[i]*d_1
                
        for i in range (self.sizes[1]):
            dc_weights_1_to_o[i] = self.layer1[i]*d_output
            self.weights_1_to_o[i] = self.weights_1_to_o[i] - step*self.layer1[i]*d_output

    def cost(self):
        return np.linalg.norm(self.output_layer - self.correct_output)

    def train(self, it, data, step):
        try:
            for _ in range(it):
                n = randrange(len(data))
                self.input_layer = data[n][0]
                self.correct_output = data[n][1]
                self.compute_network()
                self.back_propagation(step)
                print(n, self.cost())
        except:
            print("Empty dataset")