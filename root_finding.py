def bisection_method(f, x0, x1, threshold=0.001, iter=1000):
    i = 0
    while abs(x0-x1) >= threshold and i < iter:
        x_mid = (x1 + x0) / 2
        if f(x_mid) * f(x0) < 0:
            x1 = x_mid
        elif f(x_mid) * f(x1) < 0:
            x0 = x_mid
        i += 1
    return (x0 + x1) / 2

def central_difference(f, x=0, h=0.001):
    return (f(x+h/2) - f(x-h/2)) / h

def newtons_method(f, x0=0, iter=1000):
    x = x0
    for i in range(iter):
        x -= f(x) / central_difference(f, x)
    return x

def secant_method(f, x0=0, x1=1, threshold=0.001):
    x = [x0, x1]
    fx = [f(x0), f(x1)]
    
    while abs(x[0]-x[1]) >= threshold:
        x2 = x[1] - (x[1] - x[0]) * fx[1] / (fx[1] - fx[0])
        
        x[0], x[1] = x[1], x2
        fx[0], fx[1] = fx[1], f(x2)
    
    return x[1]


if __name__ == "__main__":
    f = lambda x: x ** 3 - 0.05
    print(bisection_method(f, 0, 1, 1e-6))
    print(newtons_method(f))
    print(secant_method(f))
