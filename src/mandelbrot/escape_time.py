def escape_time(a, b, MAX_ITER):

    x = 0
    y = 0

    for n in range(0, MAX_ITER):

        x_kvadrat = x * x
        y_kvadrat = y * y

        x_novi = x_kvadrat - y_kvadrat + a
        y_novi = 2 * x * y + b

        x = x_novi
        y = y_novi

        modul_kvadrat = x * x + y * y

        if modul_kvadrat > 4:
            return (1, n)

    return (0, MAX_ITER)

# 14 linija koda