import numpy as np

def sigmoid(x):
	return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
	return x * (1.0 - x)
	
def ReLU(x):
    return abs(x) * (x > 0)

def dReLU(x):
    return 1. * (x > 0)

class NeuralNetwork:
	def __init__(self, x, y):
		self.input = x
		self.weights1 = np.random.rand(self.input.shape[1],4)
		self.weights2 = np.random.rand(4,1)
		self.y = y
		self.output = np.zeros(self.y.shape)
	
	def feedforward(self):
		self.layer1 = sigmoid(np.dot(self.input,self.weights1))
		self.output = sigmoid(np.dot(self.layer1,self.weights2))
		
	def backpropagation(self):
		d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
		d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))
		
		self.weights1 += d_weights1
		self.weights2 += d_weights2

if __name__ == '__main__':
	X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
	y = np.array([[0],[1],[1],[0]])
	nn = NeuralNetwork(X,y)

	for i in range(1500):
		#print('im in iteration'+str(i))
		nn.feedforward()
		nn.backpropagation()
	
	print(nn.output)