def escape_time(a, b, MAX_ITER):

    x = 0
    y = 0

    for n in range(0, MAX_ITER):

        x_novi = x*x - y*y + a
        y_novi = 2*x*y + b

        x = x_novi
        y = y_novi

        if x*x + y*y > 4:
            return (1, n)

    return (0, MAX_ITER)
