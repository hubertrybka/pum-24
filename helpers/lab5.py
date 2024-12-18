import numpy as np

class SimplePerceptron:
    def __init__(self, alpha=0.1):
        self.w1 = 0
        self.w2 = 0
        self.b = 0
        self.alpha = alpha

    def forward(self, x):
        y = self.w1 * x[0] + self.w2 * x[1] + self.b
        return 1 / (1 + np.exp(-y))

    def loss(self, y_pred, y):
        return -y * np.log(y_pred) - (1 - y) * np.log(1 - y_pred)

    @staticmethod
    def get_grad_w1(x, y_pred, y_true):
        return (y_pred - y_true) * x[0]

    @staticmethod
    def get_grad_w2(x, y_pred, y_true):
        return (y_pred - y_true) * x[1]

    @staticmethod
    def get_grad_b(y_pred, y_true):
        return y_pred - y_true

    def update(self, x, y_pred, y_true):
        self.w1 -= self.alpha * self.get_grad_w1(x, y_pred, y_true)
        self.w2 -= self.alpha * self.get_grad_w2(x, y_pred, y_true)
        self.b -= self.alpha * self.get_grad_b(y_pred, y_true)