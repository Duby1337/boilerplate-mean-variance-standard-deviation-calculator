import numpy as np

def calculate(l: list):

    if len(l) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list into matrix
    M = np.array(l).reshape(3, 3)
    
    # Create empty lists to store values
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    for i in range(3):
        if i == 2:
            calculations['mean'].append(M.mean().item())
            calculations['variance'].append(M.var().item())
            calculations['standard deviation'].append(M.std().item())
            calculations['max'].append(M.max().item())
            calculations['min'].append(M.min().item())
            calculations['sum'].append(M.sum().item())
        else:
            calculations['mean'].append(M.mean(axis = i).tolist())
            calculations['variance'].append(M.var(axis = i).tolist())
            calculations['standard deviation'].append(M.std(axis = i).tolist())
            calculations['max'].append(M.max(axis = i).tolist())
            calculations['min'].append(M.min(axis = i).tolist())
            calculations['sum'].append(M.sum(axis = i).tolist())

    return calculations