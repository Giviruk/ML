import random
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm._libsvm import predict
from sklearn.datasets import make_blobs
from matplotlib.colors import ListedColormap


class SVM:
    def __init__(self, c=10000, max_iter=100000):
        self.kernel = lambda x, y: np.dot(x, y.T)
        self.C = c
        self.max_iter = max_iter

    # ограничение параметра t, чтобы новые лямбды не покидали границ квадрата
    def restrict_to_square(self, t, v0, u):
        t = (np.clip(v0 + t * u, 0, self.C) - v0)[1] / u[1]
        return (np.clip(v0 + t * u, 0, self.C) - v0)[0] / u[0]

    def fit(self, X, y):
        self.X = X.copy()
        self.y = y * 2 - 1
        self.lambdas = np.zeros_like(self.y, dtype=float)
        self.K = self.kernel(self.X, self.X) * self.y[:, np.newaxis] * self.y

        for _ in range(self.max_iter):
            for idxM in range(len(self.lambdas)):
                idxL = np.random.randint(0, len(self.lambdas))
                Q = self.K[[[idxM, idxM], [idxL, idxL]], [[idxM, idxL], [idxM, idxL]]]
                v0 = self.lambdas[[idxM, idxL]]
                k0 = 1 - np.sum(self.lambdas * self.K[[idxM, idxL]], axis=1)
                u = np.array([-self.y[idxL], self.y[idxM]])
                t_max = np.dot(k0, u) / (np.dot(np.dot(Q, u), u) + 1E-15)
                self.lambdas[[idxM, idxL]] = v0 + u * self.restrict_to_square(t_max, v0, u)

        # найти индексы опорных векторов
        idx, = np.nonzero(self.lambdas > 1E-15)
        self.b = np.mean((1.0 - np.sum(self.K[idx] * self.lambdas, axis=1)) * self.y[idx])

    def decision_function(self, x):
        return np.sum(self.kernel(x, self.X) * self.y * self.lambdas, axis=1) + self.b

    def predict(self, x):
        return (np.sign(self.decision_function(x)) + 1) // 2


def draw(X, y, svm_model):
    global xlim
    global ylim
    xlim = [np.min(X[:, 0]) - 1, np.max(X[:, 0]) + 1]
    ylim = [np.min(X[:, 1]) - 1, np.max(X[:, 1]) + 1]
    xx, yy = np.meshgrid(np.linspace(*xlim, num=500), np.linspace(*ylim, num=500))
    rgb = np.array([[210, 0, 0], [0, 0, 150]]) / 255.0

    svm_model.fit(X, y)
    z_model = svm_model.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

    plt.scatter(X[:, 0], X[:, 1], c=y, s=25, cmap='cool')
    plt.contour(xx, yy, z_model, colors='k', levels=[-1, 0, 1], alpha=1, linestyles=['--', '.', '--'])
    plt.contourf(xx, yy, np.sign(z_model.reshape(xx.shape)), alpha=0.3, levels=2, cmap=ListedColormap(rgb), zorder=1)


array, group = make_blobs(n_samples=10, centers=2, random_state=2, cluster_std=1.5)
model = SVM(c=10, max_iter=50)
draw(array, group, model)
plt.show()


points_to_add = 10
for _ in range(points_to_add):
    itemX = random.uniform(xlim[0], xlim[1])
    itemY = random.uniform(ylim[0], ylim[1])
    item = [[itemX, itemY]]
    array = np.append(array, item, axis=0)
    group = model.predict(array)
    draw(array, group, model)
    predict()
    plt.show()