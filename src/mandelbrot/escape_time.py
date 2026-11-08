def escape_time(a, b, MAX_ITER):

    x = 0
    y = 0

    for n in range(MAX_ITER):

        x_kvadrat = x * x
        y_kvadrat = y * y
        modul_kvadrat = x_kvadrat + y_kvadrat

        if modul_kvadrat > 4:
            return (1, n)

        x_novi = x_kvadrat - y_kvadrat + a
        y_novi = 2 * x * y + b

        x = x_novi
        y = y_novi

    return (0, MAX_ITER)

# 14 linija koda