import matplotlib.pyplot as plt
import seaborn as sns

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