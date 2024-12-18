import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def plot_vectors(vector, rotated_vector):
    if vector is None:
        raise ValueError("The vector is None")
    if rotated_vector is None:
        raise ValueError("The rotated vector is None")
    sns.set_style("whitegrid")
    sns.set_context("talk")
    plt.figure(figsize=(6, 6))
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='b', label='Original')
    plt.quiver(0, 0, rotated_vector[0], rotated_vector[1], angles='xy', scale_units='xy', scale=1, color='r',
               label='Rotated')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.legend()
    return plt.show()

def plot_hist(sums_list):
    sns.set_style("white")
    sns.set_context("talk")
    sns.histplot(sums_list, kde=True, bins=12)
    plt.ylabel("")
    plt.yticks([])
    sns.despine(left=True)
    return plt.show()

def plot_decision_boundary(clf, X, y):
    x_min, x_max = X.iloc[:, 0].min() - 1, X.iloc[:, 0].max() + 1
    y_min, y_max = X.iloc[:, 1].min() - 1, X.iloc[:, 1].max() + 1

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    if type(X) == pd.DataFrame:
        X = X.values
    if type(y) == pd.Series:
        y = y.values

    x1 = X[:, 0]
    x2 = X[:, 1]
    plot_df = pd.DataFrame({'x1': x1, 'x2': x2, 'y': y})

    sns.scatterplot(data=plot_df, x='x1', y='x2', hue='y', palette='colorblind')
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')


def plot_gradient_descent(f, xs):
    import matplotlib.pyplot as plt
    import seaborn as sns

    x_range = np.linspace(-2, 2, 100)
    y = f(x_range)

    sns.set_style('whitegrid')
    sns.set_context('talk')

    plt.plot(x_range, y)
    plt.scatter(xs, [f(x) for x in xs], c='crimson', s=100)