def f(x):
    result = 0 # 1 operation
    for i in range(1000):
        result += 1 # 1000 operations

    for i in range(x):
        result += x # x operations
    
    for i in range(x):
        for j in range(x):
            result += 1 
            result += 1 # 2*x*x operations

    return result # 1 operation
    # 1 + 1000 + x + 2*x*x + 1 = 2x^2 + x + 1002 operations