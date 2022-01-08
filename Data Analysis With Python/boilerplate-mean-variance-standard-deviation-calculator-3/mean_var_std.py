import numpy as np

def calculate(list):
    # if len(list) == 9:
    #     arr = np.array([list])
    #     arr = np.reshape(arr, (3, 3))
    # else:
    #     raise ValueError("List must contain nine numbers.")

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        arr = np.array([list])
        arr = np.reshape(arr, (3, 3))

    calculations = {
                    'mean': [],
                    'variance': [],
                    'standard deviation': [],
                    'max': [],
                    'min': [],
                    'sum': []
                   }
    axis1 = np.mean(arr, axis = 0)
    axis2 = np.mean(arr, axis = 1)
    flattened = np.mean(arr)
    calculations['mean'] = [axis1.tolist(),axis2.tolist(),flattened.tolist()]

    axis1 = np.var(arr, axis=0)
    axis2 = np.var(arr, axis=1)
    flattened = np.var(arr)
    calculations['variance'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

    axis1 = np.std(arr, axis=0)
    axis2 = np.std(arr, axis=1)
    flattened = np.std(arr)
    calculations['standard deviation'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

    axis1 = np.max(arr, axis=0)
    axis2 = np.max(arr, axis=1)
    flattened = np.max(arr)
    calculations['max'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

    axis1 = np.min(arr, axis=0)
    axis2 = np.min(arr, axis=1)
    flattened = np.min(arr)
    calculations['min'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

    axis1 = np.sum(arr, axis=0)
    axis2 = np.sum(arr, axis=1)
    flattened = np.sum(arr)
    calculations['sum'] = [axis1.tolist(), axis2.tolist(), flattened.tolist()]

    return calculations