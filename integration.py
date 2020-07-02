def trapezoidal_rule(f, a, b, n=1000):

    if type(n) == float:
        n = int(n)

    h = (b - a) / n
    x = a
    sum = 0

    for i in range(n+1):
        if i == 0 or i == n:
            sum += f(x)
        else:
            sum += 2 * f(x)
        x += h
    return sum * h / 2

def simpsons_rule(f, a, b, n=1000):
    
    if type(n) == float:
        n = int(n)
    
    if n % 2 == 1:
        # n += 1
        raise ValueError("n must be an even integer.")

    h = (b - a) / n
    x = a
    sum = 0

    for i in range(n+1):
        if i == 0 or i == n:
            sum += f(x)
        elif i % 2 == 1:
            sum += 4 * f(x)
        else:
            sum += 2 * f(x)
        x += h
    return sum * h / 3

def adaptive_simpsons_rule(f, a, b, n0=2, tol = 1e-6):

    n = n0
    S = [None] * 2
    S[0] = simpsons_rule(f, a, b, n)
    S[1] = simpsons_rule(f, a, b, 2*n)
    E2 = (S[1] - S[0]) / 15

    while abs(E2) >= tol:
        n = n * 2
        S[0] = S[1]
        S[1] = simpsons_rule(f, a, b, 2*n)
        E2 = (S[1] - S[0]) / 15

    return S[1]
    
    # return (16*S[1] - S[0]) / 15  # Richardson’s extrapolation further reduces the error.

if __name__ == "__main__":
    import math
    f = lambda x: math.sin(x) * (x ** 2)
    print(trapezoidal_rule(f, 0, math.pi))
    print(simpsons_rule(f, 0, math.pi))
    print(adaptive_simpsons_rule(f, 0, math.pi))
