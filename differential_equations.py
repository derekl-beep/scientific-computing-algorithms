def euler_method(f, x0, delta_t=0.001):
    return x0 + delta_t * f(x0)

def modified_euler_method(f, x0, delta_t=0.001):
    alpha = beta = 1
    a = b = 0.5

    k1 = delta_t * f(x0)
    k2 = delta_t * f(x0 + beta * k1)
    return x0 + a*k1 + b*k2

def midpoint_method(f, x0, delta_t=0.001):
    alpha = beta = 0.5
    a = 0
    b = 1

    k1 = delta_t * f(x0)
    k2 = delta_t * f(x0 + beta * k1)
    return x0 + a*k1 + b*k2

def fourth_order_runge_kutta_method(f, x0, delta_t=0.001):
    k1 = delta_t * f(x0)
    k2 = delta_t * f(x0 + 0.5 * k1)
    k3 = delta_t * f(x0 + 0.5 * k2)
    k4 = delta_t * f(x0 + k3)
    return x0 + (k1 + 2*k2 + 2*k3 + k4) / 6


if __name__ == "__main__":
    x_dot = lambda x: x ** 2 - x + 1
    step_count = 10


    step = [None] * step_count
    step[0] = 0

    x = [None] * step_count
    x[0] = 1
    
    for i in range(1,len(step)):
        step[i] = i
        x[i] = euler_method(x_dot, x[i-1])
    print('Euler Method: \t \t {}'.format(x))

    for i in range(1,len(step)):
        step[i] = i
        x[i] = modified_euler_method(x_dot, x[i-1])
    print('Modified Euler Method: \t {}'.format(x))

    for i in range(1,len(step)):
        step[i] = i
        x[i] = midpoint_method(x_dot, x[i-1])
    print('Midpoint Method: \t {}'.format(x))

    for i in range(1,len(step)):
        step[i] = i
        x[i] = fourth_order_runge_kutta_method(x_dot, x[i-1])
    print('4th-order R-K Method: \t {}'.format(x))

