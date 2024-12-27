import numpy as np

def normal_distribution(x, mu, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def update_weights(w, X, y, y_pred, alpha=0.0005):
    n = X.shape[0]
    for i in range(n):
        error = y_pred[i] - y[i]
        w -= alpha * error * X[i]
    return w

def mean_squared_error(y, y_pred):
    return np.mean((y - y_pred) ** 2)

def binary_cross_entropy(y, y_pred):
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)  
    return -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))


if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5])
    mu = 3
    sigma = 1

    print("Normal Distribution:", normal_distribution(x, mu, sigma))

    print("Sigmoid:", sigmoid(x))

    w = np.array([0.5, 0.5])
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 1, 0, 1, 0])
    y_pred = sigmoid(np.dot(X, w))
    updated_w = update_weights(w, X, y, y_pred)
    print("Updated Weights:", updated_w)

    y_true = np.array([1, 2, 3, 4, 5])
    y_pred = np.array([1.1, 1.9, 3.2, 3.8, 5.1])
    print("Mean Squared Error:", mean_squared_error(y_true, y_pred))

    y_true = np.array([0, 1, 0, 1, 0])
    y_pred = np.array([0.1, 0.9, 0.2, 0.8, 0.3])
    print("Binary Cross Entropy:", binary_cross_entropy(y_true, y_pred))
    