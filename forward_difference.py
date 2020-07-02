def forward_difference(f, x=0, h=0.001):
    return (f(x+h) - f(x)) / h

def backward_difference(f, x=0, h=0.001):
    return (f(x) - f(x-h)) / h

def central_difference(f, x=0, h=0.001):
    return (f(x+h/2) - f(x-h/2)) / h

def newtons_method(f, x0=0, iter=1000):
    x = x0
    for i in range(iter):
        x = x - f(x) / central_difference(f, x)
    return x

f = lambda x: x ** 3 - 0.05

print(f)
print(forward_difference(f, 1))
print(backward_difference(f, 1))
print(central_difference(f, 1))
print(newtons_method(f))