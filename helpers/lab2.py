import numpy as np

class LinReg:

    def __init__(self):
        self.weights = None

    def fit(self, X, y):
        design_matrix = self.get_design_matrix(X)
        w = np.linalg.inv(design_matrix.T @ design_matrix) @ design_matrix.T @ y
        self.weights = w

    def predict(self, X):
        design_matrix = self.get_design_matrix(X)
        return design_matrix @ self.weights

    @staticmethod
    def get_design_matrix(X):
        ones = np.ones(len(X)).reshape(-1, 1)
        design_matrix = np.concatenate([ones, X], axis=1)
        return design_matrix