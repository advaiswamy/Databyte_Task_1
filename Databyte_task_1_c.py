import numpy as np

class MPNeuron:
    '''Implementation of a MPNeuron'''

    def __init__(self):
        self.n = [1, 1, 1]
        self.weight = [1, 1, 1]
        self.threshold = 2.5

    def MP_Neuron_Input(self, n, weights, threshold):
        self.n = n
        self.weights = weights 
        self.threshold = threshold
    
    def MP_Neuron_Evaluate(self):
        a = np.array(self.n).reshape(1,-1)
        w = np.array(self.weight).reshape(-1,1)
        result = np.dot(a, w)
        if result > self.threshold:
            return 1
        return 0

def NAND(x1, x2, x3):
    y = MPNeuron()
    y.MP_Neuron_Input([-x1, -x2, -x3], [1, 1, 1], -3)
    x = y.MP_Neuron_Evaluate()
    return x



x = NAND(1,1,1)
print(x)